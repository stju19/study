#!/usr/bin/env python
"""
Compare two simian report files, and then show increased duplicate lines
"""
import os
import sys
import json
import argparse
import commands
from xml.dom.minidom import parse

reload(sys)
sys.setdefaultencoding("utf-8")
java_bin = "/usr/java/latest/bin/java"
simian_bin = "/var/lib/simian-enhanced/simian-2.5.3.jar"


class ArgumentParser(object):
    def __init__(self, argv):
        self.parser = argparse.ArgumentParser(description=__doc__)
        self.argv = argv
        self.args = None
        self.init_parser()

    def init_parser(self):
        self.parser.add_argument("file1", metavar='<old report file>',
                                 help="old simian report file")
        self.parser.add_argument("file2", metavar='<new report file>',
                                 help="new simian report file")
        self.parser.add_argument("--filter", metavar='<filter>',
                                 help="will only check files which in file filter")
        self.parser.add_argument("--java", metavar='<java>', help="java binary",
                                 default="/usr/java/latest/bin/java")
        self.parser.add_argument("--simian", metavar='<simian>', help="simian jar package",
                                 default="/var/lib/simian-enhanced/simian-2.5.3.jar")
        self.parser.add_argument("-d", "--debug", action='store_true', default=False)
        self.args = self.parser.parse_args(self.argv)


class CodeBlock(object):
    def __init__(self, code, line="10"):
        self.code = code
        self.line = line

    def create_cmp_file(self, file_name):
        commands.getstatusoutput("mkdir -p .simian_tmp")
        commands.getstatusoutput("touch .simian_tmp/%s" % file_name)

        f = open(".simian_tmp/%s" % file_name, "w")
        text_str = "void func(void)\n{\n" + self.code + "}\n"
        f.write(text_str)
        f.close()

    def __eq__(self, other):
        self.create_cmp_file("a.c")
        other.create_cmp_file("b.c")
        cmd = "%s -jar %s -includes=./.simian_tmp/*.c -threshold=%s &>/dev/null" % (java_bin, simian_bin, self.line)
        (status, output) = commands.getstatusoutput(cmd)
        return bool(status)


class SimianReportParser(object):
    def __init__(self, file_name, filter_file=None):
        self.content = None
        self.file_name = file_name
        self.read_xml_file(file_name)
        self.filter_file = filter_file
        self.filter = self.get_filter_list()

        self.result = self.parse_simian_report()
        self.duplicate_line_count = self.result["summary"]["duplicateLineCount"]
        self.duplicate_file_count = self.result["summary"]["duplicateFileCount"]
        self.total_file_count = self.result["summary"]["totalFileCount"]
        self.total_line_count = self.result["summary"]["totalLineCount"]
        self.total_raw_line_count = self.result["summary"]["totalRawLineCount"]

    def get_filter_list(self):
        if not self.filter_file:
            return []
        if not os.path.exists(self.filter_file):
            print("file %s is not exist" % self.filter_file)
            exit(1)
        f = open(self.filter_file, "r")
        filter_list = f.read().splitlines()
        f.close()
        return filter_list

    def read_xml_file(self, file_name):
        try:
            dom_tree = parse(file_name)
            self.content = dom_tree.documentElement
        except Exception:
            print("Error: parse xml file %s failed" % file_name)
            exit(1)

    def parse_simian_report(self):
        summary = {
            "duplicateFileCount": int(self.get_summary_attribute("duplicateFileCount")),
            "duplicateLineCount": int(self.get_summary_attribute("duplicateLineCount")),
            "totalRawLineCount": int(self.get_summary_attribute("totalRawLineCount")),
            "totalLineCount": int(self.get_summary_attribute("totalSignificantLineCount")),
            "totalFileCount": int(self.get_summary_attribute("totalFileCount"))
        }
        if not summary["duplicateLineCount"]:
            return {"check": {}, "summary": summary}

        check = {}
        for item in self.content.getElementsByTagName("set"):
            is_source_file_in_filter = False
            if item.getAttribute("lineCount") not in check:
                check[item.getAttribute("lineCount")] = []

            file = []
            for block in item.getElementsByTagName("block"):
                if block.getAttribute("sourceFile") in self.filter:
                    is_source_file_in_filter = True
                source_file = [block.getAttribute("sourceFile"), block.getAttribute("startLineNumber"),
                               block.getAttribute("endLineNumber")]
                file.append(source_file)
            text = item.getElementsByTagName("text")[0].childNodes[1].data
            dup_set = {"sourceFile": file, "text": text}
            if not self.filter_file:
                is_source_file_in_filter = True
            if is_source_file_in_filter:
                check[item.getAttribute("lineCount")].append(dup_set)

        result = {"check": check, "summary": summary}
        return result

    def get_summary_attribute(self, attr):
        return self.content.getElementsByTagName("summary")[0].getAttribute(attr)

    def report_check_detail(self):
        detail = {}
        for line_count in sorted(self.result["check"]):
            detail[line_count] = len(self.result["check"][line_count])
        print json.dumps(detail, indent=4, sort_keys=True)

    def __str__(self):
        return json.dumps(self.result, indent=4, sort_keys=True)
    __repr__ = __str__


class SimianReportComparer(object):
    def __init__(self, report_old, report_new):
        self.old = report_old
        self.new = report_new
        self.cmp_result = None

    def compare_simian_report(self):
        if self.new.duplicate_line_count <= self.old.duplicate_line_count:
            print("Everything is Ok!")
            return True

        new_check = self.new.result["check"]
        old_check = self.old.result["check"]
        for line_count in sorted(new_check):
            for new_dup_code in new_check[line_count]:
                is_new_dup_code_matched = False
                for old_dup_code in old_check.get(line_count, []):
                    new_code_block = CodeBlock(new_dup_code["text"], line_count)
                    old_code_block = CodeBlock(old_dup_code["text"], line_count)
                    if new_code_block == old_code_block:
                        if len(new_dup_code["sourceFile"]) > len(old_dup_code["sourceFile"]):
                            self.report_increase_simian(new_dup_code, line_count)
                        is_new_dup_code_matched = True
                        break
                if not is_new_dup_code_matched:
                    self.report_increase_simian(new_dup_code, line_count)
        return False

    def report_increase_simian(self, new_code, duplicate_count):
        print("Found %s duplicate lines in the following files:" % duplicate_count)
        for item in new_code["sourceFile"]:
            print(" Between lines %s and %s in %s" % (item[1], item[2], item[0]))
        print(new_code["text"])
        print("=====================================================================")

    def report_check_detail(self):
        print(self.old.file_name + ":")
        self.old.report_check_detail()
        print(self.new.file_name + ":")
        self.new.report_check_detail()


def report_summary(old, new):
    increase_duplicate_count = new.duplicate_line_count - old.duplicate_line_count
    print("Found %s duplicate lines in %s files from %s" % (
        new.duplicate_line_count, new.total_file_count,new.file_name))
    print("increase %s duplicate lines from %s to %s" % (
        increase_duplicate_count, old.file_name, new.file_name))
    print("Processed a total of %s significant (%s raw) lines in %s files" % (
        new.total_line_count, new.total_raw_line_count, new.total_file_count))


def check_java_version():
    if not os.path.exists(java_bin):
        print("Error: package java >= 1.8 is not installed")
        exit(1)
    version = commands.getstatusoutput(java_bin + " -version")[1].splitlines()[0].split('"')[1]
    if int(version.split(".")[1]) < 8:
        print("Error: java version %s is lower than 1.8" % version)
        exit(1)


def main(parameter):
    report1 = SimianReportParser(parameter.args.file1, parameter.args.filter)
    report2 = SimianReportParser(parameter.args.file2, parameter.args.filter)
    comparer = SimianReportComparer(report1, report2)
    if parameter.args.debug:
        print("filtered report(%s):\n" % parameter.args.file1 + str(report1))
        print("filtered report(%s):\n" % parameter.args.file2 + str(report2))
        comparer.report_check_detail()
    result = comparer.compare_simian_report()
    report_summary(report1, report2)
    exit(0 if result else 1)


if __name__ == "__main__":
    parameter = ArgumentParser(sys.argv[1:])
    java_bin = parameter.args.java
    simian_bin = parameter.args.simian
    check_java_version()
    main(parameter)
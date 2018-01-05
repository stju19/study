#!/usr/bin/env python
__author__ = '10183988'

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
        self.parser.add_argument("file", metavar='<new report file>',
                                 help="new simian report file")
        self.parser.add_argument("--java", metavar='<java>', help="java binary",
                                 default="/usr/java/latest/bin/java")
        self.parser.add_argument("--simian", metavar='<simian>', help="simian jar package",
                                 default="/var/lib/simian-enhanced/simian-2.5.3.jar")
        self.parser.add_argument("-d", "--debug", action='store_true', default=False)
        self.args = self.parser.parse_args(self.argv)


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


def check_java_version():
    if not os.path.exists(java_bin):
        print("Error: package java >= 1.8 is not installed")
        exit(1)
    version = commands.getstatusoutput(java_bin + " -version")[1].splitlines()[0].split('"')[1]
    if int(version.split(".")[1]) < 8:
        print("Error: java version %s is lower than 1.8" % version)
        exit(1)


def main(parameter):
    report = SimianReportParser(parameter.args.file)
    if parameter.args.debug:
        print("filtered report(%s):\n" % parameter.args.file + str(report))
    print(report)

if __name__ == "__main__":
    parameter = ArgumentParser(sys.argv[1:])
    java_bin = parameter.args.java
    simian_bin = parameter.args.simian
    check_java_version()
    main(parameter)


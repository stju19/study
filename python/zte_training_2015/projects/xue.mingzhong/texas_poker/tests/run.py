__author__ = 'xue.mingzhong'

import sys
import subprocess
from os.path import dirname,abspath

test_path = dirname(abspath(sys.argv[0]))

run_cmd = "python -m coverage run -m unittest discover %s" % test_path
subprocess.call(run_cmd, shell=True)
subprocess.call( "python -m coverage report", shell=True)


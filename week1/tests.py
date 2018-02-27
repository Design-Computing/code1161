"""Do the work of checking the week's work."""

import sys
import os
import inspect
from pathlib import Path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from codeHelpers import completion_message
from codeHelpers import nyan_cat
from codeHelpers import test
from codeHelpers import test_flake8
from codeHelpers import ex_runs

# from codeHelpers import test
from week1 import exercise1
WEEK_NUMBER = 1

# the context of this file
LOCAL = os.path.dirname(os.path.realpath(__file__))
# The curent working directory
CWD = os.getcwd()

testResults = []


def test_hello_world():
    source = ''.join(inspect.getsourcelines(exercise1)[0]).lower()
    if "print('hello world!')" in source or 'print("hello world!")' in source:
        return True
    return False
    
def test_dev_env():
    if os.system("""python -c 'print("python installed")'""") == 0:
        return True
    return False

def lab_book_entry_completed():
    lab_book = Path("week1/readme.md")
    if lab_book.is_file():
        with open(lab_book, 'r') as f:
            lines = f.readlines()
            if lines == ['TODO: Reflect on what you learned this week and what is still unclear.\n']:
                return False
            elif lines:
                return True
    return False
                

if __name__ == '__main__':
    testResults.append(test(test_dev_env(), "Python is installed and configured on this machine"))    
    testResults.append(test(test_hello_world(), "Exercise1: Print 'Hello world!"))
    testResults.append(test(lab_book_entry_completed(), "Lab book entry completed"))    


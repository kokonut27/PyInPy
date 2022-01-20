# python in python - does NOT use python builtin function (cough cough exec() cough cough)

import time
import datetime
import os
import sys


def traceback(line, error_type, file, actual_error):
  if type(line) != int:
    exit("pyinpy error:\n\tline number is not an integer!")
  class_error = actual_error.find("=")

  if class_error == -1:
    line = str(line)
    print(f"Traceback (most recent call last):\n  File \"<{file}>\", line {line}, in <module>\n    {actual_error}\nNameError: name '{actual_error}' is not defined")
  else:
    if_defined = actual_error[class_error:]
    if if_defined.find("\"") == -1:
      exit("")

    elif if_defined.find("'") != -1:
      if if_defined not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        exit("")
    else:
      exit("")

# traceback("e", "e", "e")


ver_ = sys.version #[:39]
ver = "Python "+ver_+" on linux\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information."

def clear():
  os.system("clear")

def help_func():
  print("Type help() for interactive help, or help(object) for help about object.")

def interactive_help_func():
  print("\nWelcome to Python 3.8's help utility!\nIf this is your first time using Python, you should definitely check out\nthe tutorial on the Internet at https://docs.python.org/3.8/tutorial/.\nEnter the name of any module, keyword, or topic to get help on writing\nPython programs and using Python modules.  To quit this help utility and\nreturn to the interpreter, just type \"quit\".\nTo get a list of available modules, keywords, symbols, or topics, type\n\"modules\", \"keywords\", \"symbols\", or \"topics\".  Each module also comes with a one-line summary of what it does; to list the modules whose name\nor summary contain a given string such as \"spam\", type \"modules spam\".\n")
  while True:
    help_in = input("help> ")

    # Using builtin function for now smh
    print(help(help_in))

def create_func(func_name, arguments):
  pass

# current_time = datetime.datetime.now()
# header = current_time.strftime("%b %d %Y")

# clear()

print(ver)
while True:
  func = input(">>> ")

  if func == "help":
    help_func()
  elif func == "help()":
    interactive_help_func()
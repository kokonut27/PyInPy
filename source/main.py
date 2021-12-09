# python in python - does NOT use python builtin function (cough cough exec() cough cough)

import time
import datetime
import os
import sys


def traceback(line, error_type, file, actual_error):
  if type(line) != int:
    exit("pyinpy error:\n\tline number is not an integer!")
  line = str(line)
  class_error = actual_error.find("=")

  if class_error == -1:
    print(f"Traceback (most recent call last):\n  File \"<{file}>\", line {line}, in <module>\n    {actual_error}\nNameError: name '{actual_error}' is not defined")
  else:
    if_defined = actual_error[class_error:]
    if if_defined.find("\"") != -1:
      if if_defined.find("'") != -1:
        if if_defined in ["0","1","2","3","4","5","6","7","8","9"]:
          pass # it is a allowed statement var
        else:
          exit("")
      else:
        exit("")
    else:
      exit("")

# traceback("e", "e", "e")


ver_ = sys.version #[:39]
ver = "Python "+ver_+" on linux\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information."

def clear():
  os.system("clear")

def create_func(func_name, arguments):
  pass

# current_time = datetime.datetime.now()
# header = current_time.strftime("%b %d %Y")

# clear()

print(ver)
while True:
  func = input(">>> ")

  
import datetime
from os import name
import sys
import pip
import camelcase


def main():
    print(sys.exec_prefix + "\\Scripts")
    print(pip.__version__)
    print("Hello World!")
    printTime()
    c = camelcase.CamelCase()
    txt = "hello world"


def printTime():
    time = datetime.datetime.now()
    print("The time is ", time)


if __name__ == "__main__":
    main()

# 4.	Write a program to accept a filename as a command line argument and display its content line by line.
import sys


if len(sys.argv) != 2:
    print("Uages : python script.py filename")
    sys.exit(1)
    filename = sys.argv[1]
try:
    with open(filename, "r") as file:                 
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print("File Not Found Error")
        
# 1.	Implement a script that takes two numbers as "command line" arguments and prints their sum.
import sys

print("script name : ",sys.argv[0])
a = int(sys.argv[1])
b = int(sys.argv[2])
print("the sum is : ", a+b)
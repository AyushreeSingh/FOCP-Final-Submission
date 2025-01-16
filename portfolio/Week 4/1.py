''' 1. Functions are o en used to validate input. Write afunction that accepts a single
 integer as a parameter and returns Trueif the integer is in the range 0 to 100
 (inclusive), or False otherwise. Write a short program to test the function.'''

def integerFunc(x):
    if x in range (0,100):
        print("True")
    else:
        print("false")
num=int(input("enter a number"))
integerFunc(num)


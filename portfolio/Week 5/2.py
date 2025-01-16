'''2. Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an argument ).'''

import sys

sys.argv = ["count_args.py","arg1","arg2","arg3","arg4"] 

num_arguments = len(sys.argv) - 1

print(f"Number of arguments provided: {num_arguments}")

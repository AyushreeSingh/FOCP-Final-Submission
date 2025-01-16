'''3. Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them.'''

import sys

sys.argv = ["shortest_arg.py", "ayuu", "saku", "niki", "onion", "dada"]

arguments = sys.argv[1:]

if arguments:
    arguments.sort(key=len)
    print(f"The shortest argument is: {arguments[0]}")
else:
    print("No arguments were provided.")

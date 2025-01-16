'''1. The Unixnlcommand prints the lines of a text filewith a line number at the start
 of each line. (It can be useful when printing out programs for dry runs or white-box
 testing). Write an implementation of this command. It should take the name of the
 files as a command-line argument.'''

import sys

def print_file_with_line_numbers(filename):
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}\t{line}", end='')  # Print line number and line content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl.py <filename>")
    else:
        filename = sys.argv[1]
        print_file_with_line_numbers(filename)
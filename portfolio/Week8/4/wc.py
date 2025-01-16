''' 4.  The Unixwccommand counts the number of lines, words,and characters in a file.
 Write an implementation of this that takes a file name as a command-line
 argument, and then prints the number of lines and characters.
 Note: Linux (and Mac) users can use the "wc" commandto check the results of their
 implementation.'''

import sys

def wc(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read all lines
            num_lines = len(lines)  # Count the number of lines
            num_chars = sum(len(line) for line in lines)  # Count the number of characters
            
            # Print the results
            print(f"Lines: {num_lines}")
            print(f"Characters: {num_chars}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc.py <filename>")
    else:
        filename = sys.argv[1]
        wc(filename)
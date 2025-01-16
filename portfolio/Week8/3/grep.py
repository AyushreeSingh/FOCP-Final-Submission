''' 3. The Unixgrepcommand searches a file and outputsthe lines in the file that
 contain a certain pattern. Write an implementation of this. It will take two
 command-line arguments: the first is the string to look for, and the second is the
 file name. The output should be the lines in the file that contain the string.'''

import sys

def grep(pattern, filename):
    try:
        with open(filename, 'r') as file:
            # Read the file line by line
            for line_number, line in enumerate(file, start=1):
                # Check if the pattern is in the current line
                if pattern in line:
                    print(f"{line_number}: {line}", end='')  # Print line number and line content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <filename>")
    else:
        pattern = sys.argv[1]
        filename = sys.argv[2]
        grep(pattern, filename)
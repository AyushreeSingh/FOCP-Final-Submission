''' 2.  The Unixdiffcommand compares two files and reportsthe differences, if any.
 Write a simple implementation of this that takes two file names as command-line
 arguments and reports whether or not the two files are the same. (Define "same" as
 having the same contents.)'''

import sys

def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            # Read the contents of both files
            content1 = f1.read()
            content2 = f2.read()
            
            # Compare the contents
            if content1 == content2:
                print(f"The files '{file1}' and '{file2}' are the same.")
            else:
                print(f"The files '{file1}' and '{file2}' are different.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff.py <file1> <file2>")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        compare_files(file1, file2)
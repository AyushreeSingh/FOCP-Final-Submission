''' 5.  The Unixspellcommand is a simple spell-checker.It prints out all the words in a
 text file that are not found in a dictionary. Write and test an implementation of this,
 that takes a file name as a command-line argument.
 Note: You may want to simplify the program at first by testing with a text file that
 does not contain any punctuation. A complete version should obviously be able to
 handle normal files, with punctuation.
 Another Note: You will need a list of valid words. Linux users will already have one
 (probably in /usr/share/dict/words). It is more complicated,as usual, for
 Windows users. Happily, there are several available on GitHub.'''

import sys
import re

def load_dictionary(dictionary_file):
    """Load the dictionary file and return a set of valid words."""
    try:
        with open(dictionary_file, 'r') as file:
            # Read all words and convert them to lowercase
            valid_words = {line.strip().lower() for line in file}
        return valid_words
    except FileNotFoundError:
        print(f"Error: The dictionary file '{dictionary_file}' does not exist.")
        sys.exit(1)

def check_spelling(input_file, valid_words):
    """Check the spelling of words in the input file against the valid words."""
    try:
        with open(input_file, 'r') as file:
            for line in file:
                # Remove punctuation and split into words
                words = re.findall(r'\b\w+\b', line.lower())
                # Check each word against the dictionary
                for word in words:
                    if word not in valid_words:
                        print(word)  # Print misspelled words
    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' does not exist.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python spell.py <dictionary_file> <input_file>")
    else:
        dictionary_file = sys.argv[1]
        input_file = sys.argv[2]
        valid_words = load_dictionary(dictionary_file)
        check_spelling(input_file, valid_words)
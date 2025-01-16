'''4.	One approach to analysing some encrypted data where a substitution is suspected is frequency analysis.
 A count of the different symbols in the message can be used to identify the language used, and sometimes some of the letters.
   In English, the most common letter is "e", and so the symbol representing "e" should appear most in the encrypted text.
Write a program that processes a string representing a message and reports the six most common letters, along with the number of times they appear. 
Case should not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so best to ignore that initially, and then check the usual resources for the runes.
'''
def frequency_analysis(message):
    # Initialize a dictionary to hold letter counts
    letter_counts = {}

    # Count the occurrences of each letter in the message
    for char in message:
        # Convert to lowercase to ensure case insensitivity
        char = char.lower()
        # Check if the character is a letter
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1  # Increment count if letter already exists
            else:
                letter_counts[char] = 1  # Initialize count if letter is new

    # Sort the letters by their counts in descending order and get the top 6
    most_common_letters = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)[:6]

    # Print the results
    print("The six most common letters are:")
    for letter, count in most_common_letters:
        print(f"Letter: '{letter}', Count: {count}")

def main():
    # Prompt the user to enter a message
    message = input("Enter a message to analyze: ")
    frequency_analysis(message)

if __name__ == "__main__":
    main()
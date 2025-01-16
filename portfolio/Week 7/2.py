'''2.	Write and test three functions that each take two words (strings) as 
parameters and return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what
 topic we have been discussing this week!
 Each function can be exactly one line.
'''
# Function to get letters that appear in at least one of the two words
def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))  
# Function to get letters that appear in both words
def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))  

# Function to get letters that appear in either word, but not in both
def letters_in_either_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))  

# Main function to test the above functions
def main():
    # Prompt user for input
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    # Test the functions
    print("Letters in at least one word:", letters_in_either(word1, word2))  
    print("Letters in both words:", letters_in_both(word1, word2))           
    print("Letters in either word but not in both:", letters_in_either_not_both(word1, word2))  

if __name__ == "__main__":
    main()
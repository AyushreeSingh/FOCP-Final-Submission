'''1. Write and test a function that takes a string as a parameter and 
returns a sorted list of all the unique letters used in the string.
 So, if the string is cheese, the list returned should be
   ['c', 'e', 'h', 's'].'''
def unique_sorted_letters(input_string):
    # Convert the string to a set to get unique letters
    unique_letters = set(input_string)
    # Sort the unique letters and convert back to a list
    sorted_letters = sorted(unique_letters)
    return sorted_letters

# Test the function
test_string = "cheese"
result = unique_sorted_letters(test_string)
print(result)  
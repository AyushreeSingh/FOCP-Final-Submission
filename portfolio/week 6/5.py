''' 5. Another way to hide a message is to include the letters that make it up within
seemingly random text. The letters of the message might be every fi h character,
for example. Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for
clarity the random letters are not random:
send cheese
s  e  n  d   c  h  e  e  s  e
sxyexynxydxy cxyhxyexyexysxye'''

import random
import string

def encrypt_message_with_random_letters(message):
    """Encrypts the message by inserting random letters at a random interval."""
    # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    
    # Initialize the encrypted message
    encrypted_message = []
    
    # Iterate through each character in the message
    for i, char in enumerate(message):
        encrypted_message.append(char)  # Add the original character
        
        # Check if we need to add random letters
        if (i + 1) % interval == 0:
            # Generate a random letter to insert
            random_letter = random.choice(string.ascii_lowercase)
            encrypted_message.append(random_letter)
    
    # Join the list into a single string
    encrypted_message_str = ''.join(encrypted_message)
    
    return encrypted_message_str, interval

if __name__ == "__main__":
    test_message = "send cheese"
    encrypted_message, used_interval = encrypt_message_with_random_letters(test_message)
    
    print(f"Original message: '{test_message}'")
    print(f"Random interval: {used_interval}")
    print(f"Encrypted message: '{encrypted_message}'")

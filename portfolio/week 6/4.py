''' 4.Computers are commonly used in encryption. A very simple form of encryption
more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way.'''

def encrypt_message(message):
    """Encrypts the message by removing spaces and reversing the string."""
    # Remove spaces from the message
    no_spaces = message.replace(" ", "")
    # Reverse the resulting string
    encrypted = no_spaces[::-1]
    return encrypted

if __name__ == "__main__":
    test_message = "mary had a little lamb"
    encrypted_message = encrypt_message(test_message)
    print(f"Original message: '{test_message}'")
    print(f"Encrypted message: '{encrypted_message}'")

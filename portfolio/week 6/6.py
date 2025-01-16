''' 6. Write a program that decrypts messages encoded as above.'''

def decrypt_message(encoded_message, interval):
    """Decrypts the encoded message by extracting characters based on the interval."""
    decrypted_message = []
    
    # Iterate over the encoded message
    for i in range(len(encoded_message)):
        # Check if the character position is within the original message's character positions
        if (i + 1) % interval != 0:
            decrypted_message.append(encoded_message[i])
    
    # Join the list into a single string
    return ''.join(decrypted_message)

if __name__ == "__main__":
    # Example of an encoded message and its interval
    encoded_message = "sendcxeheexs"  # Example encrypted message
    used_interval = 5  # The interval used during encryption
    
    decrypted_message = decrypt_message(encoded_message, used_interval)
    
    print(f"Encoded message: '{encoded_message}'")
    print(f"Used interval: {used_interval}")
    print(f"Decrypted message: '{decrypted_message}'")

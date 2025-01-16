'''3. Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.'''

def password():
    pw1=input("Enter a new password: ")
    if len(pw1)<8 or len(pw1)>12:
        print("Error: Password must be between 8 to 12 characters")
        return pw1
    pw2=input("Please, confirm your password: ")
    if pw1==pw2:
        print("Password set")
    else:
        print("Error: Password doesn't match")

password()
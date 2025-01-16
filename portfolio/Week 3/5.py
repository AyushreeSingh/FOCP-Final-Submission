'''5. Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.'''

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
def password():
    while True:
        pw1=input("Enter a new password: ")
        if pw1 in BAD_PASSWORDS:
            print("Error: Password id too common. Try again")
        if len(pw1)<8 or len(pw1)>12:
                print("Error: Password must be between 8 to 12 characters")
        pw2=input("Please, confirm your password: ")
        if pw1==pw2:
             print("Password set")
        else:
            print("Error: Password doesn't match")
password()
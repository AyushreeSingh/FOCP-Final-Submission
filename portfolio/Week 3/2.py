'''2. Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error.'''
def password():
    pw1=input("Enter a new password: ")
    pw2=input("Please, confirm your password: ")
    if pw1==pw2:
        print("Password set")
    else:
        print("Error: Password doesn't match")

password()
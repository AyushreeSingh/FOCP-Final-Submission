''' 4. When processing data it is o en useful to remove the last character from some
 input (it is o en a newline). Write and test a function that takes a string parameter
 and returns it with the last character removed. (If the string contains one or fewer
 characters, return it unchanged.)'''

def charRem():
 x=input("Enter a name:")
 if len(x)<=1:
  print("WRONG INPUT!")
 else:
  print(x[:-1])
charRem()
 




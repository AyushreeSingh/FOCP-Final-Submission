''' 3. Modify your "greetings" program so that the first letter of the name entered is
 always in uppercase with the rest in lowercase. 
This should happen even if the user entered their name differently. So if the user entered arthur, 
ARTHUR , or even arTHur the name should be displayed as Arthur'''

name = input("Enter your name: ")
newname = ""
for x in range(len(name)):
    if x == 0:
        letter= name[x].upper()  # Capitalize the first letter
    else:
        letter  = name[x].lower()
    newname=newname+letter
      
print(newname)

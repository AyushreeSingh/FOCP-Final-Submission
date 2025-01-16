''' 5. Write and test a function that converts a temperature measured in degrees
 centigrade into the equivalent in fahrenheit, and another that does the reverse
 conversion. Test both functions. (Google will find you the formulae).'''

temp=int(input("Enter the temperature:"))
def tempinFah(b):
    a=(b*9/5)+32
    print("Your Temp in Fahrenheit",b)
def tempinCel(d):
    c=(d-32)*5/9
    print("Your Temp in celsius",d)
check=input("choose b for fahrenheit or choose d for celsius,(b/d)?")
if check.lower()=="a":
   tempinFah(temp)
else:
    tempinCel(temp)



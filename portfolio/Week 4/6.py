''' 6. Write a program that takes a centigrade temperature and displays the equivalent in
 fahrenheit. The input should be a number followed by a letter C. The output should
 be in the same format'''

temp=input("Enter the temperature:")
tem=""
for x in temp: 
    if  x in "C c":
       a=0
    else:
       tem=tem+x
a=float(tem)
f=(a*9/5)+32
print("The temperature in fahrenheit is",f,"F")
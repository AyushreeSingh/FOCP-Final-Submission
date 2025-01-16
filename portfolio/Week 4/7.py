''' 7.  a program that reads 6 temperatures (in the same format as before), and
 displays the maximum, minimum, and mean of the values.
 Hint: You should know there are built-in functions for max and min. If you hunt, you
 might also find one for the mean'''

def tem():
   print("Enter 6 temperatures")
   temperature=[]
   for x in range(6):
     temp=float(input(f"temperatures {x+1}"))
     temperature.append(temp)
   mx=max(temperature)
   mn=min(temperature)
   n=sum(temperature/len(temperature))
   print("the maximum value is",mx)
   print("the minimum value is",mn)
   print("the mean is",n)
tem()


   


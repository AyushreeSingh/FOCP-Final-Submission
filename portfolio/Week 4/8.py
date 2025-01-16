'''  8. Modify the previous program so that it can process any numberof values. The input
 terminates when the user just pressed "Enter" at the prompt rather than entering a
 value'''

def temp():
    temperatures=[]
    ans="Y"
    x=0
    while ans.upper()=="Y":
        temp=float(input("enter temperature : "))
        temperatures.append(temp)
        ans=input("Do you want to continue?(Y/N)")
    mx=max(temperatures)   
    mi=min(temperatures)
    mean=sum(temperatures) / len(temperatures)
    print("maximum temperatures:",mx)
    print("minimum temperatures:",mi)
    print("mean of temperatures:",mean)
temp()

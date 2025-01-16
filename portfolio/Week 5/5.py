''' 5. Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!'''

input_data = input("Enter temperature readings: ")

try:
    temperatures = [float(temp) for temp in input_data.split(',')]
    
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    print(f"Maximum temperature: {max_temp}")
    print(f"Minimum temperature: {min_temp}")
    print(f"Mean temperature: {mean_temp:.2f}")
    
except ValueError:
    print("Please provide valid numeric temperature readings.")

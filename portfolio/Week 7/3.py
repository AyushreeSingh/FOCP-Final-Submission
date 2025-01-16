'''3.	Write a program that manages a list of countries and their capital cities. 
It should prompt the user to enter the name of a country. 
If the program already  "knows" the name of the capital city, it should display it.
 Otherwise it should ask the user to enter it. 
 This should carry on until the user terminates the program (how this happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered variously 
as, for example, "Wales", "wales", "WALES" and so on.
'''


# Dictionary to store countries and their capital cities
countries_capitals = {}

def main():
    while True:
        # Prompt the user to enter a country name
        country = input("Enter the name of a country (or type 'exit' to quit): ").strip().lower()

        # Check if the user wants to exit the program
        if country == 'exit':
            print("Exiting the program.")
            break  

        # Check if the country is already in the dictionary
        if country in countries_capitals:
            
            print(f"The capital of {country.title()} is {countries_capitals[country]}.")
        else:
            # Ask the user to enter the capital city
            capital = input(f"Enter the capital city of {country.title()}: ").strip()
            # Store the country and its capital in the dictionary
            countries_capitals[country] = capital
            print(f"Added: The capital of {country.title()} is {capital}.")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
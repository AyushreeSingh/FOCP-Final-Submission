import random
import json
from datetime import datetime

# Load keywords and responses from a configuration file
def load_responses(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)  # Load and return the JSON data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")  # Handle file not found error
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} contains invalid JSON.")  # Handle JSON decoding error
        return {}

# Randomly choosing an agent name from a predefined list
def get_random_agent():
    agents = ["Santra", "Michael", "Maria", "Gracie", "Rihana"]
    return random.choice(agents)  # Returning a random agent name

# Get a greeting based on the current time of day
def get_time_based_greeting():
    current_hour = datetime.now().hour  # Get the current hour
    if current_hour < 12:
        return "Good morning!"  # Morning greeting
    elif 12 <= current_hour < 18:
        return "Good afternoon!"  # Afternoon greeting
    else:
        return "Good evening!"  # Evening greeting

log_file_path = "chat_log.txt"  # Path to the log file

# Log the conversation between the user and the agent
def log_conversation(user_input, agent_response):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Getting the current timestamp
    with open(log_file_path, "a") as log_file:  # Opening the log file in append mode
        # Writing the user input and agent response to the log file
        log_file.write(f"[{current_time}] User: {user_input}\n[{current_time}] Agent: {agent_response}\n\n")

# Respond to user input based on keywords or randomly
def get_response(user_input, responses, user_name):
    # Normalize user input: strip whitespace and convert to lowercase
    user_words = user_input.strip().lower().split()
    
    # Check for keywords in the user input
    for keyword in responses.keys():
        # If the keyword is found in the user input words
        if keyword.lower() in user_words:
            return responses[keyword][0].format(name=user_name)  # Return the corresponding response

    # Load predefined random responses from a JSON file
    random_responses = load_responses('random_responses.json')
    if random_responses:
        return random.choice(random_responses).format(name=user_name)  # Return a random response
    else:
        return "I'm sorry, I don't have a response for that."  # Default response if no match is found

# Main chat loop
def chat():
    greeting = get_time_based_greeting()  # Get a time-based greeting
    print(greeting)  # Print the greeting
    print("Welcome to the student portal of the University of Poppleton!")  # Welcome message

    user_name = input("What's your name? ")  # Prompt for the user's name
    if not user_name:
        print("Please enter your name to proceed.")  # Ensure the user provides a name
        return

    agent_name = get_random_agent()  # Get a random agent name
    print(f"Welcome {user_name}, I'm {agent_name}. How can I help you today?")  # Introduce the agent

    # Load predefined responses from a JSON file
    responses = load_responses('responses.json')

    while True:
        user_input = input("> ")  # Prompt for user input
        
        if not user_input:
            print("Please ask a question, {name}.".format(name=user_name))  # Prompt for valid input
            continue

        # Check for exit commands
        if user_input.lower() in ["bye", "quit", "exit"]:
            print("Goodbye! Have a great day!")  # Farewell message
            return

        # Get the agent's response based on user input
        agent_response = get_response(user_input, responses, user_name)
        print(agent_response)  # Print the agent's response

        # Log the conversation
        log_conversation(user_input, agent_response)

# Entry point of the program
if __name__ == "__main__":
    chat()  # Start the chat
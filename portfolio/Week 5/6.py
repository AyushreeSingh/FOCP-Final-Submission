''' 6. Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a different name.
Hint: By now, you should be getting the idea that there is a built-in way to do the
heavy li ing here! Take a look at the "Brief Tour of the Standard Library" in the docs.'''

file_name = input("Enter the name of the file you want to back up: ")

try:
    with open(file_name, 'r') as original_file:
        file_contents = original_file.read()

    backup_file_name = file_name.split('.')[0] + "_backup." + file_name.split('.')[1]

    with open(backup_file_name, 'w') as backup_file:
        backup_file.write(file_contents)

    print(f"Backup of {file_name} created as {backup_file_name}")

except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
except Exception as e:
    print(f"Error occurred while creating the backup: {e}")

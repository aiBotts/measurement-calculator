# This program asks a user how he/she wants to calculate
# feet to inches, feet to yards, miles to yards, or miles to feet

# Constants for the Menu Choices
feetToInches = 1
feetToYards = 2
milesToYards = 3
milesToFeet = 4
Exit = 5

# Define the main Function
def main():
    # Display the menu for user.
    display_menu()
    print()
    # Create a  local variable for the menu option.
    value = int(input("Please choose a menu option: "))
    if value == 1:
        # Call feetToInches function.
        feetToInches()
    elif value == 2:
        # Call feetToYards function.
        feetToYards()
    elif value == 3:
        # Call mileToYards function.
        milesToYards()
    elif value == 4:
        # Call milesToFeet function.
        milesToFeet()
        # If the user wants to End application.
    else:
        print('Goodbye.')



# Calculate and display the feet to inches function.
def feetToInches():
    # Create a local variable for feet.
    feet = int(input('Enter the number of feet: '))
    # Calculate how many inches are in a foot
    inches = feet * 12
    print()
    # Display User's answer
    print('There are', inches, 'inches in', feet,'feet')
    # Call the main function again
    main()
    # Return inches to user
    return inches

# Calculate and display feet to yards Function.
def feetToYards():
    # Create a local variable for feet.
    feet = int(input('Enter the number of feet: '))
    # Calculate feet to yards.
    yards = feet / 3
    print()
    # Display User's answer
    print('There are', yards, 'yards in', feet, 'feet')
    # Call the main function again
    main()
    # Return the yards to user
    return yards

# Calculate and display miles to yards Function.
def milesToYards():
    # Create a local variable for miles
    miles = int(input('Enter the number of miles: '))
    # Calculate yards
    yards = miles * 1760
    # Display User's answer
    print('There are', yards,'yards in', miles, 'miles')
    # Call the main function
    main()
    # Return the yards to the user
    return yards

# Calculate and display miles to feet Function.
def milesToFeet():
    # Create a local variable for miles
    miles = int(input('Enter the number of miles: '))
    # Calculate feet
    feet = miles * 5280
    # Display User's answer
    print('There are',feet, 'feet in', miles, 'miles')
    # Call the main function again
    main()
    # Return the feet to the user
    return feet

# Display the Conversion Menu Function
def display_menu():
    print('Conversion Menu:')
    print()
    print('1. Convert feet to inches')
    print('2. Convert feet to yards')
    print('3. Convert miles to yards')
    print('4. Convert miles to feet')
    print('5. Exit')

# Call and execute the main function
main()
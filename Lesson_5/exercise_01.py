'''5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
 Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters
  anything other than a valid number catch it with a try/except and put out an appropriate
   message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.'''

# Initialize variables to store the largest and smallest numbers
largest = None
smallest = None

while True:
    # Prompt the user for input
    user_input = input("Enter an integer number (or 'done' to finish): ")

    # Check if the user wants to finish
    if user_input.lower() == 'done':
        break

    try:
        # Try to convert the input to an integer
        number = int(user_input)

        # Update largest and smallest numbers
        if largest is None or number > largest:
            largest = number
        if smallest is None or number < smallest:
            smallest = number

    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Invalid input")

# After the loop, print the largest and smallest numbers
if largest is not None and smallest is not None:
    print(f"Maximum is {largest}")
    print(f"Minimum is {smallest}")


secret = 7

name = input("What is your name?")
print(f"Hello {name}! I'm thinking of a number between 1 and 10.")

attempt = 1
found = True
while attempt <= 3:
    try:
        guess = int(input(f"Attempt {attempt}, enter your guess: "))

        if guess == secret:
            print(f"🎉 Correct {name}! You got it on attempt {attempt}!")
            found = False
            break
        elif guess > secret:
            print("Too high, try again!")
        else:
            print("Too low, try again!")

        attempt += 1

    except ValueError:
        print(f"Sorry {name}, you didn't enter a number!")

if found:
    print(f"Sorry {name}, the number was {secret}")
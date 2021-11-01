import random


print("Welcome to NumberGuesser!")
print("You have a 5 attempts to guess the right number between 1 and 100.")
print("")

i = 1
status = "0"
number = random.randint(1, 100)


while i <= 4:

    print("What is your guess?")

    guess = int(input("Guess a number: "))

    if number == guess:
        print("")
        print("Congratulations, you win!")
        print("The number was: ", end="")
        print(number)
        status = 1
        break
    else:
        if number < guess:
            print("")
            print("The number is lower than your tip.")
        else:
            print("")
            print("The number is higher than your tip.")

    i += 1


if status == 1:
    pass
else:
    print("")
    print("Nice try, maybe you win next time!")
    print("The number was: ", end="")
    print(number)

from random import randrange

z=1
x=1
y=1

num=randrange(1,101)

print("Welcome to The Perfect Guess Game")
print("You have to guess a number between 1 to 100 which computer has chose randomly")
print("you have 5 tries to guess the number")

while True:
    guess=input("Enter your guess: \n")
    if( guess.isdigit() == False):
        print("Please Enter correct choice number! \n")
        continue
    guess = int(guess)
    if(guess > 100 or guess < 0):
        print("Enter number between 0 and 100! \n")
        continue

    if (guess==num):
        print("Correct!, You've guessed it right")
        z=2
        y=2
        break
    elif (x==5):
        if (guess>num):
            print("Lower number please \n")
        else:
            print("Larger number please \n")
        break
    elif (guess>num):
        print("Lower number please \n")
        x=x+1
    else:
        print("Larger number please \n")
        x=x+1
    
if (z!=2):
    print("Oops!, you're out of tries \n")
    if(num%2==0):
        print("Here's a hint for next 3 tries ")
        print("The number guessed by the computer is even")
    else:
        print("Here's a hint for next 3 tries ")
        print("The number guessed by the computer is odd")

x=1



if (y!=2):
    while True:
        guess=input("Enter your guess: \n")
        if( guess.isdigit() == False):
            print("Please Enter correct choice number! \n")
            continue
        guess = int(guess)
        if(guess > 100 or guess < 0):
            print("Enter number between 0 and 100! \n")
            continue
        if (guess==num):
            print("Correct!, You've guessed it right")
            y=2
            break
        elif (x==3):
            print("Oh no!, Out of tries again")
            print("better luck next time")
            print("The number chosen bye computer was",num,)
            break

        elif (guess>num):
            print("Lower number please \n")
            x=x+1
        else:
            print("Larger number please \n")
            x=x+1   










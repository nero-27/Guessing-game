
import random

n = random.randint(1,100)
print(" you have 5 chances to guess the correct number")
guess = input("guess number between 1 and 100 to start with : ")

c = 5

while c!=0:
    print(f"You have {c} changes left to guess the correct number")
    if int(guess) < n:
        print("your guess is less.") 
        # old_guess = guess
        guess = input(f"guess a number more than {guess} : ")
    elif int(guess) > n:
        print("your guess more")
        # old_guess = guess
        guess = input(f"guess a number less than {guess} : ")
    elif int(guess) == n:
        print(" CONGRATULATIONS!!! You guessed the number!!")
        break
    
    if c-0==1:
        print(f" YOU LOST!! The correct number was : {n}")

    c -= 1








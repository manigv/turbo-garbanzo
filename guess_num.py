#19. Play a number guessing game (User enters a guess, you print YES or Higher or Lower)***
#!/usr/bin/env python
import sys
import random
n = random.randint(1, 99)
guess =int(input("Enter an integer from 1 to 99: "))
while n != "guess":
    
    if guess <=0:
          print("Please enter a valid input.")
          guess = int(input("Enter an integer from 1 to 99: "))
    elif guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("you guessed it!")
        break

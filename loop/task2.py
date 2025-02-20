import random
guess=int(input("enter a number between 1 to 6:"))
random_number=random.randint(1, 6)
if guess== random_number:
 print("congratulations! you guessed it right.")
else:
 print(f"the correct number is {random_number}. better luck next time!")


#  write guess game which generate number from 1 to 6.


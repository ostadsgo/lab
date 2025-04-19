import random


rand_num = random.randrange(1, 100)
print("I am number between 1 - 100 guess me.")
is_win = False

for i in range(10):
    guess = int(input("Guess: "))
    # logic
    if guess > rand_num:
        print("Guess lower.")
    if guess < rand_num:
        print("Guess higher")
    if guess == rand_num:
        print("You win")
        is_win = True
        break


if is_win == False:
    print("You lose.")
     


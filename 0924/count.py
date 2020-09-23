import random

answer = random.randint(1, 10)
count = 0

while True:
    guess = int(input("plz guess number(1~10)"))
    count += 1

    if answer == guess:
        print(" %i guesses" %count)
        break
    elif answer > guess:
        print("bigger")
    else:
        print("smaller")
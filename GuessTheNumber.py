import random

n = random.randrange(1, 101)
print("I've though a number between 1 and 100!")

while True:
    try:
        g = input('Guess! : ')
        g = int(g)
        if not (0 < g < 100):
            print("It's between a and 100")
    except ValueError:
        print("Enter an integer : ")
        continue

    if g == n:
        print("Congartualtions!!")

    if g < n:
        print("Larger")

    if g > n:
        print("Smaller")
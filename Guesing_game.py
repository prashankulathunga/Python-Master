import random

jack_pot = random.randint(1, 100)

guess_number = int(input("Please Enter a Number: "))
count = 0

while jack_pot != guess_number:
    if jack_pot < guess_number:
        print("Wrong! Please guess lower")
    else:
        print("Wrong! PLease guess higher")

    guess_number = int(input("Please Enter a Number: "))
    count += 1
else:
    print("Yeah! You win the game")
    print(f"Your attempt is {count}")

for i in range(1, 12):
    print(i)

for i in range(1, 3):
    print("Hello I am second python loop", i)

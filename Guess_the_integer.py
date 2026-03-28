from random import randint

gen = randint(0, 50)

print("Guess number between 0 to 50")

for i in range(5):
    try:
        guess = int(input("Enter guess: "))
    except:
        print("Invalid input")
        continue

    if guess == gen:
        print("🎉 Correct!")
        break
    elif guess < gen:
        print("Go higher")
    else:
        print("Go lower")

else:
    print("❌ You lost. Number was:", gen)
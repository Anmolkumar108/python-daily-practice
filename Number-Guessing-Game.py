import random

secret_number = random.randint(1, 20)

print("================================")
print("     NUMBER GUESSING GAME")
print("================================")
print("I have selected a number between 1 and 20.")
print("You have 3 chances.")

guess1 = int(input("Enter your first guess: "))

if guess1 == secret_number:
    print("🎉 You Win!")
elif guess1 < secret_number:
    print("Too Low!")
else:
    print("Too High!")


if guess1 != secret_number:

    guess2 = int(input("Enter your second guess: "))

    if guess2 == secret_number:
        print("🎉 You Win!")
    elif guess2 < secret_number:
        print("Too Low!")
    else:
        print("Too High!")


if guess1 != secret_number and guess2 != secret_number:

    guess3 = int(input("Enter your third guess: "))

    if guess3 == secret_number:
        print("🎉 You Win!")
    else:
        print("❌ Game Over!")
        print("Correct Number Was:", secret_number)
print("=" * 50)
print("🎉 WELCOME TO KAUN BANEGA CROREPATI 🎉")
print("=" * 50)

name = input("ENTER YOUR NAME: ")
print(f"\nWelcome {name}! Let's Start The Game.\n")

questions = [
    [
        "1. What Is The Capital Of India?",
        "A. Mumbai",
        "B. Delhi",
        "C. Patna",
        "D. Kolkata",
        "B",
        1000
    ],
    [
        "2. Which language is used for AI and Data Science?",
        "A. HTML",
        "B. Python",
        "C. JavaScript",
        "D. CSS",
        "B",
        5000
    ],
    [
        "3. Who developed Python?",
        "A. Dennis Ritchie",
        "B. James Gosling",
        "C. Guido van Rossum",
        "D. Elon Musk",
        "C",
        10000
    ],
    [
        "4. Which keyword is used to create a function in Python?",
        "A. function",
        "B. def",
        "C. fun",
        "D. define",
        "B",
        50000
    ],
    [
        "5. What is the extension of Python file?",
        "A. .java",
        "B. .cpp",
        "C. .py",
        "D. .html",
        "C",
        100000
    ]
]

money = 0

for i, q in enumerate(questions):

    print("\n" + "=" * 50)
    print(q[0])
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])

    answer = input("\nEnter Your Answer (A/B/C/D): ").upper()

    if answer == q[5]:
        money = q[6]

        print("\n✅ Correct Answer!")
        print(f"🎉 You won ₹{money}")

       
        if i == len(questions) - 1:
            print("\n🏆 Congratulations!")
            print("You answered all questions correctly.")
            break

        choice = input("\nDo you want to play the next question? (Y/N): ").upper()

        if choice == "N":
            print("\n😊 You decided to quit the game.")
            break

        print("\n⚠️ WARNING!")
        print("If your next answer is WRONG,")
        print("you will lose ALL your winning amount!")

        confirm = input("Still want to continue? (Y/N): ").upper()

        if confirm == "N":
            print("\n😊 You decided to quit the game.")
            break

    else:
        print("\n❌ Wrong Answer!")
        print(f"Correct Answer: {q[5]}")

        print("\n💸 You lost all your winning amount!")
        money = 0
        break

print("\n" + "=" * 50)
print(f"Game Over, {name}")
print(f"🏆 Total Winning Amount: ₹{money}")
print("=" * 50)
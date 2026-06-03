import random

words = ["python", "java", "coding", "laptop", "science"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6

print("Hangman Game Started!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if "_" not in guessed:
    print("You won! Word is:", word)
else:
    print("You lost! Word was:", word)
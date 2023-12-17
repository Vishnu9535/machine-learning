import random
words = ["pencil", "hangman", "wrong", "code", "pen"]
word = random.choice(words)
word = word.lower()
display_word = ["_"] * len(word)
max_attempts = 6
attempts = 0
guessed_letters = []
while True:
    print(" ".join(display_word))
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
             if word[i] == guess:
                display_word[i] = guess
    else:
        attempts += 1
        print(f"Wrong guess! You have {max_attempts - attempts} attemp")
    if "".join(display_word) == word:
        print("Congratulations, you've guessed the word: " + word)
        break
    if attempts >= max_attempts:
        print("You've run out of attempts. The word was: " + word)
        break
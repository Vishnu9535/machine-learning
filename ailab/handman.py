word = "vishnu"
guess_word = "_"*len(word)
print(guess_word)
def disply():
    print(guess_word)
disply()
attempts = 6
def guess(word):
        letter = str(input("guess the letter ")).lower().strip()
        if letter in word:
            print(word.replace(letter,"_"))

guess(word)


        



import random

secret_words = ["school", "pencil", "lunch", "rubber", "board"]
random_index = random.randint(0, 4)
secret_words[random_index]

word = secret_words[random_index]
blanks = list("_" * len(word))
wrong_guess = 0

while wrong_guess < 6:
    player_guess = input("Guess the letter using the prompt:")

    if player_guess not in word:
        print("Guess right letter")
        wrong_guess += 1

    for index, letter in enumerate(word):
        if player_guess == letter:
            blanks[index] = player_guess

    print(blanks)
    if "_" not in blanks:
        print("You Won!")
        break
    if wrong_guess==6 and "_" in blanks:
        print("You lost and the word is :", word)

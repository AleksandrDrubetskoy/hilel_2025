word_input = input("Enter the word with 'h' or 'H': ")
while word_input.count('h') < 1 and word_input.count('H') < 1:
    print("The word is invalid. Enter word with 'h' or 'H'")
    word_input = input()
else:
    print(f"The word {word_input} is valid")

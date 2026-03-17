while True:
    word = input("Enter a word with letter h included")
    if "h" in word or "H" in word:
        print("The word is correct:", word)
        break
    else:
        print("The word is incorrect, please enter word with 'h'or 'H':", word)
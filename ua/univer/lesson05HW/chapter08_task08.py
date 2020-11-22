def main():
    sentence = input('Enter sentence: ')
    sentence = sentence.split()
    for word in sentence:
        word = word.upper()
        print(word)
    print(sentence)


main()

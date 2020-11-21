def main():
    number: str = input('Enter some integer number in on string without space: ')
    count = 0
    for symbol in number:
        count += int(symbol)
    print(count)


main()

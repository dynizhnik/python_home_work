def main():
    phone = input('Enter phone number on XXX-XXX-XXXX format ')
    phone = phone.upper()
    number_phone = ''
    PHONE = {
        'A': '2', 'B': '2', 'C': '2', '2': '2',
        'D': '3', 'E': '3', 'F': '3', '3': '3',
        'G': '4', 'H': '4', 'I': '4', '4': '4',
        'J': '5', 'K': '5', 'L': '5', '5': '5',
        'M': '6', 'N': '6', 'O': '6', '6': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7', '7': '7',
        'T': '8', 'U': '8', 'V': '8', '8': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9', '9': '9',
        '-': '-'
    }
    for cont in phone:
        number_phone += PHONE[cont]
    print(number_phone)
main()

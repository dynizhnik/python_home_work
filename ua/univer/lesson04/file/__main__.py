if __name__ == '__main__':
    with open("data.txt", 'a') as file_data:
        file_data.write('11,12,13,14,15,16')

    with open("data.txt", 'a') as file_data:
        print('\n11,12,13,14,15,16', file=file_data)
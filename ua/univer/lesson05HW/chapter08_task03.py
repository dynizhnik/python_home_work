def main():
    date_string = input('Enter date in dd/mm/yyyy format: ')
    date_list = date_string.split('/')
    if int(date_list[1]) == 1:
        month = 'January'
    elif int(date_list[1]) == 2:
        month = 'February'
    elif int(date_list[1]) == 3:
        month = 'March'
    elif int(date_list[1]) == 4:
        month = 'April'
    elif int(date_list[1]) == 5:
        month = 'May'
    elif int(date_list[1]) == 6:
        month = 'June'
    elif int(date_list[1]) == 7:
        month = 'July'
    elif int(date_list[1]) == 8:
        month = 'August'
    elif int(date_list[1]) == 9:
        month = 'September'
    elif int(date_list[1]) == 10:
        month = 'October'
    elif int(date_list[1]) == 11:
        month = 'November'
    elif int(date_list[1]) == 12:
        month = 'December'
    print(date_list[0], month, date_list[2], 'y.')


main()

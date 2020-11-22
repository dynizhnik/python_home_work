def main():
    CLASSROOM = {
        'CS101': '3004',
        'CS102': '4501',
        'CS103': '6755',
        'CS104': '1244',
        'CS105': '1411'
    }
    #    print(CLASSROOM)

    TEACHER = {
        'CS101': 'Haince',
        'CS102': 'Alvadore',
        'CS103': 'Rich',
        'CS104': 'Berk',
        'CS105': 'Li'
    }
    #    print(TEACHER)

    TIME = {
        'CS101': '8:00',
        'CS102': '9:00',
        'CS103': '10:00',
        'CS104': '11:00',
        'CS105': '13:00'
    }
    #    print(TIME)

    key = input('Enter number of course: ')
    print('For this', key, 'course:',
          'classroom is:', CLASSROOM[key],
          'teacher is:', TEACHER[key],
          'and time is:', TIME[key]
          )


main()

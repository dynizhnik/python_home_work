from ua.univer.lesson06HW.chapter10_task04_Employee import Employee


def main():
    employee1 = Employee('Suzan Maier', 47899, 'Accountant', 'Vice-President')
    employee2 = Employee('Mark Djouns', 39119, 'IT', 'Programmer')
    employee3 = Employee('Djoi Rodjers', 81774, 'Industrial', 'Engineer')

    print(employee1.get_name(), employee1.get_id_num(), employee1.get_department(), employee1.get_position())
    print(employee2.get_name(), employee2.get_id_num(), employee2.get_department(), employee2.get_position())
    print(employee3.get_name(), employee3.get_id_num(), employee3.get_department(), employee3.get_position())


main()

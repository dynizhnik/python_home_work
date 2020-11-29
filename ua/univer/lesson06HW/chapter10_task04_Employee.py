class Employee:
    def __init__(self, name, id_num, department, position):
        self.__name = name
        self.__id_num = id_num
        self.__department = department
        self.__position = position

    def set_name(self, name):
        self.__name = name

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def set_department(self, department):
        self.__department = department

    def set_position(self, position):
        self.__position = position

    def get_name(self):
        return self.__name

    def get_id_num(self):
        return self.__id_num

    def get_department(self):
        return self.__department

    def get_position(self):
        return self.__position
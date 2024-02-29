class People:

    def __init__(self, name, login, password):
        self.__name = name
        self.__login = login
        self.__password = password

    def consult_name(self):
        return self.__name

class Student(People):

    def __init__(self, name, login, password, course):
        People.__init__(self, name, login, password)
        self.__course = course

    def consult_course(self):
        return self.__course

class Teacher:
    def __init__(self, name, login, password, title):
        People.__init__(self, name, login, password)
        self.__title = title

    def consult_title(self):
        return self.__title

people1 = People('Gustavo', 'gustavo1234', 'g1u2s3')
print(people1.consult_name())

student1 = Student('Jhon', 'jhon1234', 'j1h2o3', 'Software Engineer')
print(student1.consult_name())
print(student1.consult_course())

class OnlineCourse:
    def __init__(self, course_name, students=[]):
        self.__course_name = course_name
        self.__students = students

    def add_student(self, name):
        self.__students.append(name)
        print(self.__students)

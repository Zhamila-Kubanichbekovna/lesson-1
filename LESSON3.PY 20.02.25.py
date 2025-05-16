# '''
# Инкапсуляция позволяет скрывать внутренние данные объекта и управлятьих доступом через методы.
# В Python используются приватные (__private_attr) и защищённые (_protected_attr) атрибуты.
# '''
# class BankAccount:
#     def __init__(self, owner, balance, account_type):
#         self.owner = owner         # Публичный атрибут
#         self.__balance = balance   # Приватный атрибут (нельзя изменить извне)
#         self._account_type = account_type  # Защищённый атрибут (можно изменить извне)

#     # добавьте метод deposit, который добавляет сумму к приватному атрибуту __balance
#     def deposit(self, amount):
#         self.__balance += amount
#         return self.__balance

#     def get_balance(self):
#         return self.__balance  # метод для доступа к приватному атрибуту


# bank_account = BankAccount('Дока', 200, 'saving')  # создаём объект класса BankAccount
# print(bank_account.owner)  # можно обратиться к публичному атрибуту
# print(bank_account.get_balance())  # можно обратиться к приватному атрибуту через метод
# print(bank_account._account_type)  # можно обратиться к защищённому атрибуту
# print(bank_account.deposit(10000000000))
# print(bank_account.get_balance())  # можно обратиться к приватному атрибуту через метод
# print(bank_account.__balance)  # нельзя обратиться к приватному атрибуту


'''
Наследование позволяет создать базовый класс и передавать его свойства и методы дочерним классам.
Это позволяет избежать дублирования кода.
'''

# # Определение базового класса Animal, представляющего общее животное
# class Animal:
#     # Метод-конструктор, инициализирующий имя и вид животного
#     def __init__(self, name, species):
#         self.name = name          # сохраняем имя животного
#         self.species = species    # сохраняем вид животного

#     # Метод make_sound, который по умолчанию ничего не выводит (переопределяется в наследниках)
#     def make_sound(self):
#         print('ничего')           # базовая реализация звука животного

# # Класс Dog наследуется от Animal и представляет конкретный тип животного — собаку
# class Dog(Animal):

#     # Конструктор класса Dog, который принимает дополнительные данные - породу
#     def __init__(self, name, species, breed):
#         # Вызов конструктора базового класса Animal для установки name и species
#         super().__init__(name, species)
#         self.breed = breed       # сохраняем породу собаки

#     # Переопределение метода make_sound: собака издаёт звук "гав"
#     def make_sound(self):
#         print('гав')

# # Класс Cat наследуется от Animal и представляет конкретный тип животного — кошку
# class Cat(Animal):

#     # В данном случае конструктор не переопределён, поэтому используется конструктор Animal
#     # Переопределяем метод make_sound: кошка издаёт звук "мяу"
#     def make_sound(self):
#         print('мяу')

# # Создание экземпляра класса Dog с конкретными параметрами: имя, вид и порода
# dog = Dog('рекс', 'собачьи', 'лабрадор')
# # Создание экземпляра класса Cat с конкретными параметрами: имя и вид (порода не указана)
# cat = Cat('корниш рекс', 'кошачьи')
# # Выводим имя, вид и породу собаки
# print(dog.name, dog.species, dog.breed)
# # Собака издаёт звук: "гав"
# dog.make_sound()
# # Выводим имя и вид кошки
# print(cat.name, cat.species)
# # Кошка издаёт звук: "мяу"
# cat.make_sound()


'''
Полиморфизм позволяет объектам разного типа использовать один и тот же метод, но с разным поведением.
'''


class OnlineCourse:
    def __init__(self, course_name, students=[]):
        self.__course_name = course_name
        self.__students = students

    def add_student(self, name):
        self.__students.append(name)
        print(self.__students)


course = OnlineCourse('python')
course.add_student('hnhuniu')
course.add_student('jnjnj')
'''
🔥 Практические задания по 3 столпам ООП (Инкапсуляция, Наследование, Полиморфизм)

🏛 1. Инкапсуляция – Управление данными в Онлайн-Курсе

Задание:

Создайте класс OnlineCourse, который управляет информацией о курсе. Защитите внутренние данные, чтобы их нельзя было изменить напрямую.

📌 Что нужно сделать:
 1. Атрибуты:
 • __course_name (приватный) – название курса.
 • __students (приватный) – список студентов (по умолчанию пустой).
 2. Методы:
 • add_student(name): добавляет студента в курс.
 • remove_student(name): удаляет студента (если он есть).
 • get_students(): возвращает список студентов.
 • get_course_name(): возвращает название курса.

✅ Пример использования:
course = OnlineCourse("Python для начинающих")

course.add_student("Алексей")
course.add_student("Мария")

print(course.get_students())  # ["Алексей", "Мария"]

course.remove_student("Алексей")
print(course.get_students())  # ["Мария"]

print(course.get_course_name())  # "Python для начинающих"

# Ошибка: нельзя менять название курса напрямую
# course.__course_name = "Новый курс" ❌ AttributeError🎯 Дополнительное задание:
 • Добавьте проверку, чтобы один и тот же студент не мог быть добавлен дважды.
 '''

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def get_fullname(self):
        return self.name.capitalize() + ' ' + self.surname.capitalize()


person = Person(name='anar', surname='veliyev')
person1 = Person(name='koroglu', surname='mirzeyev')
print(person.get_fullname())
print(person1.get_fullname())


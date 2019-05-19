class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list_of_known_persons = {}

    def known(self, person):
        self.list_of_known_persons[person.name] = person.age

    def is_known(self, person):
        if person.name in self.list_of_known_persons:
            return True
        else:
            return False

Ivan = Person('Ivan',31)
Sergey = Person('Sergey',32)
John = Person('John',33)
Tom = Person('Tom',34)
Piter = Person('Piter',35)
Anton = Person('Anton',36)
Barny = Person('Barny',37)

Ivan.known(Sergey)
Ivan.known(Anton)
John.known(Tom)
John.known(Piter)
Barny.known(Ivan)

print("Ivan known: ",Ivan.list_of_known_persons,"\n")
print("John known: ",John.list_of_known_persons,"\n")
print("Barny known: ",Barny.list_of_known_persons,"\n")

print("Check {}'s relationship with {} : {} \n ".format(Ivan.name, Sergey.name, Ivan.is_known(Sergey)))
print("Check {}'s relationship with {} : {} \n ".format(John.name, Tom.name, John.is_known(Tom)))
print("Check {}'s relationship with {} : {} \n ".format(Ivan.name, John.name, Ivan.is_known(John)))
print("Check {}'s relationship with {} : {} \n ".format(Barny.name, Ivan.name, Barny.is_known(Ivan)))
print("Check {}'s relationship with {} : {} \n ".format(Barny.name, John.name, Barny.is_known(John)))
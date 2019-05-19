class Animal(object):

    def __init__(self, animal_type):
        self.animal_type = animal_type

class Human(object):
    dangerous_type = ['poisonous', 'predator']

    def is_dangerous(self, animal):
        return animal.animal_type.lower() in self.dangerous_type

Cobra = Animal('poisonous')
Tiger = Animal('predator')
Rabbit = Animal('herbivorous')

Man = Human()

print("Is {} animal dangerous for human? : {}".format(Cobra.animal_type, Man.is_dangerous(Cobra)))
print("Is {} animal dangerous for human? : {}".format(Tiger.animal_type, Man.is_dangerous(Tiger)))
print("Is {} animal dangerous for human? : {}".format(Rabbit.animal_type, Man.is_dangerous(Rabbit)))
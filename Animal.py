#Creating the Parent

class animal:
    numOfanimals = 0

    def __init__(self, species, name, animal_id, birth_date, color, sex, weight, zoo_from):
        self.species = species
        self.name = name
        self.animal = animal_id
        self.birth_date = birth_date
        self.color = color
        self.sex = sex
        self.weight = weight
        self.zoo_from = zoo_from

        animal.numOfanimals += 1




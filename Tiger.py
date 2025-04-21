#Creating the Tiger names

from Animal import animal

class tiger(animal):
    numOftigers = 0

    list_of_tiger_names = []

    file_path = r"animalNames.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
        group_of_names = lines[2].strip().split("\n")
        names = group_of_names[0].strip().split(",")
        list_of_tiger_names.extend(names)

    def __init__(self, name ="a_name", animal_id = "an_id", birth_date ="", color ="a_color", sex = "a_sex", weight = "a_weight", zoo_from = "a_zoo", arrival_date = ""):

        tiger.numOftigers += 1

        super().__init__("tiger", name, animal_id, birth_date, color, sex, weight, zoo_from)

    def get_tiger_name(self):
        return self.list_of_tiger_names.pop(0)

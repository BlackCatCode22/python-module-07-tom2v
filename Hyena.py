#Creating Hyena names

from Animal import animal

class hyena(animal):
    numOfhyenas = 0

    list_of_hyena_names = []

    file_path = r"animalNames.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
        group_of_names = lines[0].strip().split("\n")
        names = group_of_names[0].strip().split(",")
        list_of_hyena_names.extend(names)

    def __init__(self, name = "a_name", animal_id = "an_id", birth_date ="", color ="a_color", sex = "a_sex", weight = "a_weight", zoo_from = "a_zoo", date_arrival = "2099-01-01"):

        hyena.numOfhyenas += 1

        super().__init__("hyena", name, animal_id, birth_date, color, sex, weight, zoo_from)

    def get_hyena_name(self):
        return self.list_of_hyena_names.pop(0)





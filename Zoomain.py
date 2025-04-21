#Tong's Midterm Project Zoo Animals

#import strip
#import Birthday
from Animal import animal
from Hyena import hyena
from Lion import lion
from Tiger import tiger
from Bear import bear

from _datetime import date

#Create Data base of spicies
list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []

#Birthday generating variable
current_date = date.today()
current_year = current_date.year

#Birthday generation
def cal_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)

    the_birth_day = ""

    if "spring" in the_season:
        the_birth_day = str(year_of_birthday) + "-03-02"
    elif "summer" in the_season:
         the_birth_day = str(year_of_birthday) + "-06-03"
    elif "winter" in the_season:
        the_birth_day = str(year_of_birthday) + "-12-21"
    else:
        the_birth_day = str(year_of_birthday) + "-09-15"

    return the_birth_day

# Read arrivingAnimals List
def process_one_line(one_line):

     group_of_words = one_line.strip().split(",")
     single_words = group_of_words[0].strip().split(" ")
     age_in_years = single_words[0]
     a_sex = single_words[3]
     a_species = single_words[4]
     single_words = group_of_words[1].strip().split(" ")
     season = single_words[2]
     color = group_of_words[2].strip();
     weight = group_of_words[3].strip();
     origin_01 = group_of_words[4].strip();
     origin_02 = group_of_words[5].strip();
     zoo_from = origin_01 + "," + origin_02
     birth_day = cal_birth_date(season, age_in_years)

#Creating the animals
     if "hyena" in a_species:
        #Creat hyena
        my_hyena = hyena("aName","anID", birth_day, color, a_sex, weight, zoo_from, current_date)
        #Create name & id
        my_hyena.name = hyena.get_hyena_name(my_hyena)
        my_hyena.animal_id = "Hy" + str(hyena.numOfhyenas).zfill(2)
        #Add to Data base
        list_of_hyenas.append(my_hyena)

     if "lion" in a_species:
         my_lion = lion("aName","anID", birth_day, color, a_sex, weight, zoo_from, current_date)
         my_lion.name = lion.get_lion_name(my_lion)
         my_lion.animal_id = "Li" + str(lion.numOflions).zfill(2)
         list_of_lions.append(my_lion)

     if "tiger" in a_species:
        my_tiger = tiger("aName","anID", birth_day, color, a_sex, weight, zoo_from, current_date)
        my_tiger.name = tiger.get_tiger_name(my_tiger)
        my_tiger.animal_id = "Li" + str(tiger.numOftigers).zfill(2)
        list_of_tigers.append(my_tiger)

     if "bear" in a_species:
        my_bear = bear("aName","anID", birth_day, color, a_sex, weight, zoo_from, current_date)
        my_bear.name = bear.get_bear_name(my_bear)
        my_bear.animal_id = "Li" + str(bear.numOfbears).zfill(2)
        list_of_bears.append(my_bear)

file_path = r"arrivingAnimals.txt"
with open(file_path,"r") as file:
     for line in file:
         process_one_line(line)

#Creating the Zoo Population report
print()
print("****** Zoo Population And Habitat Report ******")
print(f"Number of Animals: {animal.numOfanimals}")
print()
print("Hyena Habitat:")
print(f"Number of Hyenas: {hyena.numOfhyenas}")
for hyena in list_of_hyenas:
    print((hyena.animal_id) + ", " + hyena.name + "; birthdate: " + str(
        hyena.birth_date) + "; " + str(hyena.color) + "; sex: " + str(
        hyena.sex) + "; weight: " + str(hyena.weight) + "; arrived: " + str(current_date))

print()
print("Lion Habitat:")
print(f"Number of Lions: {lion.numOflions}")
for lion in list_of_lions:
    print((lion.animal_id) + ", " + lion.name + "; birthdate: " + str(
        lion.birth_date) + "; " + str(lion.color) + "; sex: " + str(
        lion.sex) + "; weight: " + str(lion.weight) + "; arrived: " + str(current_date))

print()
print("Tiger Habitat:")
print(f"Number of Tigers: {tiger.numOftigers}")
for tiger in list_of_tigers:
    print((tiger.animal_id) + ", " + tiger.name + "; birthdate: " + str(
        tiger.birth_date) + "; " +  str(tiger.color) + "; sex: " + str(
        tiger.sex) + "; weight: " + str(tiger.weight) + "; arrived: " + str(current_date))

print()
print("Bear Habitat:")
print(f"Number of Bears: {bear.numOfbears}")
for bear in list_of_bears:
    print((bear.animal_id) + ", " + bear.name + "; birthdate: " + str(
        bear.birth_date) + "; " + str(bear.color) + "; sex: " + str(
        bear.sex) + "; weight: " + str(bear.weight) + "; arrived: " + str(current_date))


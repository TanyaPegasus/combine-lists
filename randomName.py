from mainFunctions import *
import random

names_location = "lastNames.txt"

names_list = create_list_from_file(names_location)

name = random.choice(names_list)

print(name)
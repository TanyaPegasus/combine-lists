from mainFunctions import create_list_from_file, get_random_name

first_file_location = "firstNames.txt"
first_names_list = create_list_from_file(first_file_location)
last_file_location = "lastNames.txt"
last_names_list = create_list_from_file(last_file_location)

random_name = get_random_name(first_names_list)
print(random_name.capitalize())


"""
letter = "A"

# type for letter?
def name_from_letter(letter, my_list):
    new_list = []
    for name in first_list:
        if name.start
            new_list.append(name)
    letter_list = []
    return

# Ask for user input
# Use regex to find only names that start with that letter
    # list comprehension, names = [for blah in blah if]
# output a random name
# need something for if they put tmore than one letter or something that is not a letter
"""
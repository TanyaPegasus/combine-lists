import random

def create_list_from_file(filename):
    with open(filename) as file:
        create_list = [line.strip() for line in file]
    return create_list

def capitalise_names(my_list):
    uppercase_list = [name.upper() for name in my_list]
    return uppercase_list

def remove_duplicates(my_list):
    no_duplicates = set(my_list)
    list_format = list(no_duplicates)
    return list_format

def alphabetise_list(my_list):
    my_list.sort()
    return my_list

def final_formatting(my_list):
    uppercase_list = capitalise_names(my_list)
    no_duplicates = remove_duplicates(uppercase_list)
    alphabetised = alphabetise_list(no_duplicates)
    return alphabetised

def join_two_lists(list_1, list_2):
    existing_names = create_list_from_file(list_1)
    new_names = create_list_from_file(list_2)
    modified_list = existing_names + new_names
    formatted = final_formatting(modified_list)
    return formatted

def save_final_list(final_list, filename):
    with open(filename, "w") as file:
        for name in final_list:
            file.write(name + "\n")
    return

#Optional extra functions for curiosity. Only above needed for main purpose:

# Was used to find which names were only in firstnames.txt, or only in lastnames.txt
def find_unique_words(list_1, list_2):
    first_list = create_list_from_file(list_1)
    second_list = create_list_from_file(list_2)
    words_only_in_first_list = set(first_list) - set(second_list)
    return list(words_only_in_first_list)
    # note to self. I remember there was a reason I had to use set here and not list. Don't remember it. Look it up.

# another function for curiosity. It was telling me which names were already present in both first names and last names.
def find_duplicates(list_1, list_2):
    first_list = create_list_from_file(list_1)
    second_list = create_list_from_file(list_2)
    new_list = []
    for name in first_list:
        if name in second_list:
            new_list.append(name)
    return new_list

def get_random_name(names_list):
    name = random.choice(names_list)
    return name
def create_list_from_file(filename):
    with open(filename) as file:
        create_list = [line.strip() for line in file]
    return create_list

def prepare_list(filename_or_list_location):
    if type(filename_or_list_location) == list:
        new_list = filename_or_list_location
    else:
        new_list = create_list_from_file(filename_or_list_location)
    return new_list

def capitalise_names(my_list):
    uppercase_list = [name.upper() for name in my_list]
    return uppercase_list

def remove_duplicates(my_list):
    no_duplicates = set(my_list)
    final_list = list(no_duplicates)
    return final_list

def alphabetise_list(my_list):
    my_list.sort()
    return my_list

def final_formatting(my_list):
    uppercase_list = capitalise_names(my_list)
    no_duplicates = remove_duplicates(uppercase_list)
    alphabetised = alphabetise_list(no_duplicates)
    return alphabetised

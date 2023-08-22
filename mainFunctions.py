def create_list_from_file(filename):
    with open(filename) as file:
        create_list = [line.strip() for line in file]
    return create_list

def determine_input_type(fileOrList):
    if type(fileOrList) == list:
        new_list = fileOrList
    else:
        new_list = create_list_from_file(fileOrList)
    return new_list

def capitalise_names(createdlist):
    uppercase_list = [name.upper() for name in createdlist]
    return uppercase_list

def remove_duplicates(list1):
    no_duplicates = set(list1)
    final_list = list(no_duplicates)
    return final_list

def alphabetise_list(mylist):
    mylist.sort()
    return mylist

def final_formatting(variationonlist):
    uppercase_list = capitalise_names(variationonlist)
    no_duplicates = remove_duplicates(uppercase_list)
    alphabetised = alphabetise_list(no_duplicates)
    return alphabetised

from mainFunctions import *

def join_two_lists(list_1, list_2):
    current_list = prepare_list(list_1)
    list_to_add = prepare_list(list_2)
    modified_list = current_list + list_to_add
    formatted = final_formatting(modified_list)
    return formatted

# function from Mig
def save_final_list(final_list, filename):
    list_file_str = "\n".join(final_list)
    with open(filename, "w") as file:
        file.write(list_file_str)
    return True

"""def save_final_list(final_list, filename): 
    with open(filename, "w") as file:
        for index_number, name in enumerate(final_list):
            if index_number == len(final_list) -1:
                file.write(name)
            else:
                file.write(name + "\n")
    return"""
    # "filename" creates file if it doesn't exist, or overwrites if it does

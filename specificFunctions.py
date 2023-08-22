from mainFunctions import *

def join_two_lists(input1, input2):
    current_list = determine_input_type(input1)
    list_to_add = determine_input_type(input2)
    modified_list = current_list + list_to_add
    formatted = final_formatting(modified_list)
    return formatted

def save_final_list(final_list, filename): 
    with open(filename, "w") as file:
        for index_number, name in enumerate(final_list):
            if index_number == len(final_list) -1:
                file.write(name)
            else:
                file.write(name + "\n")
    return
    # "filename" creates file if it doesn't exist, or overwrites if it does

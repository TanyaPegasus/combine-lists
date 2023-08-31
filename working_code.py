from specificFunctions import *

# inputs:
file_location_1 = "testList1.txt"
file_location_2 = "addedNames.txt"
input_as_list = ["apple", "banana"]
save_location = "newFile.txt"


ready = join_two_lists(list_1= file_location_1, list_2= file_location_2)
save_final_list(final_list= ready, filename= save_location)


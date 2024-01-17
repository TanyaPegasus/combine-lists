from mainFunctions import *

first_file_location = "firstNames.txt"
last_file_location = "lastNames.txt"
added_file_location = "supporterNames.txt" 

ready_firstnames = join_two_lists(list_1= first_file_location, list_2= added_file_location)
save_final_list(final_list= ready_firstnames, filename= first_file_location)

ready_lastnames = join_two_lists(list_1= last_file_location, list_2= added_file_location)
save_final_list(final_list= ready_lastnames, filename= last_file_location)

# To use, ensure firstnames.txt and lastnames.txt are the latest version from onelife. Add requested names to supporterNames.tex and run. 
# Replace the onelife name files with the updated files from here.
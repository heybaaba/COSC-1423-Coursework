# sorting the list of locations for the dat in order
def organize_mappings(mappings):
    for date in mappings:
        mappings[date].sort()

# printing each date and sorted locations in the format way
def organized_print(mappings):
    for date in mappings:
        print(f"{date} : {mappings[date]}", end = "\n")

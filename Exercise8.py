
def item_finder(target_value, source_list):
    for element in source_list:        
        if element == target_value:    
            return True
    return False

name_box = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_key = "Sam"

print("List of names available:", name_box)
print("Searching for:", search_key)

found_status = item_finder(search_key, name_box)

if found_status:
    print("Result: The name was found inside the list.")
else:
    print("Result: The name does NOT exist in the list.")

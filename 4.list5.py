# Ways to check if an element exists in a list
def check_element_exists(lst, element):
    return element in lst

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
search_element = int(input("Enter the element to check for existence: "))
element_exists = check_element_exists(my_list, search_element)
print(f"The element {search_element} {'exists' if element_exists else 'does not exist'} in the list.")

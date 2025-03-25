def display_recursively(elements):
    if not elements: 
        print("The list is empty.")
        return
    print(elements) 
    return

user_input = input("Enter elements separated by spaces: ")
lst = user_input.split()  

if lst:
    print("The elements in the list are:")
    display_recursively(lst)  
else:
    print("The list is empty.")


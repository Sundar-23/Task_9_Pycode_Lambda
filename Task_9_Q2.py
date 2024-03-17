#Question-2

check_list = [5, 'DELL', 66, 'MICROSOFT', '29']

#check int or string using lamda function
check_elements = lambda lst: all(isinstance(item, (int, str)) for item in lst)

result = check_elements(check_list)

# print typr of elements in the list
if result:
    print("Every element in the list is an integer or string.")
else:
    print("The list contains elements that are not integers or strings.")
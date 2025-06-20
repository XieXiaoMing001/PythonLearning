#基本列表推导式
numbers = [1, 2, 3, 4, 5, 6]
new_number = [x * 2 for x in numbers]
print(new_number)

#带有条件的列表推导式
new_number1 = [x * 2 for x in numbers if x % 2 == 0]
print(new_number1)

#多变量列表推导式
list1 = [1, 2, 3]
list2 = [4, 5, 6]

new_list = [x + y for x, y in zip(list1, list2)]
print(new_list)

#嵌套列表推导式
original_list = [1, 2, 3]
nested_list = [[x ** 2, x ** 3] for x in original_list]
print(nested_list)
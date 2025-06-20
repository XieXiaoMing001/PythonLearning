#练习算数运算符
a = 30
b = 4
print('a 加 b = ', a + b)
print('a 减 b = ', a - b)
print('a 乘 b = ', a * b)
print('a 除 b = ', a / b)
print('a 整除 b = ', a // b)
print('a 取余 b = ', a % b)
print('a 指数运算 b = ', a ** b)

# 练习比较运算符
c = 10
d = 20
print('c 等于 d = ', c == d)
print('c 不等于 d = ', c != d)
print('c 大于 d = ', c > d)
print('c 小于 d = ', c < d)
print('c 大于等于 d = ', c >= d)
print('c 小于等于 d = ', c <= d)

# 练习逻辑运算符
e = True
f = False
print('非e = ', not e)
print('e and f = ', e and f)
print('e or f = ', e or f)

# 练习赋值运算符
g = 10
g += 3
print('g += ', g)#g = 13
g -= 3
print('g -= ',g)#g = 10
g *= 3
print('g *= ',g)#g = 30
g /= 3
print('g /= ',g)#g = 10.0
g %= 4
print('g %= ',g)#g = 2.0
g **= 3
print('g **= ',g)#g = 8.0
g //= 5
print('g //= ',g)#g = 1.0

# 练习成员运算符
my_list = [1, 2, 3, 4, 5]
print('3 in my_list = ',3 in my_list)
my_tuple = (1, 2, 3, 4, 5)
print('4 in my_tuple = ',4 in my_tuple)
my_string = 'hello friend'
print('e in my_string = ','e' in my_string)
my_dict = {'a' : 1, 'b' : 2}
print('a in my_dict','a' in my_dict)
my_set = {1, 2, 3}
print('1 in my_set = ', 1 in my_set)

#练习身份运算符
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
print(arr1 == arr2)#true
print(arr1 is arr2)#false
arr3 = arr1
print(arr1 is arr3)#true


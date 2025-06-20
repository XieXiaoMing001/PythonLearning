#列表
my_list = ['a', 'b', 'c', 'd', 'e']

#访问列表元素
print('访问第一个元素：', my_list[0])
print('访问最后一个元素：', my_list[-1])

#修改列表元素
my_list[0] = '哈'
print(my_list)

#切片是获取列表的一部分元素的一种方式
print('获取前三个元素=', my_list[:3])
print('获取第二个元素到倒倒数第二个元素', my_list[1:-1])
print('获取所有元素，步长是二', my_list[::2])

#在列表末尾添加元素
my_list.append('f')
print(my_list)

#移除列表中第一个匹配到的元素
my_list.remove('f')
print(my_list)

#列表中进行排序
my_list.sort()
print(my_list)

#将列表中的元素顺序颠倒
my_list.reverse()
print(my_list)

#返回列表中第一个匹配元素的索引
print(my_list.index('c'))

my_list.append('f')
print(my_list.count('f'))
my_list.append('f')
print(my_list.count('f'))
print(my_list)

#将一个列表的所有元素添加到另一个列表的末尾
my_list.extend(['a', 2, 6])
print(my_list)

#在指定位置插入一个元素
my_list.insert(1, 'b2')
print(my_list)

#移除列表中的一个元素（默认是最后一个），并返回该元素
element = my_list.pop()
print(element)
print(my_list)

#清空列表中的所有元素
my_list.clear()
print(my_list)


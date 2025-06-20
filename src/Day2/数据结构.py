#List数据结构
first_list = [1, 2, 3, 4]#创建列表
print('访问列表中的元素', first_list[0])
print('访问列表中最后一个元素', first_list[-1])

#修改列表元素
first_list[0] = '哈哈哈'
print('修改列表中的第一个元素', first_list)

#切片获取列表大的一部分元素
print('获取列表中的第一个元素', first_list[0])
print('获取列表中的前两个元素', first_list[0: 2])
print('获取列表中的所有元素，步长为2', first_list[::2])


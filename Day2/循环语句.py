# for循环
#遍历列表
names = ['孙悟空', '唐三藏', '猪八戒', '沙悟净']
for name in names:
    print(name)

#遍历字符串
string = 'Hello'
for string1 in string:
    print(string1)

#遍历字典
a = {'a': 1, 'b': 2, 'c': 3}
for b in a:
    print(b)

#循环变量
for i in range(2):
    print(i)


# while循环
count = 14
while count <15:
    print(count)
    count += 1

#break关键字的使用
for i in range(1,10):
    if i == 6:
        break
    print(i)

#continue关键字的使用
for count in range(1,6):
    if count == 3:
        continue
    print(count)
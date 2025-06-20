a = 20
b = a + 1.2
print(type(a), ' = ', a)
print(type(b), ' = ', b)

#练习强制类型转换
c = 10
d = 10.5
print(int(d))
print(float(c))
print(abs(d))
print(pow(c,2))
print(round(10.5))
e = True
f = False
print(int(e),int(f))

g = 'Hello, World'
print('索引 = ', g[0])
print('切片 = ', g[0:6])
print('连接 = ', g + '!')
print('重复 = ', g * 3)
print('长度 = ', len(g))
print('大小写转换 = ', g.upper())
print('大小写转换 = ', g.lower())
print('查找 = ', g.find('llo'))
print('替换 = ', g.replace('llo', 'aaa'))
print('去除空白 = ', g.strip())


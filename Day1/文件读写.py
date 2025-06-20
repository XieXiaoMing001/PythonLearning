with open('/Users/fanle-xiaoming/Downloads/随机使用==========================/a.txt', 'w') as file:
    file.write("Hello, World!")

with open('/Users/fanle-xiaoming/Downloads/随机使用==========================/a.txt', 'a') as file:
    file.write("\n'这是我第一次向一个文件中写入内容呦")

with open('/Users/fanle-xiaoming/Downloads/随机使用==========================/a.txt', 'r') as file:
    content = file.read()
    print(content)

with open('/Users/fanle-xiaoming/Downloads/随机使用==========================/b.txt', 'wb') as file:
    file.write(b"Hello, World!")
    print('file = ', file)

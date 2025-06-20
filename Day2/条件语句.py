x = 10
if x > 1:
    print('x大于1')


if x < 1:
    print('x小于1')
else:
    print('x大于1')

if x in [0, 1, 2, 3, 4, 5]:
    print('x属于0-5中的数')
elif x in [6, 7, 8, 9, 10]:
    print('x属于6-10中的数字')
    for i in [6, 7, 8, 9,10]:
        if x == i:
            print(i)

else:
    print('x不属于1-10中的数字')
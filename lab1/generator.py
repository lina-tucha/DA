import random

string = "abcdefghijklmnopqrstuvwxyzabcdef" * 2
l = len(string)
f = open('test.txt', 'w')
f.write('')
f.close()

for i in range(2000000):
    x = random.randint(0, 2 ** 64 - 1)
    sint = random.randint(1, l)
    sint = int(l / sint)
    s = ''
    for j in range(0, l, sint):
        s += string[j]
    f = open('test.txt', 'a')
    f.write(str(x) + ' ' + s + '\n')
    f.close()
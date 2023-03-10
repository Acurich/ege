обычный 
def f(x, y):
    if x > y :
        return 0
    if x == y:
        return 1
    else:
        return f(x + 2, y) + f(x + 3, y) + f(x + 6, y)
print(f(11, 23))

траектория содержит
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 3, y) + f(x * 2, y)
print(f(3, 12) * f(12, 16))

траектория не содержит 
def f(x, y):
    if x > y or x == 10:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 2 , y) + f(x * 3, y)
print(f(1,14))

содержит и не содердит
def f(x, y): 
    if x > y or x == 14:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 2, y)
print(f(3, 12) * f(12, 21))

2 содержит
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 4, y) + f(x * 2, y)
print(f(4, 12) * f(12, 17) * f(17, 20))


от большего к меньшему + содержит
def f(n, target):
    if n == target:
        return 1
    elif n < target:
        return 0
    else:
        return f(n-1, target) + f(n//2, target)

print(f(23, 9)*f(9,2))

содержит ровно
def f(x, y):
    if x > y or x == 12:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 2, y)
 
def f1(x, y):
    if x > y or x == 13:
        return 0
    if x == y:
        return 1
    else:
        return f1(x + 1, y) + f1(x + 2, y)
print(f(3, 13) * f(13, 18) + f1(3, 12) * f1(12, 18))

команды
from itertools import product
s = set()
for command in product('12', repeat=4):
    n=2
    for i in range(len(command)):
        if command[i]=='1':
            n=n*3
        if command[i]=='2':
            n=n*3+1
        if command[i]=='3':
          n = n*3+2
    s.add(n)
print(len(s))

двоичка
№105
for n in range(1, 100):
    s = bin(n)[2:]
    s = str(s)
    if n % 2 == 0:
        s += "00"
    else:
        s += "11"
    r = int(s, 2)
    if r > 50:
        print(n)
        break

№106
for n in range(1, 100):
    s = bin(n)[2:] 
    s = str(s)
    if s.count('1') % 2 == 0: 
        s += '1'
    else:
        s += '0'
    s += str(s.count('1') % 2)
    r = int(s, 2)
    if r > 44:
        print(r)
        break

№107
def f(s):
    summa = 0
    for i in range(len(s)):
        summa += int(s[i])
    return summa
for n in range(1, 1000):
    s = bin(8*n)[2:]
    s = str(s)
    s = s + str(f(s) % 2)
    s = s + str(f(s) % 2)
    r = int(s, 2)
    if r > 2214:
        print(n)
        break

№111
for n in range(1, 10000):
    s = bin(n)[2:] 
    s = str(s)
    s = s[:-1]
    if n % 2 != 0:
        s += "10"
    else:
        s += "01"
    r = int(s, 2) 
    if r == 230:
        print(n)

№113
for n in range(136, 1, -1):
    s = bin(n)[2:]  
    s = str(s)
    s = s[::-1]
    s = s[s.find('1'):]
    r = int(s, 2)  
    if r == 17:
        print(n)
        break

№114
for n in range(1, 100):
    s = bin(n)[2:]
    s = str(s)
    s = s[s.find('1'):]
    if s.count('1') > s.count('0'):
        s += '1'
    else:
        s += '0'
    r = int(s, 2) 
    if r > 71:
        print(r)
        break
№115
mn = -1
for n in range(1,1000):
  r = bin(n)[2:]
  r = r.replace('0', '00')
  r = r.replace('1', '11')
  r = int(r,2)
  if r < 17 and r > mn:
    mn = r
print(mn)
№116
mn = -1
for n in range(1,1000):
  r = bin(n)[2:]
  v = ''
  for c in r:
    if c == '0':
      v += '01'
    else:
      v += '10'
  r = v
  r = int(r,2)
  if r < 49 and r > mn:
    mn = r
print(mn)

№110
for n in range(0, 256):
    s = bin(n)[2:]
    s = str(s)
    if len(s) < 8:
        s = '0' * (8 - len(s)) + s
    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', '0')
    r = int(s, 2)
    if r - n == 185:
        print(n)
№112
a = []
for x in range(240, 1501):
    i = int(bin(x)[3:], 2)
    if x - i not in a:
        a.append(x-i)
print(len(a))

№117
mx = 0
for n in range(1,10000):
  r = bin(n)[2:]
  if n % 4 == 0: r += '00'
  elif n % 4 == 1: r += '01'
  elif n % 4 == 2: r += '10'
  else: r += '11'
  r = int(r,2)
  if r < 54 and r > mx:
    mx = r
print(mx)
    
№120
for n in range(2,1000):
  r = bin(n)[2:]
  r +=r[-2]
  r += r[1]
  r = int(r,2)
  if r > 76 :
    print(n)
    break
    
№123
k = 0
for n in range(2,1000):
  r = n
  if r % 2 ==0:
    r = r // 2
  else:
    r = r - 1
  if r % 3 == 0:
    r = r // 3
  else: 
    r = r - 1
  if r % 5 ==0:
    r = r // 5
  else:
    r = r -1
  if r == 4 :
    k += 1
print(k)

№119
for n in range(2, 100): 
    s = bin(n)[2:] 
    s = str(s)
    s += s[1] + s[0]
    r = int(s, 2) 
    if r < 120:
        print(n)
        break
#121
for n in range(4, 100):
    s = bin(n)[2:] 
    s = str(s)
    s = s[0:len(s)-1]
    s += s[1] * 2
    r = int(s, 2)
    if r > 66:
        print(n)
        break
#122
for n in range(52, 1000):
    s = bin(n)[2:]
    s = str(s)
    for i in range(3):
        if s.count("1") == s.count("0"):
            s += s[-1]
        elif s.count("1") > s.count("0"):
            s += "0"
        else:
            s += "1"
    r = int(s, 2)
    if r % 4 == 0:
        print(n)
        break
        
#124.1
def f(s):
    summa = 0
    for i in range(len(s)):
        summa += int(s[i])
    return summa
for n in range(1, 100):
    n = n - (n % 4)
    s = bin(n)[2:] 
    s = str(s)
    summa = f(s)
    s = s + str(summa % 2)
    summa = f(s)
    s = s + str(summa % 2)
    r = int(s, 2) 
    if r <126:
        print(r)
        
#124.2
def f(s):
    summa = 0
    for i in range(len(s)):
        summa += int(s[i])
    return summa
for n in range(1, 100):
    s = bin(n)[2:] 
    s = str(s)
    summa = f(s)
    s = s + str(summa % 2)
    summa = f(s)
    s = s + str(summa % 2)
    r = int(s, 2) 
    if r > 110:
        print(r)
        break
#118
for n in range(1, 10):
  a = bin(n)[2:]
  if n % 2 == 0:
    a += '0' * len(a)
  else:
    a += '1' * len(a)
  if 34 < int(a, 2):
    print(int(a, 2))
    break

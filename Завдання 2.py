from math import factorial
from math import sin
n = float(input('кількість елеметів'))
b = float(input('число b'))
A = []
C = []
a = 0
i = 1
while n >= i:
    a = a + factorial(i) * sin(i * b)
    A.append(a)
    i += 1
i = 1
while n > i:
    a = A[i-1] * A[i]
    C.append(a)
    i += 1
print(min(C))
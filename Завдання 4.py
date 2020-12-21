n = int(input("Введіть кількість елементів масиву: "))
k = [float(input("{0}-ий елемент: ".format(i+1))) for i in range(n)]
n = len(k)
print("Ваш масив:",k)
g = []
gg = []
i = 0
while n > i:
    b = k[i]
    i += 1
    if b == 0:
        g+= [0]
        continue
    gg += [b]
print(g+gg)
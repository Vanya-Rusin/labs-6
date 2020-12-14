n = int(input("Введіть кількість елементів масиву: "))
k = [float(input("{0}-ий елемент: ".format(i+1))) for i in range(n)]

print("Ваш масив:",k)
g = []
for i in range(n):
   if k[i] == 0:
    g.insert(0, k[i])
   del(k[i])
g.append(k[i])

print(g)
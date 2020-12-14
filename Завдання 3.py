n = int(input("Вкажіть вимір вектора: "))

x = [float(input("Задайте {0}-координату вектора x{0}: ".format(i + 1))) for i in range(n)]
y = [float(input("Задайте {0}-координату вектора y{0}: ".format(i + 1))) for i in range(n)]
print("\nVektor x= {0}\nVektor y= {1}" .format(x, y))
a=[]
z=1
for i in range(n):
    a.append(x[i]/y[i])
print(a)
for i in range(n-1):
    if a[i]!=a[i+1]:
        z=0
        break
if z==False:
    print("непаралельні")
else:
    print("паралельні")



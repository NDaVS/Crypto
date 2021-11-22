import random
n = int(input('Введите нечётное число > 3 для проверки => '))
k = int(input('Введите количество итераций для проверки => '))
s = 0
bl = True
check = True
t = (n-1)
mas=[]
while True:
    if (2 ** s) * t == (n-1) and (t % 2 != 0):
        break
    t = t / 2
    s += 1
for i in range(1, k+1):
    a = random.randint(2, 15)
    x = (a ** t) % n
    if (x == 1) or (x == n-1) and bl:
        mas.append("Простое")
        bl = False
    for j in range(s):
        x = (x ** 2) % n
        if x == 1:
            mas.append("Составное")

            bl = False
            break
        if x == n - 1:
            mas.append("Простое")
            bl = False
            break

if 'Простое' in mas:
    print("Простое")
else:
    print("Составное")
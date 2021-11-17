import random, math

masE = []
masD = []
d=0

p = 5
q = 37

n = p * q # Modul
proverka = True
fE = (p - 1) * (q - 1)
m=0

try:
    m = int(input(f"Введите число меньше {fE} => "))

except:
    proverka = False

if proverka and (m < 144):


    for a in range(2, fE):
        if math.gcd(a, fE) == 1:
            masE.append(a)

    e = masE[0]

    #print("e - "+ str(e))

    for i in range(150):
        if e*i%fE==1:
            masD.append(i)

    # def inv(x, m): #Второй вариант
    #     u = (x, 1)
    #     v = (m, 0)
    #     while v[0] != 0:
    #         q = u[0] // v[0]
    #         t = (u[0] % v[0], u[1] - q * v[1])
    #         u = v
    #         v = t
    #     if u[0] != 1: return 0
    #     return u[1] % m
    # print(masD)
    #d=inv(e,fE)
    def gcd_extended(num1, num2):
        if num1 == 0:
            return (num2, 0, 1)
        else:
            div, x, y = gcd_extended(num2 % num1, num1)
        return (div, y - (num2 // num1) * x, x)
    masD = gcd_extended(e, fE)

    d=masD[1]
    #print("d - " +str(d))

    publicKey = (n, e)
    privateKey = (n, d)

    Ctext = (m ** publicKey[1])%publicKey[0]
    print(f'Шифротекст - {Ctext}')

    Text = (Ctext ** privateKey[1])%privateKey[0]
    print(f'Исходное сообщение - {Text}')

    print(f'Открытый ключ - {publicKey}')
    print(f'Закрытый ключ - {privateKey}')
else:
    print("Ошибка ввода.")
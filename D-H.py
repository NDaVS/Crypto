import random
prov = True
try:
    g = int(input('Введите значение g => '))
    p = int(input('Введите значение p => '))
except:
    prov = False
    print("Ошибка ввода.")
if prov:
    openKey = (g, p)
    userA = [random.randint(1000, 10000), 0, 0] # y|x, k_1|K_2, privateKey_1|privateKey_2
    userB = [random.randint(1000, 10000), 0, 0]

    userA[1] = (openKey[0] ** userA[0]) % openKey[1]
    userB[1] = (openKey[0] ** userB[0]) % openKey[1]

    # Произошла передача k_1 и k_2

    arrKey = [userB[1], userA[1]]

    if ((arrKey[0] ** userA[0]) % openKey[1]) == ((arrKey[1] ** userB[0]) % openKey[1]):
        print("Общий ключ = "+str((arrKey[0] ** userA[0]) % openKey[1]))
    key = (arrKey[0] ** userA[0]) % openKey[1]
    m = 15
    chText = m ** key
    print(chText)
    text = chText ** (1/key)
    print(text)
else:
    pass
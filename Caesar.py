import string
abc = string.ascii_lowercase

print('''Шифр Цезаря.
Используйте только СТРОЧНЫЕ (lowercase) БУКВЫ АНГЛИЙСКОГО АЛФОВИТА БЕЗ ПРОБЕЛОВ''')

while True:

    proverka = True
    proverkaChisla = True

    k=0
    m = input('Введите сообщение (/stop чтобы остановить) => ')

    if m == '/stop':
        break

    for i in range(len(m)):

        if not(m[i] in abc):
            proverka = False

    try:
        k = int(input('Введите смещение (Натуральное число) => '))
    except:
        proverka = False

    if proverka:

        chText=''
        text=''

        for i in range(len(m)):
            chText += abc[(abc.index(m[i]) + k) % 26]
        print('Шифротекст => ' + chText)

        for i in range(len(chText)):
            text += abc[(abc.index(chText[i]) - k + 26) % 26]
        print('Исходный текст => ' + text)
    else:
        print('Ну я же просил соблюдать условия...')
    print('='*30)
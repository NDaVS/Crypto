import string
abc = string.ascii_lowercase

print('''Шифр Виженера.
Используйте только СТРОЧНЫЕ (lowercase) БУКВЫ АНГЛИЙСКОГО АЛФОВИТА БЕЗ ПРОБЕЛОВ''') # предостережение

while True:
    proverka = True # Проверить введёные сообщения
    k=0 # ключ
    n=0 # Счётчик для ключа

    m = input('Введите сообщение (/stop чтобы остановить) => ')

    if m == '/stop':
        break

    for i in range(len(m)):# Проверка на правильность введёных данных
        if not(m[i] in abc):
            proverka = False

    k = input('Введите ключ => ')
    for i in range(len(k)):
        if not(m[i] in abc):
            proverka = False

    if proverka:

        chText=''
        text=''

        for i in range(len(m)):#Шифрование
            if n == len(k):
                n = 0

            chText += abc[(abc.index(m[i]) + abc.index(k[n])) % 26]
            n += 1

        print('Шифротекст => ' + chText)
        n = 0

        for i in range(len(chText)):#Расифрование
            if n == len(k):
                n = 0

            text += abc[(abc.index(chText[i]) - abc.index(k[n]) + 26) % 26]
            n+=1

        print('Исходный текст => ' + text)

    else:
        print('Ну я же просил соблюдать условия...')

    print('='*30)
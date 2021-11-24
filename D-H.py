import random
# from check_alg.miller_rabin import *


def p_start():
    while True:
        p = random.randint(1000, 10000)
        a = random.randint(2, p-1)
        if miller_r(p,a):
            return p
def g_start(p):
    fi_p = p -1
    for g in range(3,250):
        a = random.randint(2, p - 1)
        if miller_r(g, a) and (g ** fi_p) % p == 1:
            return g

def key(g, p):
    openKey = (g, p)
    return openKey

def users(openKey):
    userA = [random.randint(1000, 10000), 0, 0] # y|x, k_1|K_2, privateKey_1|privateKey_2
    userB = [random.randint(1000, 10000), 0, 0]

    userA[1] = (openKey[0] ** userA[0]) % openKey[1]
    userB[1] = (openKey[0] ** userB[0]) % openKey[1]

# Произошла передача k_1 и k_2

    arrKey = [userB[1], userA[1]]

    if ((arrKey[0] ** userA[0]) % openKey[1]) == ((arrKey[1] ** userB[0]) % openKey[1]):
        print("Общий ключ = "+str((arrKey[0] ** userA[0]) % openKey[1]))
    global_key = (arrKey[0] ** userA[0]) % openKey[1]
    return global_key

def chText(m, key):
    chText = m ** key
    print(chText)
    text = chText ** (1 / key)
    print(text)

def single_test(n, a):
    exp = n - 1
    while not exp & 1:
        exp >>= 1
    if pow(a, exp, n) ==1:
        return True
    while exp < n-1:
        if pow(a, exp, n) == n -1:
            return True
        exp <<= 1
    return False

def miller_r(n, a,  k = 40):
    for i in range(k):

        if not single_test(n, a):
            return False
    return True


if __name__ == '__main__':
    p = p_start()
    g = g_start(p)

    open_key = key(g, p)
    global_key = users(open_key)

    m = int(input("Input a number"))

    chText(m, global_key)


def fatorial(n):
    f = 1
    while n > 1:
        f = f * n
        n = n - 1
        return f

def fatorial1(k):
    fat = 1
    while k > 1:
        fat = fat * k
        k = k - 1
        return k

def fatorial2(u):
    u = fatorial1(n) - fatorial2(k)
    fato = 1
    if u == 0:
        u = 1
    else:
        if u == 1:
            u = 1
        else:
            while u > 1:
                fato = fato * u
                u = u - 1
                return u

def numero_binomial (n, k):
    return fatorial1(n) / fatorial2(k) * fatorial3(u)

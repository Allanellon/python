n = int(input("Digite um número inteiro: "))
m = 0

while n != 0:
    m = m + (n % 10)
    n = n // 10

print(m)

n = int(input("Digite um número inteiro: "))

d_i = False
u_d = n % 10
n_n = n // 10
d_a = 0 

while n_n > 0 and d_i == False:
    d_a = n_n % 10
    if u_d == d_a:
        d_i = True
    else:
        u_d = d_a
        n_n = n_n // 10

if d_i:
    print("sim")
else:
    print("não") 
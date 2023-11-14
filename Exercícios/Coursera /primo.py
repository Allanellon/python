n = int(input("Digite um número inteiro: "))
i = 2
primo = True
if n == 1:
    primo = False
else:
    if n == 2:
        primo = True
    else:
        while i < n:
            if n % i == 0:
                primo = False
                break
            else:
                i = i + 1

if primo == True:
    print("primo")

else: 
    print("não primo")

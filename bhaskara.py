import math

a = float(input("Digite o valor de a: "))
b= float(input("Digite o valor de b: "))
c= float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c 

if delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    print("a raiz desta equação é {}" .format(x1))

else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        if x1 < x2:
            print("as raízes da equação são",x1,"e",x2)
        else:
            print("as raízes da equação são",x2,"e",x1)
import math

x = int(input("Digite uma coordenada: "))
y = int(input("Digite outra coordenada: "))
x1 = int(input("Digite mais uma coordenada: "))
y1 = int(input("Digite a ultima coordenada: "))

d = math.sqrt((x - x1)**2 + (y - y1)**2)

if d >= 10:
    print("longe")

else:
    print("perto")

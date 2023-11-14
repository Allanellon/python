segundos= int(input("Por favor, entre com o número de segundos que deseja converter: "))
a = segundos // 86400
segundoss = segundos % 86400
b = segundoss // 3600
segundosss = segundoss % 3600
c = segundosss // 60
d = segundosss % 60
print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")
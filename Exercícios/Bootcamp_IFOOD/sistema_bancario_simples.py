menu = """
	Bem vindo ao serviço de atendimento bancário virtual! Escolha abaixo uma
	das opções:
	
	[1] Sacar
	[2] Depositar
	[3] Extrato
	[4] Sair

	=> """

saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

	opcao = int(input(menu))

	if opcao == 1:
		if numero_saques < LIMITE_SAQUES:
			print(f"Você tem R$ {saldo} de saldo")
			saque = float(input("Quanto você deseja sacar: "))
			
			if saque > saldo:
				print(f"Você não possui saldo suficiente! O seu saldo é de {saldo}")

			elif saque > limite:
				print(f"O seu limite por saque é de R$ {limite}")

			elif saque <= limite and saque > 0 and saque < saldo:
				saldo -= saque
				numero_saques += 1
				extrato += f"\n [1] Saque R$ {saque: .2f}"
				print(f"Saque concluido! O seu novo saldo é de {saldo}")

			elif saque < 0:
				print("Operação invalida!")

		elif numero_saques >= LIMITE_SAQUES:
			print("Você ultrapassou o seu limite de saque!")

	elif opcao == 2:
		deposito = float(input("Qual o valor que você deseja depositar: "))
		if deposito > 0:
			saldo += deposito
			extrato += f"\n [2] Deposito {deposito: .2f}"
			print(f"Deposito concluido com sucesso! O seu novo saldo é de {saldo}")
		elif deposito <=0:
			print("Operação invalida!")

	elif opcao == 3:
		print("========== EXTRATO ==========")

		print("Não foram realizadas movimentações" if not extrato else extrato)
		print(f"Saldo R$ {saldo: .2f}")

		print("=============================")

	elif opcao == 4:
		print("Obrigado pela preferência!")
		break

	else:
		print("Operação invalida, por favor selecione novamente a operação desejada.")

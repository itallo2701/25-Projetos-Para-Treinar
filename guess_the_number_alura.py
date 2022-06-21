import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

tdt = input("Qual Nivel você quer ?\nFacil = Digite F\nMedio = Digite M\nDificil = Digite D\nQual sua escolha :  ").lower()


if tdt == 'f':
	total_de_tentativas = 10
	x = 20
	secret_number = random.randint(1,x)
	
	
elif tdt == 'm':
	total_de_tentativas = 5
	x = 50
	secret_number = random.randint(1,x)
	
	
elif tdt == 'd':
	total_de_tentativas = 3
	x = 100
	secret_number = random.randint(1,x)


while total_de_tentativas > 0 :
	print(f"Total de tentativas disponiveis : {total_de_tentativas}")
	chute = input(f"Digite o numero que você acha que é o numero secreto, lembrando que o valor é de 1 a {x}: ")


	if int(chute) == secret_number:
		print(f"Você acertou o numero parabens, o numero é {secret_number}")
		total_de_tentativas -= total_de_tentativas
		
		
	else:
		
		
		if int(chute) > secret_number:
			total_de_tentativas -= 1 
			print("Você errou! O seu chute foi maior do que o número secreto")
			
			
		elif int(chute) < secret_number:
			total_de_tentativas -= 1
			print("Você errou! O seu chute foi menor do que o número secreto")
	
	print(f"O numero secreto era : {secret_number}")
	
	

print("Fim do Jogo")



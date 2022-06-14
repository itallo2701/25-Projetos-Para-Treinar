import random

def guess(x):
	random_number = random.randint(1,x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Adivinhe um numero entre 1 e {x}: '))
		if guess < random_number:
			print("Tente Novamente. Muito Baixo.")
		elif guess > random_number:
			print("Tente Novamente. Muito Alto")
	
	print(f"Parabens, você acertou o numero.")
	
guess(200)

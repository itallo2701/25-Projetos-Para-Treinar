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
	
	
def computer_guess(x):
	low = 1 
	high = x 
	feedback = ''
	while feedback != 'c' and low != high:
		if low != high:
			guess = random.randint(low,high)
		else:
			guess = low #could also be high b/c low = high
		feedback = input(f"is {guess} too high (H), too low(L), or correct(C)?? ").lower()
		if feedback == 'h':
			high = guess - 1 
		elif feedback == 'l':
			low = guess + 1
	print(f"The computer guessed the number, {guess}, congratulations!")
		
	

computer_guess(100)

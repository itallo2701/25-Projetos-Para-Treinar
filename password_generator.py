import random
import string

print("*********************************")
print("Bem vindo ao Gerador de Senhas !!!")
print("*********************************")

def generate_passwords(number,length):
	print("\nAqui esta sua(s) senha(s) :")
	for pwd in range(number):
		passwords = ''
		for c in range(length):
			passwords += random.choice(chars)
		print(passwords)

#letras, numeros e pontuações que fazem parte da senha 
chars = string.ascii_letters + string.digits + string.punctuation

#Quantas Senhas vão ser geradas 
number = input("Quantas senhas você quer gerar ? ")
number = int(number)

#Quantas caracteres a senha vai ter  
length = input("Quantos caracteres deseja na sua senha ? ")
length = int(length)

#Chamada da função
generate_passwords(number,length)

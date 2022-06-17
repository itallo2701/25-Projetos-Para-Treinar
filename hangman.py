import random
import string

from words import words

#Verifica se a palavra não contem Hifen ou espaço em branco
def get_valid_word(words):
	#Escolhemos com Choice do modulo Random
	word = random.choice(words)
	#Usamos um laço while para verificar se possui hifen ou espaço em branco
	while '-' in word or ' ' in word:
		#Se possuir ele ira Usar Choice novamente pra escolehr outra palavra
		word = random.choice(words)
	return word.upper()

#O jogo em si
def hangman():
	#A chamada da função para verificar as palavras
	word = get_valid_word(words)
	#Aqui pegamos as letras da palavra
	word_letters = set(word)
	#Aqui temos as letras do alfabeto maiusculo pela chamada do modulo String
	alphabet = set(string.ascii_uppercase)
	#Aqui deixamos um conjunto vazio para as letras que iremos usar
	used_letters = set() 
	
	#Quantidade de vidas que temos disponiveis, fiz para que a pessoa consiga escolher a quantidade.
	ask = input("how many lives do you want to have? ")
	lives = int(ask)
	
	#Um laço while para que o jogo continue executando ate você acertar todas as letras ou sua vida chegar a 0
	while len(word_letters) > 0 and lives > 0:
		#Imprimimos as informações de vidas e as letras ja usadas toda vez que tem a passagem do loop
		print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))
		
		#Ele pega as letras que não adivinharam ainda e deixa ela 
		#mostrando apenas um traço, caso você acerte ele troca os traços por letra
		word_list = [letter if letter in used_letters else '-' for letter in word]
		print("Current word: ", " ".join(word_list))
		
		#Para a pessao colocar a letra que ela quer chutar
		user_letter = input("guess a letter:").upper()
		#Caso essa letra esteja no (alfabeto - as letras usadas) ele ira adicionar user_letter a used_letters
		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			#Aqui verificamos se a letra esta na palavra da forca e caso esteja removemos ela
			if user_letter in word_letters:
				word_letters.remove(user_letter)
			#Caso não esteja perdemos 1 vida 	
			else:
				lives = lives - 1
				print("letter is not in word.")
		#Caso ja tenhamos usado esse caractere ele ira verificar e imprimir uma mensagem
		#falando que ja usamos esse caractere
		elif user_letter in used_letters:
			print("You have already used that character. Please try again")
		#Caso o caractere seja infalido ele isa imprimir uma mensagem	
		else:
			print("Invalid character. Please try again")
	#Aqui temos o fim do jogo, caso você perca todas as vidas ou caso tenha acertado
	if lives == 0:
		print("You died, sorry. The word was", word)
	else:
		print("You guessed the word", word, "!!")
		
#chamada do jogo.		
hangman()

from random import choice


def pedra_papel_tesoura():
	itens = ['pedra','papel','tesoura']
	flag = True
	while flag:
		if flag:
			pc = choice(itens)
		else:
			break
		feedback = input("Escolha : \n p = pedra\n a = papel \n t = tesoura\n sua escolha : ")
		
			#pedra
		if feedback == 'p' and pc == 'pedra':
			print(f"Empate ambos escolheram {pc}\n")
		elif feedback == 'p' and pc =='papel':
			print(f"Você perdeu o computador escolheu {pc}\n")
		elif feedback == 'p' and pc =='tesoura':
			print(f"Você ganhou o computador escolheu {pc}\n")
			
			#papel
		elif feedback == 'a' and pc =='papel':
			print(f"Empate ambos escolheram {pc}\n")
		elif feedback == 'a' and pc =='tesoura':
			print(f"Você perdeu o computador escolheu {pc}\n")
		elif feedback == 'a' and pc =='pedra':
			print(f"Você ganhou o computador escolheu {pc}\n")
			
			#tesoura
		elif feedback == 't' and pc =='papel':
			print(f"Você ganhou o computador escolheu {pc}\n")
		elif feedback == 't' and pc =='tesoura':
			print(f"Empate ambos escolheram {pc}\n")
		elif feedback == 't' and pc =='pedra':
			print(f"Você perdeu o computador escolheu {pc}\n")

pedra_papel_tesoura()

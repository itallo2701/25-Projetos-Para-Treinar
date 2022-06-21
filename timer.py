import time 
from playsound import playsound



def timer(t):
	while t:
		time.sleep(t*60)
		playsound("alert.mp3")
		break
	print("Timer Acabou")


def countdown(t):
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins,secs)
		print(timer, end='\r')
		time.sleep(1)
		t -= 1 
	playsound("alert.mp3")
	print("Contagem Acabou")

select = input("Se deseja um Timer digite T\nSe deseja um contador digite C\nSe deseja sair digite Q\nO que você quer : ").lower()
if select == "t":
	t=input("\nLembrando que o tempo é em minutos\nQuanto tempo de Timer ? ")
	timer(int(t))
elif select == "c":
	t=input("\nLembrando que o tempo é em segundos\nQuanto tempo de Contador ? ")
	countdown(int(t))
elif select == "q":
	print("Volte Sempre")

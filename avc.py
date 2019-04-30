# Autor: Manoel Santiago
# Em Abril 2019
# Conceito: Média harmônica é definida como o número de membros dividido pela soma do inverso dos membros
# Fonte: https://pt.wikipedia.org/wiki/M%C3%A9dia_harm%C3%B4nica

print("Programa calcula a Média Harmônica entre 3 valores")
print("=======================================================")

from time import sleep
import os
import sys

# Variáveis que recebem os valores digitados pelo usuário e fazem o tratamento de exceção
#def calculo():
while True:
	try:
		v1 = float(input("Digite o primeiro valor: "))
		print("")
		break
	except Exception:
		print("\nValor inválido. Informe apenas números reais\n")

while True:			
	try:
		v2 = float(input("Digite o segundo valor valor: "))
		print("")
		break
	except Exception:		
		print("\nValor inválido. Informe apenas números reais\n")

while True:			
	try:
		v3 = float(input("Digite o terceiro valor: "))
		print("")
		break
	except Exception:
		print("\nValor inválido. Informe apenas números reais\n")
		
# Variável que calcula a média harmonica dos 3 valores fornecidos pelo usuário
try:	
	media_harmonica = (3/((1/v1)+(1/v2)+(1/v3)))
except ZeroDivisionError:
	print("Impossível calcular média harmônica de zero")
	os.system("pause")
			
print("")

''' É exibido ao usuário os 3 valores que ele digitou seguido do
resultado do cálculo da média harmônica dos mesmos '''
print("\nA Média Harmônica entre {}, {} e {}, é: {:.2f}\n".format(v1,v2,v3, media_harmonica))
print("\nObrigado por utilizar nosso sistema!\n")
sleep(4)
sys.exit()

''' Função que mantém o programa em execução após o cálculo
quando executado no prompt de comando do Windows '''
#os.system("pause")

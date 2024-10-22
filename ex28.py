#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu 
from random import randint
from time import sleep
n = randint(0, 5)
print('Vou pensar em um número entre 0 e 5... ')
sleep(1)
n = int(input("Qual numero estou pensando? "))
if n == n:
    print("Parabéns, você conseguiu me vencer!")
else:
    print("Que pena, você perdeu. O número que eu estava pensando era {}")
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo_graus = float(input("Ângulo em graus: "))

angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print("Seno do ângulo: ",seno )
print("Cosseno do ângulo: ", cosseno)
print("Tangente do ângulo: ", tangente)
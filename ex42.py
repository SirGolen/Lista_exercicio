#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo sera formado:
#Equilatero: todos os lados são iguais
#Isóceles: dois lados são iguais
#Escaleno: todos os lados diferentes
a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if a == b == c:
    print("Triângulo Equilátero!")
elif a == b or a == c or b == c:
    print("Triângulo Isóceles!")
else:
    print("Triângulo Escaleno!")
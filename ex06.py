#Crie um algoritmo que leia um número que mostre o dobro, o triplo e a raiz quadrada
num = float(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print(f'O dobro de {num} é {dobro:.2f}',f'Já o triplo é {triplo:.2f}',f' enquanto a raiz é {raiz:.2f}.')

#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo de alistamento

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# Perguntar ao usuário o ano de nascimento do jovem
ano_nascimento = int(input("Digite o ano de nascimento do jovem: "))

# Calcular a idade atual do jovem
from datetime import date
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

# Definir a idade mínima e máxima para o alistamento
idade_minima = 18
idade_maxima = 20

# Verificar a situação do jovem
if idade < idade_minima:
    print("Ele ainda vai se alistar ao serviço militar.")
    print(f"Faltam {idade_minima - idade} anos para o alistamento.")
elif idade == idade_minima:
    print("É a hora de se alistar ao serviço militar.")
else:
    print("Já passou do tempo de alistamento.")
    print(f"Já se passaram {idade - idade_maxima} anos desde o prazo de alistamento.")
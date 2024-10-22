#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5 : Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#Entre 25 até 30: Sobrepeso
#Entre 30 até 40: Obesidade
#Acima de 40: Obesidade mórbida
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return f"Seu IMC é {imc:.2f} e você está abaixo do peso."
    elif 18.5 <= imc < 25:
        return f"Seu IMC é {imc:.2f} e você está no peso ideal."
    elif 25 <= imc < 30:
        return f"Seu IMC é {imc:.2f} e você está com sobrepeso."
    elif 30 <= imc < 40:
        return f"Seu IMC é {imc:.2f} e você está com obesidade."
    else:
        return f"Seu IMC é {imc:.2f} e você está com obesidade mórbida."

# Exemplo de uso:
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
print(calcular_imc(peso, altura))
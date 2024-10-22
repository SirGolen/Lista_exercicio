#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada Km acima do limite

def calcular_multa(velocidade):

    limite = 80 
    valor_por_km = 7  

    if velocidade > limite:
        km_acima_do_limite = velocidade - limite
        multa = km_acima_do_limite * valor_por_km
        return multa
    else:
        return 0

def main():
    velocidade = float(input("Digite a velocidade do carro em Km/h: "))
    multa = calcular_multa(velocidade)

    if multa > 0:
        print(f"Você foi multado! O valor da multa é R$ {multa:.2f}.")
    else:
        print("Você está dentro do limite de velocidade.")

if __name__ == "__main__":
    main()
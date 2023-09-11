def calcular_idade(ano_nascimento):
    ano_atual = 2023
    idade = ano_atual - ano_nascimento
    return idade

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (1922-2022): "))
            if 1922 <= ano_nascimento <= 2022:
                return ano_nascimento
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")

nome_completo = input("Digite seu nome completo: ")
ano_nascimento = obter_ano_nascimento()

idade = calcular_idade(ano_nascimento)
print(f"Olá, {nome_completo}! Você completou ou completará {idade} anos em 2023.")

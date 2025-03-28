 #5)  Faça um algoritmo que solicite o ano que o usuário nasceu, depois disso, faça o programa descrever se o usuário fará ou já fez 18 anos neste ano.

    # Solicita o ano atual ao usuário
ano_atual = int(input("Digite o ano atual: "))

# Solicita o ano de nascimento do usuário
ano_nascimento = int(input("Digite o ano em que você nasceu: "))

# Calcula a idade do usuário
idade = ano_atual - ano_nascimento

# Determina se o usuário fará ou já fez 18 anos neste ano
if idade == 18:
    print("Você faz 18 anos este ano!")
elif idade > 18:
    print("Você já fez 18 anos.")
else:
    print("Você ainda não tem 18 anos.")
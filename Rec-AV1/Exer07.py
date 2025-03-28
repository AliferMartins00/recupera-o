  #7) Faça um programa que solicite ao usuário 2 valores, utilize uma condição ternária para escrever qual o maior valor: o primeiro ou o segundo (caso os valores sejam iguais, considere o segundo).

# Solicita dois valores ao usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Utiliza uma condição ternária para determinar o maior valor
maior_valor = valor2 if valor1 <= valor2 else valor1

# Exibe o maior valor no console
print(f"O maior valor é: {maior_valor}")
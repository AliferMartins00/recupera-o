#3) Faça um algoritmo que solicite um número ao usuário, depois disso, escreva True no console, caso o número tenha dois dígitos (Esteja entre 10 e 99), caso contrário escreva False.

numero = int(input("Digite um numero: "))
dois_digitos = 10 <= numero <= 99
print(dois_digitos)
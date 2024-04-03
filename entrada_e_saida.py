# Questão 1:
# def nome():
#     nome = input("Qual o seu nome? ")
#     print(f'Olá {nome}! Seja bem vindo(a).')

# nome()

# Questão 2:
# def somar_numeros():
#     num1 = int(input("Digite o 1º número: "))
#     num2 = int(input("Digite o 2º número: "))
#     soma = num1 + num2
#     print(f'A soma dos números é = {soma}')
# somar_numeros()

# Questão 3:
# def multiplica_numeros():
#     num1 = int(input("Digite o 1º número: "))
#     num2 = int(input("Digite o 2º número: "))
#     multiplicar = num1 * num2
#     print(f'O produto dos números é: {multiplicar}')
# multiplica_numeros()

# Questão 4:
# def divide_numeros():
#     num1 = int(input("Digite o 1º número: "))
#     num2 = int(input("Digite o 2º número: "))
#     dividir = num1 / num2
#     print(f'O produto dos números é: {dividir}')
# divide_numeros()

# Questão 5:
def calcular_imc():
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite o seu peso: "))
    calcula_imc = peso / (altura*altura)
    print(f'O seu IMC é: {calcula_imc}')

calcular_imc()
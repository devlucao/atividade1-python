"""
Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.

As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

Trate os seguintes erros:
Entrada inválida (não numérica) para os números
Divisão por zero
Operação inválida

Use try/except para capturar e tratar os erros apropriadamente.

Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, *, /): ")

try:
    if operacao == "+":
        resultado = numero1 + numero2
        print(f"O resultado de {numero1} + {numero2} é: {resultado}")
    elif operacao == "-":
        resultado = numero1 - numero2
        print(f"O resultado de {numero1} - {numero2} é: {resultado}")
    elif operacao == "*":
        resultado = numero1 * numero2
        print(f"O resultado de {numero1} * {numero2} é: {resultado}")
    elif operacao == "/":
        resultado = numero1 / numero2
        print(f"O resultado de {numero1} / {numero2} é: {resultado}")
    else:
        print("Operação inválida. Por favor, insira uma operação válida (+, -, *, /).")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, insira números válidos.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    print("Fim da execução.")


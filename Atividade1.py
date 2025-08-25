# Atividade 1
print("Hello, World!")

# Atividade 2
numero1 = int(12)
numero2 = int(14)

soma = numero1 + numero2

print("A soma de", numero1, "e", numero2, "é:", soma)

# Atividade 3
comprimento = int(12)
largura = int(14)
altura = int(20)

volume = comprimento * largura * altura

print("O volume do paralelepípedo é:", volume)

# Atividade 4
nomeProduto = "Cadeira Infantil"
precoUnitario = float(89.90)
quantidade = int(3)

precoTotal = "{:.2f}".format(precoUnitario * quantidade)

print("O preço total de", quantidade, nomeProduto, "é: R$", precoTotal)

#Atividade 5
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))  
d = int(input("Digite o quarto valor: "))

diferenca = (a * b) - (c * d)

print("A diferença é:", diferenca)
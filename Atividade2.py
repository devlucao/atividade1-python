#Atividade 1

valorBRL = float(100.00)
taxaConversaoDolar = float(5.60)
taxaConversaoEuro = float(6.60)

print("Valor em Dólar: U$ {:.2f}".format(valorBRL/taxaConversaoDolar))
print("Valor em Euro: € {:.2f}".format(valorBRL/taxaConversaoEuro))

#Atividade 2
nomeProduto = "Camiseta"
precoOriginal = float(50.00)
percentualDesconto = float(0.20)

valorDesconto = "{:.2f}".format(precoOriginal * percentualDesconto)
precoComDesconto = precoOriginal * (1 - percentualDesconto)

print("O preço final da {} com desconto de R$ {} é: R$ {:.2f}".format(nomeProduto, valorDesconto, precoComDesconto))

#Atividade 3
nota1 = float(7.5)
nota2 = float(8.0)
nota3 = float(6.5)

media = (nota1 + nota2 + nota3) / 3

print("A média das notas é: {:.2f}".format(media))

#Atividade 4
distanciaPercorrida = float(300.0)
combustivelGasto = float(25.0) 

mediaConsumo = distanciaPercorrida / combustivelGasto
print("A média de consumo do veículo é: {:.2f} km/l".format(mediaConsumo))

#Atividade 5
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

x = a + b

print("O valor de X é: {}".format(x))

#Atividade 6
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora do funcionário: "))

salario = horas_trabalhadas * valor_por_hora

print("Funcionário Número: {}".format(numero_funcionario), "Salário: R$ {:.2f}".format(salario))
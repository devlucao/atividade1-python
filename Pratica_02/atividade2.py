#Atividade 2
nomeProduto = "Camiseta"
precoOriginal = float(50.00)
percentualDesconto = float(0.20)

valorDesconto = "{:.2f}".format(precoOriginal * percentualDesconto)
precoComDesconto = precoOriginal * (1 - percentualDesconto)

print("O preço final da {} com desconto de R$ {} é: R$ {:.2f}".format(nomeProduto, valorDesconto, precoComDesconto))


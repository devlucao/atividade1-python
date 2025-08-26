# Atividade 4
nomeProduto = "Cadeira Infantil"
precoUnitario = float(89.90)
quantidade = int(3)

precoTotal = "{:.2f}".format(precoUnitario * quantidade)

print("O preço total de", quantidade, nomeProduto, "é: R$", precoTotal)


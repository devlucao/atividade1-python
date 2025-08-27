def calcular_desconto(preco, percentual_desconto):
    preco = float(input("Digite o preço do produto: R$ "))
    percentual_desconto = float(input("Digite o percentual de desconto (por exemplo, 20 para 20%): "))

    desconto = (percentual_desconto / 100) * preco
    preco_final = preco - desconto
    return print(f"O preço final após um desconto de {percentual_desconto:.1f}% é: R$ {preco_final:.2f}")

calcular_desconto(100, 20)
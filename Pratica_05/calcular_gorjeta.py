"""
    Calcula o valor da gorjeta com base no valor da conta e no percentual da gorjeta.

    Parâmetros:
    valor_conta (float): O valor total da conta.
    percentual_gorjeta (float): O percentual da gorjeta (por exemplo, 15 para 15%).

    Retorna:
    float: O valor da gorjeta.
"""
def calcular_gorjeta(valor_conta, percentual_gorjeta):
    gorjeta = (percentual_gorjeta / 100) * valor_conta
    return gorjeta

total_conta = float(input("Digite o valor total da conta: R$ "))
percentual = float(input("Digite o percentual da gorjeta (por exemplo, 15 para 15%): "))

gorjeta = calcular_gorjeta(total_conta, percentual)
print(f"O valor da gorjeta de {percentual:.1f}% é: R$ {gorjeta:.2f}")
nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
comissao_percentual = 0.15

vendas = float(input("Digite o valor total das vendas realizadas pelo vendedor: "))
comissao = vendas * comissao_percentual

print(f"O vendedor {nome_vendedor} receberá um salário fixo de R$ {salario_fixo:.2f} e uma comissão de R$ {comissao:.2f}, totalizando R$ {salario_fixo + comissao:.2f}.")
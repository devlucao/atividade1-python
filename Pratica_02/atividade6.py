#Atividade 6
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora do funcionário: "))

salario = horas_trabalhadas * valor_por_hora

print("Funcionário Número: {}".format(numero_funcionario), "Salário: R$ {:.2f}".format(salario))
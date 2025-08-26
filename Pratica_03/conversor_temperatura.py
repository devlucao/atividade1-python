temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
unidade_destino = input("Digite a unidade para qual deseja converter (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
## fonte: https://www.infoescola.com/fisica/conversao-de-escalas-termometricas/
if unidade_origem == 'C':
    if unidade_destino == 'F':
        temperatura_convertida = (temperatura * 1.8) + 32
    elif unidade_destino == 'K':
        temperatura_convertida = temperatura + 273
    else:
        temperatura_convertida = temperatura
elif unidade_origem == 'F':
    if unidade_destino == 'C':
        temperatura_convertida = (temperatura - 32) / 1.8
    elif unidade_destino == 'K':
        temperatura_convertida = (temperatura - 32) * 5/9 + 273
    else:
        temperatura_convertida = temperatura
elif unidade_origem == 'K':
    if unidade_destino == 'C':
        temperatura_convertida = temperatura - 273
    elif unidade_destino == 'F':
        temperatura_convertida = (temperatura - 273) * 1.8 + 32
    else:
        temperatura_convertida = temperatura
else:
    print("Unidade de origem inválida.")

print(f"A temperatura convertida é: {temperatura_convertida:.2f} {unidade_destino}")
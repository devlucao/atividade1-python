def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    idade_em_dias = idade * 365
    
    return print(f"Você tem aproximadamente {idade_em_dias} dias de idade.")

calcular_idade(1991, 2025)
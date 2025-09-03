pares = []
impares = []

try:
  numero = int(input("Digite um número inteiro (ou fim para sair): "))
  while True:
    if numero == 'fim':
            break
    
    if numero % 2 == 0:
      pares.append(numero)
    else:
      impares.append(numero)
    numero = int(input("Digite outro número inteiro (ou fim para sair): "))
except ValueError:
  print(f"Total de números pares: {len(pares)}")
  print(f"Total de números ímpares: {len(impares)}")




peso = int(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 24.9:
    print("Peso normal")
elif imc >= 25 and imc < 29.9:
    print("Sobrepeso")
else:
    print("Obeso")
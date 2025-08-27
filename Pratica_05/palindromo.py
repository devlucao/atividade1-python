def palindromo(palavra):
    palavra = input("Digite uma palavra: ")
    if palavra == palavra[::-1]:
        return print("Sim! É um palíndromo!")
    else:
        return print("Não! Não é um palíndromo!")
    
palindromo("arara")
    
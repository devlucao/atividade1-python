senha = input("Digite uma senha: ")

try:
    if len(senha) < 8:
        print("Senha deve ter pelo menos 8 caracteres.")
    if not any(char.isdigit() for char in senha):
        print("Senha deve conter pelo menos um número.")
    else:
        print("Senha válida!")
except ValueError:
    print(f"Ocorreu um erro inesperado.")
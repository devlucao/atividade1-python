def calcular_media_turma():
    """
    Calcula a média de notas de uma turma.
    O programa solicita notas até que o professor digite 'fim'.
    Notas válidas estão entre 0 e 10.
    """
    notas_da_turma = []

    while True:
        nota = input("Digite a nota (0 a 10) ou 'fim' para encerrar: ").lower()

        # Verifica se o usuário quer sair do programa
        if nota == 'fim':
            break

        # Tenta converter a nota para float e trata possíveis erros
        try:
            nota = float(nota)
            # Verifica se a nota está no intervalo válido (0 a 10)
            if 0 <= nota <= 10:
                notas_da_turma.append(nota)
                print(f"Nota {nota} registrada com sucesso.")
            else:
                print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
        except ValueError:
            print("nota inválida. Por favor, insira um número ou digite 'fim'.")
    
    # Após o loop, verifica se há notas para calcular a média
    if notas_da_turma:
        media = sum(notas_da_turma) / len(notas_da_turma)
        print("\n--- Resultados ---")
        print(f"Total de notas registradas: {len(notas_da_turma)}")
        print(f"A média da turma é: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")

# Chama a função para rodar o programa
calcular_media_turma()
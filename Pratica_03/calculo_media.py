nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 1) / 10

if media >= 7.0:
    print(f"Media: {media:.1f}\nAluno aprovado.")
elif media < 5.0:
    print(f"Media: {media:.1f}\nAluno reprovado.")
else:
    print(f"Media: {media:.1f}\nAluno em exame.")
    nota_exame = float(input("Digite a nota do exame: "))
    nova_media = (media + nota_exame) / 2
    if nova_media >= 5.0:
        print(f"Aluno aprovado.\nMedia final: {nova_media:.1f}")
    else:
        print(f"Aluno reprovado.\nMedia final: {nova_media:.1f}")
# Nome: Rodrigo Barcellos Santos Silva
# Matricula: 2026B012258

# ENTRADA

nome = input("Digite seu nome: ")

matricula = input("Digite sua matricula: ")

disciplina = input("Digite o nome da disciplina: ")

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

freq = int(input("Digite sua frequência: "))


# VALIDAÇÃO

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10:
    print("Aviso: uma ou mais notas são inválidas. As notas devem estar entre 0 e 10.")

elif freq < 0 or freq > 100:
    print("Aviso: frequência inválida. A frequência deve estar entre 0 e 100.")

else:

    # PROCESSAMENTO

    media = (nota1 + nota2 + nota3) / 3


    # SITUAÇÃO DO ALUNO - CONDICIONAL ANINHADA

    if media >= 7:
        if freq >= 75:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado por falta"
    else:
        if freq >= 75:
            situacao = "Reprovado por nota"
        else:
            situacao = "Reprovado por nota e falta"


    # CONCEITO

    if media >= 9:
        conceito = "A"
    elif media >= 7:
        conceito = "B"
    elif media >= 5:
        conceito = "C"
    else:
        conceito = "D"


    # MAIOR NOTA

    if nota1 >= nota2 and nota1 >= nota3:
        maior_nota = nota1
    elif nota2 >= nota1 and nota2 >= nota3:
        maior_nota = nota2
    else:
        maior_nota = nota3


    # MENOR NOTA

    if nota1 <= nota2 and nota1 <= nota3:
        menor_nota = nota1
    elif nota2 <= nota1 and nota2 <= nota3:
        menor_nota = nota2
    else:
        menor_nota = nota3


    # QUANTO FALTA PARA PASSAR

    if media < 7:
        pontos_faltantes = 7 - media
        mensagem_media = f"Faltaram {pontos_faltantes:.2f} ponto(s) para atingir a média 7.0"
    else:
        mensagem_media = "Parabéns! Você atingiu a média 7.0."


    # SAÍDA

    print()
    print("======================================")
    print("       ANALISE ACADEMICA")
    print("======================================")

    print(f"Aluno......: {nome} ({matricula})")
    print(f"Disciplina.: {disciplina}")
    print(f"Media......: {media:.2f}")
    print(f"Frequencia.: {freq:.2f}%")
    print(f"Conceito...: {conceito}")
    print(f"Maior nota.: {maior_nota:.2f}")
    print(f"Menor nota.: {menor_nota:.2f}")
    print(f"Situacao...: {situacao}")
    print(mensagem_media)

    print("======================================")
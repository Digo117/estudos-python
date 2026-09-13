#Questão 3

quantidade = 0
soma = 0

nota = float(input("Digite uma nota (0 a 10) ou -1 para encerrar: "))

while nota != -1:
    soma += nota
    quantidade += 1

    nota = float(input("Digite uma nota (0 a 10) ou -1 para encerrar: "))

if quantidade == 0:
    print("Não há notas.")
else:
    media = soma / quantidade
    print(f"Quantidade de notas: {quantidade} e média: {media:.2f}")
 
 
#Questão 4
 
numero = int(input("Digite um número inteiro positivo: "))

while numero >= 1:
    print(numero)
    numero = numero - 1

print("Fim")

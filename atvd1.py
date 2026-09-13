#Questão 1

salario_atual = float(input("Digite o salário atual:"))
percentual_aumento = float(input("Digite o percentual de aumento:"))

aumento = (salario_atual * percentual_aumento) / 100
novo_salario = salario_atual + aumento

print(f"Seu aumento é de {aumento:.2f} reais")
print(f"Seu novo salário é de {novo_salario:.2f} reais")


#Questão 2 

ano = float(input("Digite o ano: "))

bissexto = (ano % 4 == 0 and not (ano % 100 == 0)) or (ano % 400 == 0)

print(f"O ano {ano} é bissexto? {bissexto}")


#Questão 3

numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))

maior = numero1 > numero2
igual = numero1 == numero2
diferente = numero1 != numero2

print(f"{numero1} é maior que {numero2}? {maior}")
print(f"{numero1} é igual a {numero2}? {igual}")
print(f"{numero1} é diferente de {numero2}? {diferente}")


#Questão 4

pontos = 100

valor1 = float(input("Valor 1: "))
valor2 = float(input("Valor 2: "))
valor3 = float(input("Valor 3: "))

pontos += valor1
pontos -= valor2
pontos *= valor3

print(f"Pontuação final: {pontos}")


#Questão 5


duracao= int(input("Digite a duração em minutos:")) 

hora =  duracao // 60
minutos = duracao % 60

print (f"{duracao} minutos equivale a {hora} hora(s) e {minutos} minuto(s)")


#Questão 6

numero = int(input("Digite um número: "))

par = numero % 2 == 0
multiplo5 = numero % 5 == 0
ultimo_digito = numero % 10

print(f"{numero} é par? {par}")
print(f"{numero} é múltiplo de 5? {multiplo5}")
print(f"Último dígito: {ultimo_digito}")


#Questão 7


valor = int(input("Valor do saque: "))

notas50 = valor // 50
resto = valor % 50

notas10 = resto // 10
notas1 = resto % 10

print(f"Notas de R$ 50: {notas50}")
print(f"Notas de R$ 10: {notas10}")
print(f"Notas de R$ 1: {notas1}")


#Questão 8


nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média: {media:.2f}")


#Questão 9


nota = float(input("Digite a nota: "))

valida = 0 <= nota <= 10

print(f"A nota {nota} é válida? {valida}")


#Questão 10

media = float(input("Média: "))
frequencia = float(input("Frequência (%): "))

condicao_media = media >= 7
condicao_frequencia = frequencia >= 75

aprovado = condicao_media and condicao_frequencia
pelo_menos_uma = condicao_media or condicao_frequencia
nao_aprovado = not aprovado

print(f"Aprovado: {aprovado}")
print(f"Atingiu ao menos uma condição: {pelo_menos_uma}")
print(f"Não aprovado: {nao_aprovado}")

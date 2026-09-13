#Questão 1

idade = int(input("Digite sua idade:"))

if idade <= 12:
    print("Criança.")
elif idade <= 17:
    print("Adolescente.")
elif idade <= 59:
    print("Adulto.")
else:
    print("Idoso.")
    
    
#Questão 2

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))

if num1 > num2:
    print(f"O maior é: {num1}")
elif num1 < num2:
    print(f"O maior é: {num2}")
else:
    print("Os números são iguais.")


#Questão 3

num = int(input("Digite um número:"))

if num > 0:
    print("É positivo.")
    if num%2 == 0:
        print("É par.")
    else:
        print("É ímpar.")
elif num == 0:
    print("O número é zero.")
elif num < 0:
    print("É negativo.")
    if num%2 == 0:
        print("É par.")
    else:
        print("É ímpar.")
        
        

#Questão 4

nota = float(input("Digite sua nota:"))

if nota < 0 or nota > 10:
    print("Nota inválida, tente novamente.")
else:
    
    if nota < 5:
        print("Conceito: D")
    elif nota <= 6.9:
        print("Conteico: C")
    elif nota <= 8.9:
        print("Conceito: B")
    else:
        print("Conceito: A")
        

#Questão 5

num = int(input("Digite um número:"))

if num%2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
    
    
#Questão 6

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")

escolha = int(input("Escolha uma opção:"))

if escolha == 1:
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif escolha == 2:
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif escolha == 3:
    resultado = num1 * num2
    print(f"Resultado: {resultado}") 
else:
    print("Opção inválida.")

#Questão 7

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")
    
#Questão 8

media = float(input("Digite a média: "))
frequencia = float(input("Digite a frequência: "))

if media < 0 or media > 10:
    print("Nota inválida. O valor deve estar entre 0 e 10.")
elif frequencia < 0 or frequencia > 100:
    print("Frequência inválida. O valor deve estar entre 0 e 100.")
else:
    if media >= 7 and frequencia >= 75:
        print("Aprovado")
    elif media < 7 and frequencia < 75:
        print("Reprovado por nota e falta")
    elif media < 7:
        print("Reprovado por nota")
    else:
        print("Reprovado por falta")

#Questão 9

idade = int(input("Digite sua idade:"))

if idade < 5:
    print("Não permitido.")
elif idade <=10:
    print("Categoria: Infantil.")
elif idade <= 15:
    print("Categoria: Juvenil.")
else:
    print("Categoria: Adulto.")
    

#Questão 10

media = float(input("Digite a média: "))
frequencia = float(input("Digite a frequência: "))

if media < 0 or media > 10:
    print("Nota inválida. O valor deve estar entre 0 e 10.")
elif frequencia < 0 or frequencia > 100:
    print("Frequência inválida. O valor deve estar entre 0 e 100.")
else:
    if media >= 7 and frequencia >= 75:
        print("Aprovado")
    else:
        print("Reprovado")
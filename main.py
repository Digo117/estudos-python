def mostrar_titulo():
    print("""
          ===================
            DARK WORLD RPG
          ===================
          """)
def mostrar_opcoes():
    print("""
          1 - Novo Jogo
          
          2 - Carregar jogo
          
          3 - Sair
          """)
    escolha = input("Escolha:")
    return escolha
def criar_personagem():
    nome = input("Qual o seu nome?")
    classe = input("Qual a sua classe?")
    personagem = {
        "nome": nome,
        "classe": classe,
        "vida": 100,
        "ataque": 15,
        "defesa": 10,
        "nivel": 1,
        "xp": 0
    }
    return personagem
def combate(personagem):
    goblin = {
        "nome": "Goblin",
        "vida": 50,
        "ataque": 8
    }
    return goblin





while True:
    mostrar_titulo()
    escolha = mostrar_opcoes()
    if escolha == "1":
        print("Começando...")
        personagem = criar_personagem()
        print(f"Bem vindo {personagem["nome"]} o {personagem["classe"]}")
        goblin = combate(personagem)
        print(f"Essa não, apareceu um Goblin!")
        print(f"Vida do goblin: {goblin['vida']}")
        print(f"Sua vida: {personagem['vida']}")
        input("Tecle 'enter' para atacar...")
        goblin["vida"] -= personagem["ataque"]
        if goblin["vida"] <= 0:
            print("Você derrotou o goblin!")
            break
        
    
    elif escolha == "2":
        print("Carregando...")
    elif escolha == "3":
        print("Até Logo!")
        break
    else:
        print("""
              Opção Inválida!
              Tente Novamente.
              """)
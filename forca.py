#TRABALHO RICARDO GROTH E ENZO SCHULTZ

from funcoes import limparTela, aguarde

dicas = []
digitadas = []
erradas = []
vidas = 6

desafiante = input("Digite seu nome desafiante: ")
jogador = input("Digite seu nome jogador: ")

print("SALVANDO INFORMAÇÕES...")
aguarde(2)
limparTela()

chave = input(f'{desafiante}, qual é a palavra chave? ')
espacos = "_" * len(chave)
dica1 = input(f'{desafiante}, qual é a primeira dica? ')
dica2 = input(f'{desafiante}, qual é a segunda dica? ')
dica3 = input(f'{desafiante}, qual é a terceira dica? ')


print("SALVANDO INFORMAÇÕES...")
aguarde(2)
limparTela()

print(f'{jogador}, sua palavra chave contém {len(chave)} letras. ')
print(espacos)

def boneco(vidas):
    if vidas == 6:
        print(" _________     ")
        print("|         |    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif vidas == 5:
        print(" _________     ")
        print("|         |    ")
        print("|         O    ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif vidas == 4:
        print(" _________     ")
        print("|         |    ")
        print("|         O    ")
        print("|         |    ")
        print("|              ")
        print("|              ")
    elif vidas == 3:
        print(" _________     ")
        print("|         |    ")
        print("|         O    ")
        print("|        /|    ")
        print("|              ")
        print("|              ")
    elif vidas == 2:
        print(" _________     ")
        print("|         |    ")
        print("|         O    ")
        print("|        /|\   ")
        print("|              ")
        print("|              ")
    elif vidas == 1:
        print(" _________     ")
        print("|         |    ")
        print("|         O    ")
        print("|        /|\   ")
        print("|        /     ")
        print("|              ")
    else:
        print(" _________     ")
        print("|         |    ")
        print("|         O    ")
        print("|        /|\   ")
        print("|        / \   ")
        print("|              ")
        print("\nGAME OVER!")






while True:
    boneco(vidas)
    opcao = input(
        f'{jogador}, digite (0) para jogar, (1) para solicitar dica ou digite (2) para sair:')

    if opcao == "1":
        if len(dicas) == 0:
            print('Sua primeira dica é: ', dica1)
            dicas.append(dica1)
            print(" Restam apenas 2 dicas")
            aguarde(2)
            limparTela()
        elif len(dicas) == 1:
            print('Sua segunda dica é: ', dica2)
            dicas.append(dica2)
            print(" Resta apenas 1 dica")
            aguarde(2)
            limparTela()
        elif len(dicas) == 2:
            print('Sua terceira dica é: ', dica3)
            dicas.append(dica3)
            print(" Restam 0 dicas")
            aguarde(2)
            limparTela()
        else:
            print("Você já usou todas as dicas!")
            aguarde(2)
            limparTela()
    elif opcao == "0":
        letra = input('Qual letra você gostaria de arriscar? ')
        if len(letra) > 1:
            print("Você só pode digitar uma letra por vez!")
            aguarde(2)
            limparTela()
            continue
        if letra in chave:
            print("Você acertou uma letra!")
            aguarde(2)
            limparTela()
            digitadas.append(letra)
            espacos = ""
            for letra_chave in chave:
                if letra_chave in digitadas:
                    espacos += letra_chave
                else:
                    espacos += "_"
            print(espacos)
            if espacos == chave:
                print(f"Parabéns, {jogador}! Você venceu!")
                break
        else:
            print("Você errou uma letra!")
            aguarde(2)
            limparTela()
            erradas.append(letra)
            vidas -= 1
            print(f"Você tem {vidas} chances")
            if vidas == 0:
                boneco(vidas)
                print(f"Você perdeu, {jogador}!")
                break
    elif opcao == "2":
        print(f"Até mais, {jogador}!")
        break
    else:
        print("Opção inválida!")
        aguarde(2)
        limparTela()
        continue
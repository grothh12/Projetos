from funcoes import limparTela, aguarde, lerInteiro, lerString

while True:
    limparTela()
    print("Hackday - Inscrições")
    print("(0) Sair")
    print("(1) Nova Inscrição")
    print("(2) Lista de Inscritos")
    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        print("Informe os dados abaixo para uma nova inscrição:")
        nome = lerString("Nome: ")
        ra = lerInteiro("RA: ")
        arquivo = open("bd.atitus","a")
        arquivo.write(nome+ "-"+str(ra)+"\n")
        arquivo.close()   
        print("Dados Salvos!")
        aguarde(2)


    elif opcao == "2":
        try:
            arquivo = open("bd.atitus","r")
            dados = arquivo.read()
            print(dados)
            arquivo.close()
            aguarde(5)
        except:
            print("Nenhum dado encontrado")
            arquivo = open("bd.atitus","w")
            arquivo.close()
            aguarde(2)

    else:
        print("Opção Invalida!")
        aguarde(2)
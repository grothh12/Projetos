import os
import time
os.system("cls")
print("Seja bem vindo ao Sistema!")
time.sleep(1)
while True:
    os.system("cls")
    print("(0) Sair")
    print("(1) Conversão em C")
    print("(2) Conversão em F")
    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        print("Convertendo F para C")
        input("press enter to continue")
    elif opcao == "2":
        print("Convertendo C para F")
        input("press enter to continue")
    else:
        print("Opcao invalida!")
        input("press enter to continue")
print("Volte sempre!")
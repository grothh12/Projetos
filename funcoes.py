import os
import time

def limparTela():
    os.system("cls")

def aguarde(segundos=1):
    time.sleep(segundos)

def soma(numero1, numero2):
    soma = numero1 + numero2
    return soma

def convertCelsiusFire(fahrenheit):
    celsius = (fahrenheit - 32)/1.8
    return celsius

def mudarCor(codeCor):
    os.system("color "+str(codeCor))

def lerInteiro(mensagem):
    while True:
        try:
            variavel = int(input(mensagem))
            return variavel

        except:
            print("Valor informado incorretamente!")

def lerString(mensagem):
    while True:
        variavel = input(mensagem)
        if len(variavel)>1:
            return variavel
        else:
            print("Valor informado Incorretamente")

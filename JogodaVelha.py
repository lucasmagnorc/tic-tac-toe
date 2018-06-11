# -*- coding: utf-8 -*-
import sys
import os
import funcoesJDV
import agenteSimples
from random import randint

resultado = False
posicao = 99
simbolo = ""
simboloHumano = " "
simboloIa = " "
tabuleiro = [".",".",".",".",".",".",".",".","."]
contadorJogadas = 0
jogaPrimeiro = randint(0,1)

# Limpando o console
os.system('clear')

while simbolo != "1" and simbolo != "2":
    simbolo = input("1 para X  \n2 para O \nDigite o número correspondente ao símbolo: ")
    if simbolo == "1":
        simboloHumano = "X"
        simboloIa = "O"
    elif simbolo == "2":
        simboloHumano = "O"
        simboloIa = "X"
    print(simboloHumano)
    os.system('clear')

while resultado != True:
    # Limpando o console
    os.system('clear')

    # Verifica Empate
    if funcoesJDV.verificaEmpate(tabuleiro) == True:
        break

    # Imprimindo tabuleiro
    funcoesJDV.imprimiTabuleiro(tabuleiro, simboloHumano, simboloIa)

    # Pegando uma posição válida
    posicao = funcoesJDV.validaPosicao(tabuleiro)

    # Colocando o símbolo na posição e acrescentando contador
    tabuleiro[posicao] = simboloHumano
    contadorJogadas += 1

    # Verifica se o Humano é campeao
    campeao = funcoesJDV.verificaCampeao(tabuleiro, simboloHumano)
    if campeao == simboloHumano:
        os.system('clear')
        print("\t\tVocê VENCEU !\n\n")
        funcoesJDV.imprimiTabuleiro(tabuleiro, simboloHumano, simboloIa)
        break

    # Verifica Fim de Jogo
    if funcoesJDV.verificaEmpate(tabuleiro) == True:
        break

    agenteSimples.jogadaIa(tabuleiro, simboloIa)

    # Verifica campeao
    campeao = funcoesJDV.verificaCampeao(tabuleiro, simboloIa)
    if campeao == simboloIa:
        os.system('clear')
        print("\t\tVocê PERDEU !\n\n")
        funcoesJDV.imprimiTabuleiro(tabuleiro, simboloHumano, simboloIa)
        break

    # Verifica Fim de Jogo
    if funcoesJDV.verificaEmpate(tabuleiro) == True:
        break

    funcoesJDV.imprimiTabuleiro(tabuleiro, simboloHumano, simboloIa)

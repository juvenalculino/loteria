# @Author: Juvenal Culino
# @Date:   2020-12-04T23:22:41-02:00
# @Last modified by:   Juvenal Culino
# @Last modified time: 2020-12-07T00:09:09-10:00
#!/usr/bin/python3
# coding: utf-8 -*-
# Script Para Gerar Números da Loteria

from random import randint
from time import sleep

def jogos(quant,cartela,quantNum):
    lista = list()
    jogos = list()
    print('←→'*20)
    print('     JOGOS DA LOTERIA    ')
    print('←→'*20)
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            num = randint(1, cartela)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= quantNum:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
    for i, l in enumerate(jogos):
        print(f'Jogo {i+1}: {l}')
        sleep(0.5)
    print('-=' * 5, '< Boa sorte >', '-=' * 5)
    


def menu():
    print('''         OPÇÕES:
    |---------------|
    | [1] LOTOFÁCIL | 
    | [2] MEGA-SENA |
    | [3] LOTOMANIA |
    | [4] QUINA     | 
    | [0] SAIR      |
    |---------------|''')


while True:
    menu()
    opcao = input('\n    Escolha uma opção: ')
    try:
        if opcao == '1':
            jogos(quant=int(input('Escolha quantos jogos deseja: ')),
                  cartela=25, quantNum=15)
        elif opcao == '2':
            jogos(quant=int(input('Escolha quantos jogos deseja: ')),
              cartela=60, quantNum=6)
        elif opcao == '3':
            jogos(quant=int(input('Escolha quantos jogos deseja: ')),
              cartela=99, quantNum=50)
        elif opcao == '4':
            jogos(quant=int(input('Escolha quantos jogos deseja: ')),
              cartela=80, quantNum=5)
        elif opcao == '0':
            print('Saindo...')
            sleep(2)
            break
        else:
            print('Digite a opção correta...')
    except Exception as erro:
        print(erro)

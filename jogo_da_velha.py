
def primeira_linha(numero):
    
    saida = []

    if numero == 1:
        saida = print('|' + 'X' + '|' + ' |' + ' |')
    elif numero == 2 :
        saida = print('| ', '|', 'X', '|', '|')
    elif numero == 3 :
        saida = print('| ', '|', '|', 'X', '|')
    else:
        saida = print('| ', '| ', '| ', '| ')
    
    return saida

def segunda_linha(numero):
    
    saida = []

    if numero == 4:
        saida = print('|', 'X', '|', '|', '|')
    elif numero == 5 :
        saida = print('|', '| ', 'X', '|', '|')
    elif numero == 6 :
        saida = print('|', '|', '|', 'X', '|')
    else:
        saida = print('| ', '| ', '| ', '| ')
    
    return saida

def terceira_linha(numero):
    
    saida = []

    if numero == 7:
        saida = print('|', 'X', '|', '|', '|')
    elif numero == 8 :
        saida = print('|', '|', 'X', '|', '|')
    elif numero == 9 :
        saida = print('|', '|', '|', 'X', '|')
    else:
        saida = print('| ', '| ', '| ', '| ')
    
    return saida

def tabela_inicial():
    resultado = print(
        '| ' + '1' + ' | ' + '2' + ' | ' + '3' + ' |' + '\n'  
        '| ' + '4' + ' | ' + '5' + ' | ' + '6' + ' |' + '\n'
        '| ' + '7' + ' | ' + '8' + ' | ' + '9' + ' |'
    )

def total_jogadas(numero):
    resultado = numero
    return resultado

def numeros_selecionados_P1():
    numeros_selecionados_player_1 = []
    return numeros_selecionados_player_1

def plant_ground():

    tabela_inicial()

    quantidade_P1 = numeros_selecionados_P1()

    numeros_selecionados_player_2 = []

    if len(quantidade_P1) == 0:
        numero = 1
    else:
        pass

    if total_jogadas(numero) == 1:
        numero_jogada = 1
    else:
        numero_jogada = len(quantidade_P1) + len(numeros_selecionados_player_2)
    
    

    if quantidade_P1 != '':
        player_turn = 1
    else:
        player_turn = 2 

    if player_turn == 1:
        jogada = int( input('Jogador numero I, digite a casa escolhida (1-9):') )
    elif player_turn == 2:
        jogada = int( input('Jogador numero II, digite a casa escolhida (1-9):') )
    else:
        pass

    #numero_de_jogadas += 1
    quantidade_P1.append(jogada)
    numeros_selecionados_player_2.append(jogada)

    primeira_linha(jogada)
    segunda_linha(jogada)
    terceira_linha(jogada)

    print(quantidade_P1)
    print(numero)
    print(len(quantidade_P1))

plant_ground()


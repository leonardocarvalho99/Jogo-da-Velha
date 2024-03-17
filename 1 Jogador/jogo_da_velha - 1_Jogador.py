from random import randint
import os

#Exibir o Menu e também pedir o nome do usuário
def exibir_menu():
  print('Developed by Leonardo Carvalho\n')
  print('------ SEJA BEM VINDO AO JOGO DA VELHA -------')
  print('Lembre-se: Você pode digitar -1 para encerrar o programa imediatamente')
  nome = input('Por favor, Insira o seu nome: ')
  print('='*60)
  return nome


def LimparTela():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')


def escolher_objeto(nome):
  objeto = input('\nVamos a partida!\n%s, selecione qual objeto você deseja: [X] ou [O]:\n' % (nome)).upper()

  while objeto != 'X' and objeto != 'O' and objeto != '-1':
    objeto = input('Por favor, selecione apenas as opções válidas\nSelecione qual objeto você deseja: [X] ou [O]:\n').upper()

  LimparTela()

  if objeto == 'X':
    jogador1 = 'X'
    cpu = 'O'
    print('%s escolheu "X"!\nPortanto a CPU ficará com "O"!' % (nome))
    return jogador1, cpu

  elif objeto == 'O':
    jogador1 = 'O'
    cpu = 'X'
    print('%s escolheu "O"!\nPortanto, a CPU ficará com "X"!' % (nome))
    return jogador1, cpu

  elif objeto == '-1':
    return objeto


# Função para verificar se há um vencedor na matriz.
# Retorna True se houver um vencedor e o objeto (X ou O) que venceu
def verificar_objetos(matriz, tamanho):
  venceu = False
  objeto = ''

# Terceira linha
  if matriz[2][0] == matriz[2][1] == matriz[2][2]:
      venceu = True
      objeto = matriz[2][0]

  
# Segunda linha  
  if matriz[1][0] == matriz[1][1] == matriz[1][2]:
    venceu = True
    objeto = matriz[1][0]


# Primeira linha  
  if matriz[0][0] == matriz[0][1] == matriz[0][2]:
    venceu = True
    objeto = matriz[0][0]
    

  # Terceira coluna
  if matriz[0][2] == matriz[1][2] == matriz[2][2]:
    venceu = True
    objeto = matriz[0][2]
    

  # Segunda coluna
  if matriz[0][1] == matriz[1][1] == matriz[2][1]:
    venceu = True
    objeto = matriz[0][1]
    

  # Primeira coluna
  if matriz[0][0] == matriz[1][0] == matriz[2][0]:
    venceu = True
    objeto = matriz[0][0]

  
  #  Diagonal secundária
  if matriz[0][2] == matriz[1][1] == matriz[2][0]:
    venceu = True
    objeto = matriz[0][2]


  # Verificação da Diagonal Principal
  if matriz[0][0] == matriz[1][1] == matriz[2][2]:
    venceu = True
    objeto = matriz[0][0]

  if tamanho == 9 and venceu == False:
    venceu = 'velha'

  return venceu, objeto


# Exibir placar conforme os parâmetros de vencer ou de encerrar o programa
# parametro: se vencer for verdade ou se for velha ou se N ou -1
# nome: Nome do usuário
# turno: Após o jogador 1 fazer a jogada, o turno é setado para 2 e, com isso conseguimos perceber que ele foi a pessoa que acabou de ganhar
# a partida
def ExibirPlacar(parametro, placar1, placar2, nome, turno=0):
  mensagem = '\nPlacar:\n%s: %d pontos\nCPU: %d pontos' % (nome, placar1, placar2)

  if parametro == True:
    if turno == 2:
      print('\nTemos um vencedor!\n%s venceu a partida!' % (nome))
    else:
      print('\nTemos um vencedor!\nCPU venceu a partida!')
    print(mensagem)

  elif parametro == 'velha':
    print('\nDeu velha!\nPortanto, ninguém venceu a partida...')
    print(mensagem)

  elif parametro == 'N' or parametro == '-1':
    print('\n--> Jogo Encerrado <--')
    print(mensagem)


# Inserir X ou O na matriz
def trocar_valor(valor, objeto):
    for linha in range(len(matriz)):
      for coluna in range(len(matriz[0])):
        if valor == matriz[linha][coluna]:
          matriz[linha][coluna] = objeto



def VerificarValorEntrada(valor_digitado):
  encerrar = '-1'

  if valor_digitado == '-1':
    return encerrar

  while valor_digitado not in ('1','2','3','4','5','6','7','8','9') or valor_digitado in num_digitados:
    valor_digitado = input('Jogada não permitida.\nSelecione apenas números que estão disponíveis no tabuleiro!: ')
    if valor_digitado == '-1':
      return encerrar

  if valor == '-1':
    return encerrar

  return valor_digitado


def exibir_matriz(matriz):
  print()
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      print(matriz[i][j],end='     ')
    print('\n-------------')


def continuar_partida():
  parar = input('\nDeseja continuar partida? [S/N]\n').upper()

  while parar != 'N' and parar != 'S' and parar != '-1':
    parar = input('Comando Inválido\nDeseja continuar partida? - Tecle "S" para sim ou "N" para não - [S/N]:\n').upper()

  if parar == 'N' or parar == '-1':
    return parar


matriz = [['1','2','3'],['4','5','6'],['7','8','9']]
num_digitados = []
jogador1 = cpu = ''
placar1 = placar2 = tot_jogadas =  0
turno = 1

nome = exibir_menu()
if nome == '-1':
  exit(' --> Jogo encerrado <--\n')

escolher_objeto = escolher_objeto(nome)

while True:
  if escolher_objeto == '-1':
    print('\n--> Jogo encerrado <--')
    break

  jogador1 = escolher_objeto[0]
  cpu = escolher_objeto[1]


  exibir_matriz(matriz)

# Se turno igual a 1, então é a vez do jogador 1, se for igual a 2, é a vez da CPU
  if turno == 1:
    valor = input('\nÉ a sua vez %s! ["%s"]\nSelecione um número do tabuleiro para indicar a posição que deseja jogar: ' % (nome, jogador1))
    valor = VerificarValorEntrada(valor)

    if valor == '-1':
      print('--> Jogo encerrado <--')
      break

    trocar_valor(valor,jogador1)
    turno = 2

  else:
    valor = str(randint(1,9))

    while valor in num_digitados:
      valor = str(randint(1,9))

    trocar_valor(valor,cpu)
    turno = 1

  num_digitados.append(valor)
  tot_jogadas += 1

  ### Verificando se há um vencedor ###
  venceu = verificar_objetos(matriz, len(num_digitados))
  LimparTela()

  if venceu[0] == True and venceu[1] == jogador1:
    placar1 += 10
    exibir_matriz(matriz)
    ExibirPlacar(venceu[0], placar1, placar2, nome, turno)

    #Fazer a pergunta se quer continuar na partida
    continuar = continuar_partida()

    LimparTela()

    if continuar == 'N' or continuar == '-1':
      exibir_matriz(matriz)
      ExibirPlacar(continuar, placar1, placar2, nome)
      break


    matriz = [['1','2','3'],['4','5','6'],['7','8','9']]
    num_digitados = []

  elif venceu[0] == True and venceu[1] == cpu:
    placar2 += 10
    exibir_matriz(matriz)
    ExibirPlacar(venceu[0], placar1, placar2, nome, turno)

    continuar = continuar_partida()

    LimparTela()

    if continuar == 'N' or continuar == '-1':
      exibir_matriz(matriz)
      ExibirPlacar(continuar, placar1, placar2, nome)
      break


    LimparTela()
    matriz = [['1','2','3'],['4','5','6'],['7','8','9']]
    num_digitados = []


  elif venceu[0] == 'velha':
    exibir_matriz(matriz)
    ExibirPlacar(venceu[0], placar1, placar2, nome)


    continuar = continuar_partida()

    LimparTela()

    if continuar == 'N' or continuar == '-1':
      exibir_matriz(matriz)
      ExibirPlacar(continuar, placar1, placar2)
      break


    matriz = [['1','2','3'],['4','5','6'],['7','8','9']]
    num_digitados = []


  LimparTela()
  # print(num_digitados)

print('\nTotal de jogadas:',tot_jogadas)
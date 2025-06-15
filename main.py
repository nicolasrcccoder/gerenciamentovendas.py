import time

list_personagens = []


def add_personagem(list_personagens):
    while True:
        try:
            print('-ADICIONE PERSONAGENS-')
            personagem_nome = str(input('digite o nome (s para sair) :')).lower()
            if (personagem_nome == 's'):
                print('voltando ao hub...')
                break
            personagem_classe = str(input('digite a classe (s para sair) : ')).lower()
            if (personagem_classe == 's'):
                print('voltando ao hub...')
                break
            personagem_forca = int(input('digite o quanto de força (0 para sair) : '))
            if (personagem_forca == 0):
                print('voltando ao hub...')
                break
            personagem_vida = int(input('digite o quanto de hp (0 para sair) :'))
            if (personagem_vida == 0):
                print('voltando ao hub...')
                break

            else:
                personagens = {'nome': personagem_nome,
                               'classe': personagem_classe,
                               'força': personagem_forca,
                               'vida': personagem_vida
                               }
                list_personagens.append(personagens)
                return list_personagens
        except ValueError:
            print('apenas números!')


def mostrar_personagem(list_personagens):
    if not list_personagens:
        print('não há personagens no momento...')
    else:
        print('-SEUS PERSONAGENS-')
        for personagens in list_personagens:
            print(
                f' | NOME : {personagens['nome']} | CLASSE : {personagens['classe']} | FORÇA : {personagens['força']} | HP : {personagens['vida']}')
        print('voltando...')
        time.sleep(1)


def editar_personagem(list_personagens):
    while True:
        try:
            if not list_personagens:
                print('não há nenhum personagem para editar.')
                print('voltando ao hub...')
                break
            else:
                print('-EDITAR PERSONAGEM-')
                personagem_editando = str(input('digite o nome do personagem que gostaria de editar(s para sair):')).lower()
                encontrado = False
                if personagem_editando == 's':
                    print('voltando ao hub...')
                    break
                for personagens in list_personagens:
                    if personagem_editando == personagens['nome']:
                        print(f'---MUDANDO OS ATRIBUTOS DE {personagem_editando} ')
                        nova_classe = str(input('qual a nova classe: ')).lower()
                        nova_forca = int(input('qual a nova força :'))
                        nova_vida = int(input('qual a nova vida :'))
                        personagens['classe'] = nova_classe
                        personagens['força'] = nova_forca
                        personagens['vida'] = nova_vida
                        print('editado com sucesso!')
                        encontrado = True

                if not encontrado:
                    print('personagem não encontrado!')
                return list_personagens

        except ValueError:
            print('apenas números!')


def remover_personagem(list_personagens):
    while True:
        if not list_personagens:
            print('não há nenhum personagem para remover .')
            print('voltando ao hub...')
            break
        else:
            print('-APAGAR PERSONAGEM-')
            apagar_personagem = str(input('qual o personagem que deseja apagar (s para sair): ')).lower()
            encontrado = False
            if apagar_personagem == 's':
                print('voltando ao hub...')
                break
            for personagens in list_personagens:
                if apagar_personagem == personagens['nome']:
                    list_personagens.remove(personagens)
                    print('personagem removido!')
                    encontrado = True

            if not encontrado:
                print('personagem não encontrado!')
            return list_personagens


def batalha_personagem(list_personagens):
    player1 = None
    player2 = None
    while True:
      try:
        if not list_personagens:
            print('sem personagens aqui!')
            print('voltando ao hub...')
            break
        else:
            print('-SELECIONE DOIS PERSONAGENS PARA LUTAR CONTRA-')
            nome_1 = str(input('qual o personagem 1 (s para sair) : ')).lower()
            nome_2 = str(input('digite o personagem 2 (s para sair) : ')).lower()
            if nome_1 == 's' or nome_2 == 's':
                print('voltando ao hub...')
                break
            for personagens in list_personagens:
                if (nome_1 == personagens['nome']):
                    player1 = personagens
                if (nome_2 == personagens['nome']):
                    player2 = personagens
        print(
            f" {player1['nome']} (Força: {player1['força']} | Vida: {player1['vida']}) VS {player2['nome']} (Força: {player2['força']} | Vida: {player2['vida']})")
        print('quem tiver mais força ganha!')
        print('carregando partida ...')
        time.sleep(2)
        if player1['força'] > player2['força']:
            print(' player 1 vence na força!')
            print('partida encerrada')
            break
        if player2['força'] > player1['força']:
            print(' player 2 vence na força!')
            print('partida encerrada')
            break
        if player1['força'] == player2['força']:
            print('empate na força!')
            print('quem tiver mais vida ganha!')
            print('carregando round 2 ...')
            time.sleep(2)
            if player1['vida'] > player2['vida']:
                print('player 1 vence na vida!')
                print('partida encerrada')
                break
            if player2['vida'] > player1['vida']:
                print('player 2 vence na vida!')
                print('partida encerrada')
                break
            if player1['vida'] == player2['vida']:
                print('EMPATE')
                print('partida encerrada')
                break
      except TypeError:
          print('personagem 1 ou personagem 2 invalido!')



def main(list_personagens):
    while True:
        print('---minibatalha de RPG---')
        print(' 1 - adicionar personagens\n 2 - listar personagens\n 3 - editar personagem ')
        print(' 4 - remover personagem\n 5 - batalha entre dois personagens\n 6 - SAIR ')
        opcao = str(input('opção : '))
        if opcao == '1':
            add_personagem(list_personagens)
        elif opcao == '2':
            mostrar_personagem(list_personagens)
        elif opcao == '3':
            editar_personagem(list_personagens)
        elif opcao == '4':
            remover_personagem(list_personagens)
        elif opcao == '5':
            batalha_personagem(list_personagens)
        elif opcao == '6':
            print('saindo do jogo...')
            break


main(list_personagens)


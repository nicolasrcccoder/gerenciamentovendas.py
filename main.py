import time
from salvandodados import salvando_arquivo , carregando_arquivo
produto_id = 1
cliente_id = 1
vendas_id = 1
list_produtos = []
list_clientes = []
list_vendas = []


def cadastrar_produto():
    while True:
        global produto_id
        try:
            nome_produto = str(input('qual o nome do produto (s para sair) : ')).strip().lower()
            if nome_produto == 's':
                print('voltando ao hub')
                break
            preco_produto = float(input('qual o preço do produto (0 para sair) : '))
            if preco_produto == 0:
                print('voltando ao hub')
                break
            if preco_produto <= -1:
                print('apenas números positivos!')
                continue
            estoque_produto = int(input('qual é o estoque do produto :'))
            if estoque_produto <= -1:
                print('apenas números positivos!')
                continue
            produtos = {'id': produto_id,
                        'nome': nome_produto,
                        'preco': preco_produto,
                        'estoque': estoque_produto
                        }
            list_produtos.append(produtos)
            produto_id += 1
            print(f'{nome_produto} cadastrado com sucesso!')
        except ValueError:
            print('apenas números!')
            continue


def cadastrar_cliente():
    while True:
        global cliente_id
        nome_cliente = str(input('nome do cliente (s para sair) :')).strip().lower()
        cpf_cliente = str(input('cpf do cliente (s para sair) : '))
        if nome_cliente == 's':
            print('voltando ao hub')
            break
        if cpf_cliente == 's':
            print('voltando ao hub')
            break
        clientes = {'id': cliente_id,
                    'nome': nome_cliente,
                    'cpf': cpf_cliente
                    }
        list_clientes.append(clientes)
        cliente_id += 1
        print(f'{nome_cliente} cadastrado com sucesso!')


def registrar_vendas():
    while True:
        global vendas_id
        try:
            if not list_clientes:
                print('não há cliente para selecionar')
                break
            if not list_produtos:
                print('não há produtos para selecionar')
                break

            cliente_selecionar = str(input('qual cliente selecionar (s para sair) :')).strip().lower()
            if cliente_selecionar == 's':
                print('voltando ao hub')
                break
            cliente_encontrado = False
            for clientes in list_clientes:
                if cliente_selecionar == clientes['nome']:
                    cliente_encontrado = True
            if not cliente_encontrado:
                print('cliente inexistente.')
                break

            produto_cliente = str(input('qual produto o cliente gostaria :'))
            produto_encontrado = None
            for produtos in list_produtos:
                if produto_cliente == produtos['nome']:
                    produto_encontrado = produtos
                    print('verificando se há estoque disponivel ...')
                    time.sleep(2)
            if produto_encontrado is not None:
              if produto_encontrado['estoque'] >= 1:
                 print('ainda há estoque')
                 produto_encontrado['estoque'] -= 1
                 valor_final = produto_encontrado['preco']
                 data_hora = str(input('qual a data e a hora ?'))
                 vendas = {'id': vendas_id,
                          'datahora': data_hora,
                          'cliente': cliente_selecionar,
                          'item': produto_cliente,
                          'valor': valor_final
                          }
                 list_vendas.append(vendas)
                 vendas_id += 1
                 print('venda registrada!')
                 break
              else:
                print('não temos estoque deste produto ainda...')
                break

        except ValueError:
            print('apenas números!')
            break


def gerar_relatorios():
    while True:
        if not list_clientes:
            print('não há clientes no momento')
            break
        if not list_produtos:
            print('não há produtos no momento')
            break
        if not list_vendas:
            print('não há vendas no momento')
            break
        total_vendas = 0
        print('-----TODAS AS VENDAS-----')
        for vendas in list_vendas:
            print(f'ID: {vendas["id"]} | Cliente: {vendas["cliente"]} | Produto: {vendas["item"]} | Valor: R$ {vendas["valor"]:.2f} | Data: {vendas["datahora"]}')
            total_vendas += vendas['valor']
        print(f'total de todas as compras : {total_vendas:.2f} ')
        print('-----TODOS OS CLIENTES-----')
        for clientes in list_clientes:
            print(f'ID: {clientes["id"]} | Nome: {clientes["nome"]} | CPF: {clientes["cpf"]} ')
        print('-----TODOS OS PRODUTOS-----')
        for produtos in list_produtos:
            print(f'ID: {produtos["id"]} | Item: {produtos["nome"]} | Preço: {produtos["preco"]} | Estoque: {produtos["estoque"]}')
        break


carregando_arquivo(list_vendas , list_clientes , list_produtos) 
while True:
  print('-----gerenciamento de vendas de uma loja-----')
  print( ' 1 - cadastrar produtos\n 2 - cadastrar clientes\n 3 - registrar vendas\n 4 - gerar relatórios\n 5 - salvar')
  print(' 6 - SAIR')
  opcao = str(input('opção :'))
  if opcao == '1':
    cadastrar_produto()
  elif opcao == '2':
    cadastrar_cliente()
  elif opcao == '3':
    registrar_vendas()
  elif opcao == '4':
    gerar_relatorios()
  elif opcao == '5':
    salvando_arquivo(list_vendas, list_clientes , list_produtos)
  elif opcao == '6':
    print('até mais...')
    break
  else:
    print('invalido!')



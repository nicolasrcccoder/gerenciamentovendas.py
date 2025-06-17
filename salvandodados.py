import json
import time
def salvando_arquivo(list_vendas , list_clientes , list_produtos):
  while True: 
   salvarounao = str(input('deseja salvar (s / n) ?')).lower()
   if salvarounao == 's':
     print('salvando...')
     time.sleep(2)
     with open('produtos.json' , 'w') as arquivoLoja:
      (json.dump(list_produtos ,arquivoLoja, indent=4))
     with open('clientes.json' ,'w' ) as arquivoLoja:
      (json.dump(list_clientes ,arquivoLoja , indent=4 ))
     with open('vendas.json' , 'w') as arquivoLoja:
      (json.dump(list_vendas  , arquivoLoja , indent=4)) 
     print('dados salvos com sucesso!')
     break
   elif salvarounao == 'n':
     print('voltando...')
     break
   else:
     print('opção invalida!')
     continue
   
   
def carregando_arquivo(list_vendas , list_clientes , list_produtos):
  try:
    with open('produtos.json', 'r') as arquivo:
      list_produtos.clear()
      list_produtos.extend(json.load(arquivo))
  except FileNotFoundError:
    list_produtos.clear()

  try:
    with open('clientes.json', 'r') as arquivo:
      list_clientes.clear()
      list_clientes.extend(json.load(arquivo))
  except FileNotFoundError:
    list_clientes.clear()
  
  try:
   with open('vendas.json', 'r') as arquivo:
      list_vendas.clear()
      list_vendas.extend(json.load(arquivo))
  except FileNotFoundError:
    list_vendas.clear()
  print('carregado com sucesso!')

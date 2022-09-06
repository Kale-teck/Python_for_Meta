from ast import match_case


http_status = 404 #declaração da variável

match http_status: #equivale a um switch em C++
   case 200 | 201: # caractere | equivale ao operador (ou/or)
      print('Sucesso')
   case 400:
      print('Pedido errado')
   case 404:
      print('Não encontrado')
   case 500 | 501:
      print('Erro no servidor')   
   case _: #representa um valor 'padrão'
      print('Desconhecido')
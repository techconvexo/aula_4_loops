# Desafio 2  Condicionais
# Você é um Dev Jr. e precisa criar um sistema de coletas de dados.
# Utilize as condicionais, para escolher o tipo de dado e os métodos de lista
# Para:
# Mostra o dado;
# Alterar o dado;
# Coletando Dados de Experimentos
# Analisando a Soma de Dados de Vendas
# Localizar um Registro no Conjunto de Dados



print('''
SISTEMA DE COLETADA DE DADOS: 

1 Mostra o dado;
2 Alterar o dado;
3 Coletando Dados de Experimentos
4 Analisando a Soma de Dados de Vendas
5 Localizar um Registro no Conjunto de Dados
''')


lista_de_dados = [1,2,3,6]

escolha = input('Escolha a operação: ')

if escolha == '1':
   print('DADOS: ', lista_de_dados) 
elif escolha == '2':
     alterar = False
     alteracao = bool(input('Deseja alterar algo? - True '))
     if alteracao == True:
        alterar =  True
        indice = int(input('Digite o indice'))
        valor  =  input('Digite o dado')
        lista_de_dados[indice] = valor
        print('Lista atualizada:', lista_de_dados)
        
elif escolha  == '3':
    ex1 = int(input('Insira dados do experimento'))
    ex2 = int(input('Insira dados do experimento'))
    ex3 = int(input('Insira dados do experimento'))
    experimentos = []
    experimentos +=(ex1, ex2, ex3)
    lista_de_dados +=(experimentos)
    print(lista_de_dados)

elif escolha  == '4':
    soma  =  sum(lista_de_dados)
    print('Total da soma de dados: ', soma) 
elif escolha  == '5':
     dado =  int(input('BUSQUE UM DADO:'))
     if dado in lista_de_dados:
        print('Resultado da busca:existe')
         
     dado =  int(input('BUSQUE UM DADO:'))
     if dado in lista_de_dados:
             print('Resultado da busca: existe')

     else:
        print('Esse dado não existe na lista')   
else:
    print('Digite algo válido')        

              







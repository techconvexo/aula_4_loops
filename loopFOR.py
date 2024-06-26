
import random 

# '# lista = [1,2,3]
# # # iterar
# # for variavel in lista:
# #     print(variavel)
# dicionario = {
#    'key': 'valor',
#    'key2':'valor2'

# }

# multiplicador = int(input('Digite o mult'))
# for n in range(1,11) :
#     result = n * multiplicador
#     print(multiplicador, 'X', n ,'=', result)' 

# print('2x2=',2*2) 
# print('2x3=',2*3) 
# print('2x4=',2*4) 
# print('2x5=',2*5) 
# print('2x6=',2*6)  

# lista = ['ana', 'bruna', 'carol']
# for c in 'text':
#     aleatorio = random.choice(lista)
#     print(aleatorio, c)
     

c = 10
while c > 0:
    print(c)
    c = c -1

x = 0
while x <= 10:
      print(x)
      x += 2
   
aleatorio = random.randint(1,200)

n =  [x + aleatorio for n in range(1,10) ]
print(n)


while True:
    n = 20000000
    print(n)

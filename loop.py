#REPETIÇÃO (loop)

# 1 - for
str = 'Repetindo' # declara a string

for item in str: # percorre str[?] a cada volta
   print(item)

for i in range(10):
   print('repetindo...', i) # i = 0 a 9

favoritos = ['Creme caramelizado', 'Pêra maçã', 'Churros', 'Tiramisú', 'Bolo Chocolate']

for item in favoritos: #item representará cada item de favori...
   print('Eu gosto de comer ', item)#item irá até o último índice
   if item == 'Churros':
      print('Sim!, este é meu favorito', item)

# 2 - while

count = 0

while count < len(favoritos): #count < 5 (elements of favori...)
   print('Eu gosto de comer ', favoritos[count])# favoritos[?]
   count += 1#possui a mesma função do for anterior
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

x = 0
count = 0

while x < len(num_list):
   count += 1
   if num_list[x] == 36:
      print(num_list[x], ' encontrado na posição ', x,'(',x+1,')')
      break
   #else:
      #print(num_list[x], ' menor que 45')
   x += 1

print(count)
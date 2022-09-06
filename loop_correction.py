num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for x,numero in enumerate(num_list): 
   count += 1
   if numero == 36:
      print('numero encontrado em' , x)
      break

print(count)
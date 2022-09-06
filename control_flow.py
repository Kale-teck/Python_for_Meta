#controle de fluxo é usado para tomada de decisão

#CONDICIONAL (conditional)
# 1 - if
# 2 - else
# 3 - elif (else if)

conta_total = 105
desconto1 = 20
desconto2 = 40

if conta_total > 100 and conta_total < 200:
   print('A conta deu mais que 100!')
   conta_total = conta_total-desconto1
elif conta_total > 200:
   print('A conta deu mais que 200!')
   conta_total = conta_total-desconto2
else:
   print('A conta deu menos que 100! = '+str(conta_total))

print('No total a conta deu ' + str(conta_total) + ' após desconto')

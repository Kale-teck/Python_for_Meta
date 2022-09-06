myString = 'Este é um exemplo \
de string multiline declarada \
usando contra-barra para quebrar\
as linhas no código'

print(myString)

#Em python, strings se comportam como arrays
#significa que podemos acessá-la por indíces

name = 'Kalebe'
print(name[2]) #imprime a terceira letra do meu nome

#podes também acessar o tamanho de uma string

m = 'Hello,'
n = 'There!'

print(m + " " + n) #concatenação de strings
print(len(m)) #exibe o tamanho da string

print('Eu curto {1} mais que {0}'.format('Laranjas', 'Uvas'))
#os índices dirão onde quais dados aparecerão


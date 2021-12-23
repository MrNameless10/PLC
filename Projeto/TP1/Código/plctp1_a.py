"""a) imprimir o nome e o email dos concorrentes inscritos entre a 5º e a 15º posições"""

#nome\t+email\t+situação\t+data\t+tipo_inscricao\t+valor\t+tipo_pagamento\t+......
import re

inscritos = open("inscritos.txt")

min = 6 
max = 16                        

for i, linha in enumerate(inscritos):
  if (i in range(min, max+1)):
    nome = re.match(r'[^\t]+', linha)
    email = re.search(r'\t.+@[a-z.]+\t', linha) 
    if(nome and email):
      print(nome.group(), email.group())
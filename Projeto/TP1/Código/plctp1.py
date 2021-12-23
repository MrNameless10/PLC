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

"""b) imprimir o nome dos concorrentes que se inscrevem como 'Individuais' ('Individual') e são de 'Valongo'."""

import re

inscritos = open("inscritos.txt")

for linha in inscritos:
  x = re.search(r'(?:Individual)', linha)
  y = re.search(r'(?:Valongo)', linha)
  nome = re.match(r'[^\t]+', linha) #[^\t]+ -> inicio até \t
  if(x and y and nome):
    print(nome.group())

"""c) imprimir o telemóvel e a prova em que está inscrito cada concorrente cujo nome seja 'Paulo' ou 'Ricardo', desde
que seja da Vodafone."""

import re

inscritos = open("inscritos.txt")

for linha in inscritos:
  x = re.match(r'(?i:Paulo)', linha) #consideramos concorrente cujo *primeiro* nome seja 'Paulo' (PERGUNTAR AO STOR)
  y = re.match(r'(?i:Ricardo)', linha) #consideramos concorrente cujo *primeiro* nome seja 'Ricardo'

  num = re.search(r'91[0-9]{7}', linha) #consideramos Vodafone os números que começam em '91'
  prova = re.search(r'(([0-9]{2}\/*){3})(([\t ]|[A-z])+)', linha) #procuramos a data e o texto seguinte que corresponde a prova
  if((x or y) and num and prova):
    print(num.group(), prova.group(3)) #dividimos em groups e escolhemos o group do nome da prova

"""d) imprimir os 20 primeiros registos com os nomes convertidos para minúsculas."""

import re

inscritos = open("inscritos.txt")

min = 2
max = 21   

for i, linha in enumerate(inscritos):
  if(i in range(min, max+1)):
    new_line = re.sub(r'\n', '\t\n', linha) #separar o \n da informação final
    lista = re.split(r'\t', new_line)
    lista = list(dict.fromkeys(lista)) #remover informação repetida
    x = '\t'.join(lista)
    x = re.match(r'([^\t]+)(.+)', x)
    if(x):
      print(x.group(1).lower(), x.group(2))

"""e) imprimir os 20 primeiros registos num novo ficheiro de output mas em formato Json."""

import re
import json

inscritos = open("inscritos.txt")
ficheiro = open("Fjson.json", 'w')
ficheiro.write("[\n")

registo = {}
min = 2
max = 21
cats = []   
listaregs = []
j=0
for i, linha in enumerate(inscritos):
  new_line = re.sub(r'\n', '\t\n', linha) #separar o \n da informação final

  if i==1:
    cats = new_line.split('\t')
    cats.remove('\n') #remover \n das categorias
  
  if i in range(min, max+1):
    lista = re.split(r'\t', new_line)
    ficheiro.write("\t\t{\n")
    for k in range(len(cats)):
      registo[cats[k]] = lista[k]

    newd = {}
    for key,value in registo.items(): #retirar informação repetida
      if value not in newd.values():
        newd[key] = value

    listaregs.append(newd.copy())
    
    for k in range(len(list(listaregs[j].keys()))):
      categoria = list(listaregs[j].keys())[k]
      info = (list(listaregs[j].items())[k])[1]
     
      ficheiro.write("\t\t"*2 + '"' + categoria + '":' + ' "' + info + '"')
      ficheiro.write('\n' if k == (len(list(listaregs[j].keys()))-1) else ',\n')

    ficheiro.write("\t\t}\n" if i == max-1 else "\t\t},\n")

    j+=1

ficheiro.write("]")
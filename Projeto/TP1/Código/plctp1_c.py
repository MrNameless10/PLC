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
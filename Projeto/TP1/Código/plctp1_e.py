import re

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

    ficheiro.write("\t\t}\n" if i == max else "\t\t},\n")

    j+=1
ficheiro.write("]")
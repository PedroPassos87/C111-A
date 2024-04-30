# coleções
# TUPLAS ( )  ---> imutavel

#nomes = ('Goku','Vegeta','Trunks','Gohan')
#slicing de dados
#print(nomes[0])
#print(nomes[:2])
#print(nomes[1:3])
#print(nomes[-2])

#Update
#nomes[0] = 'Bulma

# LISTAS [ ]
#nomes = ['Goku','Vegeta','Trunks','Gohan']
#ADD
#nomes.append('Bulma')
#UPDATE
#nomes[0] = 'Goten'
#DELETE
#nomes.remove('Trunks') #remoçao por valor
#del nomes[2] # remocao por indice
#SELECT
#print(nomes)

# CONJUNTOS{ }  ---> nao guarda ordem dos elementos e possui elementos unicos
#nomes = {'Goku','Vegeta','Trunks','Gohan'}
#adicionar um elemento
#nomes.add('Picolo')
#remover
#nomes.remove('Gohan')
#update (nao permite update nativo)
#print(nomes)

# DICIONARIOS  ---> indices costumizaveis
pessoa = {'nome': 'Goku','idade': 42}
#ADD
#pessoa['sexo'] = 'M'
#UPDATE
#pessoa['nome'] = 'Picolo'
#DELETAR
#del pessoa['idade']
#acessando os valores do dicionario
#print(pessoa['nome'])

pessoa2 = {'nome':'Bulma','idade':40}

# COLECOES ANINHADAS
nomes = [pessoa,pessoa2]
print(nomes[1]['nome'])










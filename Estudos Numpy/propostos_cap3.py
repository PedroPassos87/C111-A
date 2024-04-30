#PROPOSTO 1
times = ['Real Madrid','Milan','Bayern de Munique', 'São Paulo', 'Barcelona']
print('3 primeiros: ',times[:3])
print('Dois ultimos: ',times[3:5])
print('Ordem alfabetica: ',sorted(times))
print('Posiçao do barcelona: ',times.index('Barcelona')+1)

#PROPOSTO 2
loja1 = {'iphone 12','iphone 13','Galaxy S3','Galaxy S21'}
loja2 = {'iphone 13','iphone 14','Galaxy S7','Galaxy S21'}
 
print('Opcoes de modelos:',loja1.union(loja2))
print('Modelos presentes nas duas lojas:',loja1.intersection(loja2))

#PROPOSTO 3
nome = input("Digite o nome do aluno: ")
media = float(input("Digite a media do aluno: "))

aluno = {'nome':nome,'media':media}

if(aluno['media'] >=60):
    print('Aluno Aprovado')
elif(aluno['media'] <30):
    print('Aluno Reprovado')
else:
    print('NP3')
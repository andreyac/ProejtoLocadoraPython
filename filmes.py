import csv

#parte das funções deste módulo foram explicados nos comentários do módulo clientes.py

def arq_existe(filename): #mesma verificação de existência de um cadastro de filmes
    existe = 1
    try:
        open(filename)
    except IOError:
        existe = 0
    return(existe)

def ler_csv(filename): #leitura de csv adaptado para a quantidade de colunas do novo dicionário
    csvfile = open(filename, 'r')
    reader = csv.reader(csvfile,delimiter=';')
    
    r = []
    
    for row in reader:
        r.append(row)
        
    dict_ant = {}
    
    for i in r:
        dict_ant.update({
            i[0] : [i[1],i[2],i[3]] #uma coluna a mais
            })
        
    return dict_ant

def pedir_dados(): #processo similar de pedido de dados
    cod = input('Insira o codigo do filme: ')
    tipo = input('1 para fita, 2 para DVD: ')
    
    while (tipo != '1') and (tipo != '2'): #aqui, após pedir 1 ou 2 como input de tipo, cria-se um loop que se repete em caso de digitação errada
        tipo = input('Apenas 1 para fita, 2 para DVD: ')
    
    if tipo == 1: #if else para converter 1/2 em Fita/DVD
        tipo = 'Fita'
    else:
        tipo = 'DVD'        
        
    nome = input('Insira o nome do filme: ')
    ano_lan = input('Insira o ano de lançamento: ')
    
    filmes = {
        cod : [tipo, nome, ano_lan]} #dicionário com código como chave e o restante como lista de valores
    
    resp = input('\nDeseja cadastrar mais um filme [s/n]? ') #mesmo processo da função anterior que pergunta
    
    while  resp == 'S' or resp =='s':#se o usuário quer cadastrar mais clientes e repete o processo enquando a resposta for S/s
        cod = input('Insira o codigo do filme: ')
        tipo = input('1 para fita, 2 para DVD: ')
    
        while (tipo != '1') and (tipo != '2'):
            tipo = input('Apenas 1 para fita, 2 para DVD: ')
    
        if tipo == 1:
            tipo = 'Fita'
        else:
            tipo = 'DVD'        
    
        nome = input('Insira o nome do filme: ')
        ano_lan = input('Insira o ano de lançamento: ')
    
        resp = input('\nDeseja cadastrar mais um filme [s/n]? ')
        
        filmes.update({
            cod : [tipo, nome, ano_lan]
            }) #faz-se o update do dicionario com os dados que o cliente cadastrou a mais
    
        
    return filmes

def mesclar_dicts(dic1,dic2): #mesma função de mesclar dicionários
    dic1.update(dic2)
    return dic1

def gravarcsv(filename, dic, existe): #função de gravar csv similar, mas adaptada para o cabeçalho e uma coluna a mais
    w = csv.writer(open(filename,'w'), delimiter=';', lineterminator='\n')
    if existe == 0:
        w.writerow(['Codigo', 'Tipo', 'Nome', 'Ano']) # <-- gravação de cabeçalho diferente caso existe == 0
    for key, val in dic.items():
        w.writerow([key,val[0],val[1],val[2]])
    return()

def main(): 
    filename = 'filmes.csv' #arquivo a ser gravado
    
    if arq_existe(filename) == 1: #aqui é feito o mesmo processo que em clientes.py
        filmes_ant = ler_csv(filename) #caso haja um cadastro anterior, ele é lido
        filmes_nov = pedir_dados() #o novo é requerido
        filmes = mesclar_dicts(filmes_ant, filmes_nov) #e os dois são mesclados
    else:
        filmes = pedir_dados() #caso não haja, trabalha-se apenas com o novo
    
    gravarcsv(filename,filmes, arq_existe(filename))  #gravação do dicionário mesclado em csv
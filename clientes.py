import csv

def arq_existe(filename): #essa função verifica se já existe um arquivo .csv chamado clientes
    existe = 1 #variável dummy que define a existência do arquivo (1 para sim e 0 para não)
    try: 
        open(filename) #aqui eu tento abrir o arquivo
    except IOError: #se houver erro de input output, não existe o arquivo
        existe = 0
    return(existe) # retorna 0 se o arquivo não existe e 1 caso contrário

def ler_csv(filename): #essa função lê o csv existente e converte seus dados para dicionário
    csvfile = open(filename, 'r') 
    reader = csv.reader(csvfile,delimiter=';') #com isso abre-se e lê-se o csv
    
    r = [] #uma lista vazia para receber as variáveis
    
    for row in reader: #esse loop faz uma iteração entre as linhas do csv
        r.append(row) #as linhas do csv são inscritas como itens da lista
        
    clientes_ant = {} #é definido um dicionário de trabalho vazio
    
    for i in r: #iteração entre os itens da lista
        clientes_ant.update( { 
            i[0] : [i[1],i[2]]
            }) #as chaves do dicionário são incritas com os valores a partir da lista
        
    return clientes_ant #retorna o dicionário de clientes anteriores, ie, antes da execução

def pedir_dados(): #essa função pede dados dos clientes para registrá-los
    cpf = input('Insira o CPF do cliente: ')
    nome = input('Insira o nome do cliente: ')
    rg = input('Insira o RG do cliente: ')
    
    
    clientes = {
        cpf : [nome, rg]
        } #forma-se um dicionário com os dados
    
    resp = input('\nDeseja cadastrar mais um cliente [s/n]?' ) #entrada para o loop de registro de clientes
    
    
    while  resp == 'S' or resp =='s': #loop que se repete cadastrando clientes enquanto o usuário desejar
        cpf = input('Insira o CPF do cliente: ')
        nome = input('Insira o nome do cliente: ')
        rg = input('Insira o RG do cliente: ')
        clientes.update({
        cpf : [nome, rg]
        })
        resp = input('\n\nDeseja cadastrar mais um cliente [s/n]? ')
    return clientes #retorna uma lista de clientes formada nessa execução

def mesclar_dicts(dic1,dic2): #apenas uma função para mesclar os dicionários de clientes antes e depois
    dic1.update(dic2)
    return dic1 #retorna um dicionário único com todos os clientes

def gravarcsv(filename, dic, existe): # essa função imprime os valores num .csv
    w = csv.writer(open(filename,'w'), delimiter=';', lineterminator='\n') #aqui é criado um csv separado por ;
    if existe == 0: #se não existe arquivo, registra-se novamente o cabeçalho
        w.writerow(['CPF', 'Nome', 'RG'])
    for key, val in dic.items(): #depois é feita uma iteração entre as chaves e valores do dicionário, registrando no csv
        w.writerow([key,val[0],val[1]])
    return() #essa função não tem retorno

def main(): #essa função é a principal, ie, executa as demais e retorna o resultado principal
    filename = 'clientes.csv' #nome do arquivo desejado
    
    if arq_existe(filename) == 1: #caso o arquivo exista anteriormente, 
        clientes_ant = ler_csv(filename) #ele é lido pela função já explicada anteriormente
        clientes_nov = pedir_dados() #o da atual execução é definido com novos dados
        clientes = mesclar_dicts(clientes_ant, clientes_nov) #os dois são mesclados
    else:
        clientes = pedir_dados() #caso não existe, apenas são pedidos dados
    
    gravarcsv(filename,clientes, arq_existe(filename)) #clientes.csv é gravado com os dicionários
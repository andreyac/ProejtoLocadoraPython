import csv
import datetime #novo repositório de funções para trabalhar com datas dos emprestimos

arq_filmes = 'filmes.csv' #aqui são definidos os nomes dos arquivos
arq_clientes = 'clientes.csv'
arq_emprestimos = 'emprestimos.csv'

emprestimos = {} #um dicionário vazio para empréstimos

def ler_filmes(filename): #função de ler cadastro de filmes, tal e qual em filmes.py
    csvfile = open(filename, 'r')
    reader = csv.reader(csvfile,delimiter=';')
    
    r = []
    
    for row in reader:
        r.append(row)
        
    dict_ant = {}
    
    for i in r:
        dict_ant.update({
            i[0] : [i[1],i[2],i[3]]
            })
        
    return dict_ant

def ler_clientes(filename): #função de ler clientes, igual à de clientes.py
    csvfile = open(filename, 'r')
    reader = csv.reader(csvfile,delimiter=';')
    
    r = []
    
    for row in reader:
        r.append(row)
        
    dict_ant = {}
    
    for i in r:
        dict_ant.update( {
            i[0] : [i[1],i[2]]
            })
        
    return dict_ant

def ler_emprestimos(filename): #função de ler empréstimos anteriores (caso haja), igual às outras acima
    csvfile = open(filename, 'r')
    reader = csv.reader(csvfile,delimiter=';')
    
    r = []
    
    for row in reader:
        r.append(row)
        
    dict_ant = {}
    
    for i in r:
        dict_ant.update( {
            i[0] : [i[1],i[2]]
            })
        
    return dict_ant

def arq_existe(filename): #função genérica de existência de arquivo, já explicada em clientes.py
    existe = 1
    try:
        open(filename)
    except IOError:
        existe = 0
    return(existe)

def emprestimoF(): #essa função registra os empréstimos
    resp = 's' #dummy de resposta para entrar no loop de registro de empréstimos (enquanto sim, registrar)
    while resp == 'S' or resp == 's':
        ver = [arq_existe(arq_clientes), arq_existe(arq_filmes)] #verificação se existe cadastro de clientes e filmes
        
        if ver == [0,0]: #caso não existe algum, é impossível prosseguir
            print('Não existe registro de clientes e de filmes.') #retorna uma mensagem de erro adequada
            return #finaliza a execução
        if ver == [1,0]:
            print('Não existe registro de filmes.')
            return
        if ver == [0,1]:
            print('Não existe registro de clientes.')
            return
        if ver == [1,1]: #caso os dois existam, pode-se prosseguir
            clientes = ler_clientes(arq_clientes) #são lidos clientes e filmes
            filmes = ler_filmes(arq_filmes)
        
        i = False #variável dummy para os loops de verificação de nome de cliente e código de filme
        while i == False:
            cli = input('Qual o nome do cliente? ') #pede-se o nome do cliente
           
            for key in clientes: #é feita uma iteração nas chaves do dicionário de cliente
                if clientes[key][0] == cli: #se a chave remete a algum valor no dicionário,
                    i = True #o cliente existe e a dummy inverte
                    break #pode-se quebrar o loop
            
            if i == False: #caso não remeta, mantém-se falso
                print('\nCliente não encontrado.') #retorna o erro e o loop pede novamente o nome do cliente
        
        i = False #a variável dummy é reciclada para ser isada com o código do filme
        while i == False : #enquanto for falsa, pede-se um código novo
            i = True #aqui ela é definida como verdadeira por default
            fil = input('Qual o codigo do filme?  ') #pede-se código do filme
            
            try:
                filmes[fil] #tenta-se acessar o código do filme no dicionário
            except KeyError: #em caso de erro de chave, ie, de a chave não existir no dicionário
                i = False #a dummy é invertida para falsa
                print('\nFilme não registrado.') #retorna-se que o filme não foi encontrado e o loop pede outro filme
        
        data_valida = False #essa dummy é definida para trabalhar com a data do empréstimo
        
        while data_valida == False: #enquanto a data for inválida (posição default), pede-se uma data válida
              
            data_valida = True
            
            data = input('Data do empréstimo (dd/mm/aaaa): ')   #aqui é requerida a data do empréstimo em formato dd/mm/aaaa
            
            try:
                dia, mes, ano = data.split('/') #aqui testa-se o valor, ie, se está no formato adequado; em caso positivo, os dados de ano, mês e dia são separados
            except ValueError: #o except é definido para caso haja erro no valor, ie, data inserida em formato inadequado
                print('\nData inválida. Por favor, digite uma data válida.') #pede-se uma nova data, até que esteja válida
                data_valida = False #muda-se a dummy para manter o loop
                
            if data_valida: #se a dummy continuar verdadeira na verificação de formato       
                try:
                    datetime.datetime(int(ano), int(mes), int(dia)) #é verificado se a data é válida com a função datetime formada de ano, mês e dia separado no split anterior 
                except ValueError: #caso haja erro de valor, a data é inválida (como dia 45/23/2020 ou 30 de fevereiro)
                    data_valida = False #a dummy é invertida para manter o loop
                    print('Data inválida. Por favor, digite uma data válida.') #pede-se novamente uma data válida
            emprestimos.update({
                fil : [cli, data] #feitas as verificações, é formado um dicionário com os dados de código, nome e data
                })
        resp = input('Deseja cadastrar mais um empréstimo? [s/n] ') #variável resp para o loop de cadastrar novos empréstimos
        while (resp != 'S') and (resp != 's') and (resp != 'N') and (resp != 'n'):
            resp = input('Deseja cadastrar mais um empréstimo? >>[s/n]<<  ')
    return emprestimos #retorna um dicionário de empréstimos

def gravarcsv(filename, dic, existe): #função de gravar csv igual às outras
    w = csv.writer(open(filename,'w'), delimiter=';', lineterminator='\n')
    if existe == 0:
        w.writerow(['Codigo', 'Nome', 'Data']) #com adaptação do cabeçalho para empréstimos
    for key, val in dic.items():
        w.writerow([key,val[0],val[1]])
    return()

def main(): #função main definida igual às outras
    emprestimos_nov = emprestimoF() #os novos empréstimos são frutos da execução da função que pede dados
    emprestimos = {} #um dicionário de empréstimos é aberto
    
    if arq_existe(arq_emprestimos) == 1: #se existe um arquivo de empréstimos anterior, é mesclado com o novo
        emprestimos_ant = ler_emprestimos(arq_emprestimos)
        emprestimos.update(emprestimos_ant)
        emprestimos.update(emprestimos_nov)
    gravarcsv(arq_emprestimos,emprestimos, arq_existe(arq_emprestimos)) #tudo é escrito em um csv
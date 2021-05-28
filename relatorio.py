import csv
import datetime
from tabulate import tabulate #aqui é importada a função tabulate para apresentação do relatório

arq_filmes = 'filmes.csv'
arq_clientes = 'clientes.csv'
arq_emprestimos = 'emprestimos.csv'

def ler_filmes(filename): #as funções de leitura aqui são similares: filmes, clientes e empréstimos
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

def ler_clientes(filename):
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

def ler_emprestimos(filename):
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

def arq_existe(filename): #função de verificação de existência de arquivo, como de praxe
    existe = True
    try:
        open(filename)
    except IOError:
        existe = False
    return(existe)

def main(): #agora se inicia a main e a principal parte deste script
    ver = arq_existe(arq_emprestimos) #primeiramente, é necessário verificar se há arquivo de empréstimo
    
    if ver == False: #caso não haja, a função é encerrada, pois não há como gerar relatório sem empréstimos
        print('\nNão há empréstimos registrados.')
        return
        
    clientes = ler_clientes(arq_clientes) #em caso contrário, são lidos clientes, filmes e empréstimos
    filmes = ler_filmes(arq_filmes)
    emprestimos = ler_emprestimos(arq_emprestimos)
    
    del clientes['CPF'] #são deletados os cabeçalhos de cada dicionário
    del filmes['Codigo']
    del emprestimos['Codigo']
    
    relatorio = [] #aqui é aberta a lista a partir de que será gerado o relatório
        
    for key in emprestimos: #iteração entre os empréstimos
        titulo = filmes[key][1]  #são tomados os títulos dos filmes emprestados de cada item
        emp = emprestimos[key][1] #a data é tomada em formato de string, como está no dicionário
        data = datetime.datetime.strptime(emp, '%d/%m/%Y') #essa string é convertida em data
        data = data.date() #são eliminados os valores de horário
        hoje = datetime.date.today() #é definida uma variável com o dia de hoje
        delta = hoje - data #o delta é a variação de dias entre o empréstimo e o dia atual
        if delta.days > 7: #se o delta for maior que 7, o empréstimo está atrasado
            sit = 'Atrasado' #a stiação recebe o valor 'Atrasado'
            dias = delta.days-7 #os dias de atraso receber o valor de delta - 7
        else: #caso o delta não seja maior que 7
            sit = 'Em dia' #situação recebe o valor 'Em dia'
            dias = '-' #não há dias de atraso a serem registrados
        for item in clientes: #aqui começa uma iteração entre os clientes para buscar os nome registrado em cada empréstimo
            if clientes[item][0] == emprestimos[key][0]: #caso o nome associado à chave seja o mesmo dado no empréstimo
                cpf = item #cpf é o item atual do dicionário de clientes
                nome = clientes[item][0] #nome é o primeiro valor do item
                break #pode-se quebrar o loop
        relatorio.append((cpf, nome, titulo, emp, sit, dias)) #os valores gerados são inseridos em uma lista de listas
    
    print(tabulate(relatorio, headers = ['CPF', 'Nome', 'Título', 'Empréstimo', 'Situação', 'Dias'])) #é usada a função tabulate para gerar uma tabela legível com base na lista do relatório e com cabeçalho
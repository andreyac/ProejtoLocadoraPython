import clientes
import filmes
import emprestimos
import relatorio

k = 's' #variável dummy de repetição do loop do programa

while k == 's' or k == 'S': #enquanto o cliente responder sim

    print('Segue a lista de funcionalidades:') # a lista de funcionalidades é apresentada
    print('\n(1) Cadastrar clientes \n(2) Cadastrar filmes \n(3) Registrar empréstimo\n(4) Relatório de atrasos')
    ativ = input('O que você deseja fazer? ') #input de qual atividade o usuário deseja 
    
    while (ativ!='1') and (ativ!='2') and (ativ!='3') and (ativ!='4'): #loop caso ele responda valores inválidos
        ativ = input('Por favor, insira uma resposta válida (1,2,3 ou 4): ')
        print('\n\n')
        
    if ativ == '1': #atividade um chama o script clientes
        clientes.main() #execução do script
    if ativ == '2': #assim por diante
        filmes.main()
    if ativ == '3':
        emprestimos.main()
    if ativ == '4':
        relatorio.main()
        
    input('Deseja realizar outra operação [s/n]? ') #o usuário é questionado se deseja realizar outra operação
    while (k != 's') and (k != 'S') and (k != 'n') and (k != 'N') :
        input('Deseja realizar outra operação [s/n]? ')
        
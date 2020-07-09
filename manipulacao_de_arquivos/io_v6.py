with open('pessoas.csv') as arquivo:
    '''
    O open pode abrir para escrever
    Com a vírgula se acessa os diferentes modos do open, sendo o padrão ler
    "w" é o modo de escrita (write)
    '''
    with open('pessoas.txt', 'w') as saida:

        for registro in arquivo:
            pessoa = registro.strip().split(',')
            '''
            A função print pode imprimir em diversos lugares
            Por padrão imprime no console
            mas pode imprimir por exemplo em um arquivo escolhido
            aqui no caso escolhido a saida, pessoas.txt
            '''
            print('Nome: {}, Idade: {}\n'.format(*pessoa), file=saida, end='')

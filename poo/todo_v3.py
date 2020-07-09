from datetime import datetime
'''
Esse import trás as datas formatadas
'''


class Projeto:
    '''
    Essa classe cria um projeto, onde nele haverão diversas tarefas
    e funcionalidades
    '''
    def __init__(self, nome):
        '''
        A inicialização ocorre com o nome
        e ao mesmo tempo inicializa uma lista de tarefas vazia
        '''
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        '''
        Essa função define o que pode ser iterado dentro da classe
        Assim, não tem mais necessidade de
        sempre que for necessária uma iteração
        definir a propriedade que deve ser iterada

        Isso facilita escrever o código
        Substituindo, por exemplo, em um objeto chamado de casa

        for _ in casa.tarefas: por for _ in casa:

        Isso é conhecido como ducktype
        "Se voa como um pato, se anda como um pato, se nada como um pato...
        É um pato"
        Se esse objeto é iterativo então pode ser iterado
        '''
        return self.tarefas.__iter__()

    def add(self, descricao):
        '''
        O método add pega a descrição desejada para uma tarefa
        e dentro da lista de tarefas deste objeto
        cria um novo objeto Tarefa()
        '''
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        '''
        Esse método retorna um lista comprehension
        que basicamente retorna uma lista de tarefas não feitas
        caso elas tenham o tarefa.feito() = false
        '''
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        '''
        Nesse método ao encontrar dentro dessa lista de tarefas
        a que tenha descrição desejada
        ele retorna o objeto dela (o conteúdo da instância)
        '''
        # Possível IndexError
        return next((tarefa for tarefa in self.tarefas
                     if tarefa.descricao == descricao))

    def __str__(self):
        '''
        Retorna quantas tarefas ainda estão pendentes na lista
        '''
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    '''
    Essa classe cria uma Tarefa, que terá uma descrição
    um momento de criação
    E uma propriedade booleana dizendo se foi feita ou não
    '''
    def __init__(self, descricao):
        '''
        Essa inicialização ocorre com a descrição
        e cria por padrão as outras duas propriedades
        '''
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        '''
        Esse método somente altera o valor de self.feito
        '''
        self.feito = True

    def __str__(self):
        '''
        Retorna a decrição da tarefa
        concatenando com Concluída somente se self.feito for True
        caso contrário contatena com nada, ou ""
        '''
        return self.descricao + (' (Concluída)' if self.feito else '')


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')

    print(casa)


if __name__ == '__main__':
    main()

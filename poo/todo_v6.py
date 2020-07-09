from datetime import datetime, timedelta
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
        '''
        return self.tarefas.__iter__()

    def _add_tarefa(self, tarefa, **kwargs):
        '''
        O método _add_tarefa() adiciona uma tarefa na lista de tarefas
        indepentente do tipo de tarefa
        Tarefa() ou TarefaRecorrente()

        Este é um método privado, começando com _
        pertencente somente a classe Projeto

        Por convenção métodos privados começam com _
        e métodos públicos são os normais

        Essa função possui os argumento nomeados para ser mais fácil de chamar
        pois assim se assemelha com a função _add_nova_tarefa()
        '''
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        '''
        Essa função _add_nova_tarefa(), tem a mesma cara da função
        _add_tarefa() para que seja mais uniforme a sua chamada

        Caso seja inserido um parâmetro nomeado
        se ele for "vencimento", ela insere como parâmetro
        caso a função .get() não encontre no dicionário
        ela retorna None
        '''
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        '''
        Este método agora será o que chamamos de sobrecarregado
        dependendo do tipo de chamada

        No caso, tanto faz se é uma Tarefa() ou TarefaRecorrente()
        se extiver no contexto de Tarefa(), ele irá adicionar a tarefa
        visto que TarefaRecorrente() é uma subtarefa de Tarefa()

        Caso contrário, ele irá criar uma nova tarefa
        usando tarefa como uma descrição

        É um pseudo overload
        '''
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        '''
        Aqui estou criando o parâmetro de vencimento como dicionário
        caso ele tenha sido inserido na chamada
        '''
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        '''
        Esse método retorna um list comprehension
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
    um momento de criação e seu vencimento
    E uma propriedade booleana dizendo se foi feita ou não
    '''
    def __init__(self, descricao, vencimento=None):
        '''
        Essa inicialização ocorre com a descrição
        e cria por padrão as outras duas propriedades
        '''
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        '''
        Esse método somente altera o valor de self.feito
        '''
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() >= self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dia(s))')
        return f'{self.descricao} ' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    '''
    Essa subclasse de Tarefa que define uma tarefa que ocorre com recorrência

    Ou seja, as caracteristicas aqui iniciadas
    pertencem a TarefaRecorrente
    mas são herdadas da classe Tarefa
    '''
    def __init__(self, descricao, vencimento, dias=7):
        '''
        Aqui vamos usar o super() para chamar o construtor da classe mãe
        somente adicionando dai o parâmetro de dia
        '''
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        '''
        Aqui vamos chamar o método concluir() da classe mãe
        e já adicionar um novo vencimento, advindo da recorrência
        '''
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    casa.add(TarefaRecorrente('Trocar lençóis', datetime.now(), 7))
    casa.add(casa.procurar('Trocar lençóis').concluir())
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')

    print(casa)

    compras = Projeto('Compras no Super')
    compras.add('Carne', datetime(2020, 4, 17, 1))
    compras.add('Refri', datetime(2020, 4, 14))
    compras.add('Banana')

    comprar_bananas = compras.procurar('Banana')
    comprar_bananas.concluir()
    print(compras)

    for compra in compras:
        print(f'- {compra}')


if __name__ == '__main__':
    main()

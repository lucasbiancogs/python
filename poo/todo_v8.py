from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception):
    '''
    TarefaNaoEncontrada será uma subclasse de Exception
    que é a classe mãe das excessões.
    '''
    pass


class Projeto:
    '''
    Cria um projeto que terá nome e uma lista de tarefas
    '''
    def __init__(self, nome):
        '''
        Esse é um método construtor que inicializa a classe.
        '''
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        '''
        Esse método define o que deve ser iterado na classe
        '''
        return self.tarefas.__iter__()

    def __iadd__(self, tarefa):
        '''
        Esse método sobrecarrega o operador "+="
        '''
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        '''
        Adiciona uma tarefa na lista de tarefas
        indepentente do tipo de tarefa.
        '''
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        '''
        Cria uma nova tarefa.

        Caso seja inserido um parâmetro nomeado:
        se ele for "vencimento", ela insere como parâmetro.
        '''
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        '''
        Caso esteja no contexto de Tarefa() ou TarefaRecorrente()
        adicionara a tarefa à lista.

        Caso contrário, ele irá criar uma nova tarefa
        usando tarefa como uma descrição.
        '''
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        '''
        Aqui é criando o parâmetro de vencimento como dicionário
        caso ele tenha sido inserido na chamada
        '''
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        '''
        Retorna uma lista de tarefas não feitas.
        '''
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        '''
        Retorna o objeto ao encontrar dentro dessa lista de tarefas
        a que tenha descrição desejada.

        Se houver um problema de índice a função irá retornar
        qual foi o tipo de erro.
        '''
        try:
            '''
            Como visto anteriormente, o bloco try é um bloco perigoso
            onde pode haver algum problema de código.
            No caso aqui um possível IndexError.

            Ele tenta rodar, se não conseguir entra na exceção.
            '''
            return [tarefa for tarefa in self.tarefas
                    if tarefa.descricao == descricao][0]
        except IndexError as erro:
            '''
            Se o erro encontrado em try: for do tipo IndexError
            a exceção chama a classe TarefaNaoEncontrada
            com erro como input em forma de string
            porque é assim que a classe Exception
            interpreta os parâmetros.
            '''
            raise TarefaNaoEncontrada(str(erro))

    def __str__(self):
        '''
        Retorna um log de quantas tarefas ainda estão pendentes na lista.
        '''
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    '''
    Cria uma Tarefa que terá uma descrição,
    um momento de criação, seu vencimento
    e uma propriedade booleana dizendo se foi feita ou não
    '''
    def __init__(self, descricao, vencimento=None):
        '''
        Esse é um método construtor que inicializa a classe.
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
        '''
        Retorna um log da classe dependendo do seu estado:
        concluída, vencida ou que vence em x dia(s).
        '''
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
    Define uma tarefa que ocorre com recorrência.
    '''
    def __init__(self, descricao, vencimento, dias=7):
        '''
        Esse é um método construtor que inicializa a classe.
        '''
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        '''
        Conclui, cria e adiciona um dono a essas tarefas
        e retorna um novo objeto com um novo vencimento.
        '''
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(self.descricao,
                                       novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    casa += TarefaRecorrente('Trocar lençóis', datetime.now(), 7)
    casa.procurar('Trocar lençóis').concluir()
    print(casa)

    try:
        casa.procurar('Lavar prato - ERRO').concluir()
    except TarefaNaoEncontrada as erro:
        print(f'A causa do erro foi: {str(erro)}')

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

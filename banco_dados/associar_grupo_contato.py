from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

contato_grupo = {
    'Joel': 'Futebol',
    'Rafael': 'Trabalho',
    'Joana': 'Trabalho',
    'Gabriel': 'Faculdade',
    'Nairana': 'Trabalho',
    'Xavier': 'Futebol',
    'Pedro': 'Faculdade',
    'Lucas': 'Futebol'
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        '''
        Aqui ele seleciona no grupo, a partir da descrição o id
        e insere no cursor
        depois coloca esse valor em grupo_id
        ai atualiza o contato onde estive o contato com aquele nome
        '''
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Contatos associados!')

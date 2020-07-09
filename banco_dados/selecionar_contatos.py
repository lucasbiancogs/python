from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'SELECT * FROM contatos'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        '''
        Para uma tabela com muitos dados esse tipo de consulta
        gerará problemas de desempenho
        '''
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        '''
        o cursor.fetchall irá retornar uma lista com listas em cada índice
        cada lista será uma linha e cada índice dessa lista um valor de coluna
        só é preciso saber qual é qual
        nessa tabela será
        nome - tel - id
        O :3d indica quanto daquele dado será apresentado para int
        E :10s para strings ou caracteres, não sei

        '''
        for contato in contatos:
            print(f'{contato[2]:3d} - {contato[0]:10s}\
 Telefone: {contato[1]:10s}')

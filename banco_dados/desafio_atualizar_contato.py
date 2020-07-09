from bd import nova_conexao
from mysql.connector import ProgrammingError

sql = '''
UPDATE contatos
SET
    nome = %s,
    tel = %s
WHERE id = 19
'''
args = ('Lucas', '99940-1801')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) atualizado(s).')

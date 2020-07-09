from mysql.connector import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Joel', '99654-6754'),
    ('Rafael', '99544-2354'),
    ('Joana', '99654-6344'),
    ('Gabriel', '94434-6754'),
    ('Nairana', '95554-6754'),
    ('Lucas', '96564-6744'),
    ('Xavier', '96754-7654'),
    ('Pedro', '99244-6754'),
    ('Matheus', '99622-4554')
)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros.')

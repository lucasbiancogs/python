from bd import nova_conexao
from mysql.connector import ProgrammingError

sql = "INSERT INTO grupos (descricao) VALUES (%s)"
args = (
    ('Futebol',),
    ('Faculdade',),
    ('Trabalho',)
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')

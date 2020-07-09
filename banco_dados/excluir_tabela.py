from bd import nova_conexao
from mysql.connector import ProgrammingError

excluir_tabela = """
    DROP TABLE IF EXISTS emails
"""

# DROPY TABLE email
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(excluir_tabela)
        print('Tabela excluída.')
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')

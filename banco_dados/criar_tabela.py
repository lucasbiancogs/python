from bd import nova_conexao
from mysql.connector import ProgrammingError

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos(
        nome VARCHAR(50),
        tel VARCHAR(40)
    )
"""

tabela_email = """
    CREATE TABLE IF NOT EXISTS emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""

'''
Criando as novas tabelas

O tratamento de exceção deve ser realizado para conexões fora do with
ou até mesmo dentro da função nova_conexao()

Já tratamentos de código mal escrito, problemas de SQL
são trabados dentro do bloco with:
'''
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contatos)
        print('Tabela criada.')
        cursor.execute(tabela_email)
        print(f'Tabela criada.')
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')

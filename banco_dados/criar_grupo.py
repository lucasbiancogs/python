from bd import nova_conexao
from mysql.connector import ProgrammingError

criar_tabela_grupo = """
    CREATE TABLE IF NOT EXISTS grupos(
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(30)
    )
"""

alterar_tabela_contato_1 = """
    ALTER TABLE contatos ADD grupo_id INT
"""

alterar_tabela_contato_2 = """
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
    REFERENCES grupos(id)
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
        cursor.execute(criar_tabela_grupo)
        print('Tabela criada.')
        cursor.execute(alterar_tabela_contato_1)
        print(f'Tabela alterada.')
        cursor.execute(alterar_tabela_contato_2)
        print(f'Tabela alterada.')
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')

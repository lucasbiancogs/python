from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = """
    SELECT
    grupos.descricao AS grupo,
    contatos.nome AS nome
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, nome
    """

with nova_conexao() as conexao:
    '''
    O parâmetro nomeado dictionary=True é uma funcionalidade mais usual do sql
    ela faz com que os retornos de cursos não seja tuplas
    e sim dicionários
    '''
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro : {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["nome"]}')

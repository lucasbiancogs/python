from mysql.connector import connect, ProgrammingError
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='6dddebcn',
    database='agenda'
)


@contextmanager
def nova_conexao():
    '''
    Essa função estabelece uma nova conexão e deve ser usada com o block with:
    assim, enquanto usada estara em yield: o retorno parcial
    quando sairmos do bloco with ela irá para diretamente para o finally
    que irá fechar a conexão com o banco de dados e poupar recurso do sistema

    O decorator context manager
    '''
    conexao = connect(**parametros)
    try:
        if conexao.is_connected:
            print('Conectado!')
        yield conexao
    except ProgrammingError as e:
        print(f'Erro de conexão: {e.msg}')
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()
            print('Conexão encerrada!')

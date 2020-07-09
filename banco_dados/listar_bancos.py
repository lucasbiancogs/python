from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    password='6dddebcn'
)

cursor = conexao.cursor()

'''
Coloquei escrito desse jeito pq o MySQL não é case sensitive
'''
cursor.execute('Show Databases')

for i, database in enumerate(cursor, start=1):
    '''
    A resposta de cursos é uma listas, onde só o primeiro termo existe
    por isso só irá aceitar database[0]
    '''
    print(f'Banco de dados {i}: {database[0]}')

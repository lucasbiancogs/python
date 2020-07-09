from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    password='6dddebcn'
)

cursor = conexao.cursor()
# CREATE DATAABASE IF NOT EXISTS
cursor.execute('CREATE DATABASE agenda')

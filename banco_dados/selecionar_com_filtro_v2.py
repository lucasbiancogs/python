from bd import nova_conexao
'''
Esse tipo de abordagem trás todos que tiverem 'a' no nome
abordagem do sql
'''
sql = "SELECT * FROM contatos WHERE nome like '%ca%'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for dado in cursor:
        print(dado)

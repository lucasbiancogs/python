from bd import nova_conexao

sql = "SELECT * FROM contatos WHERE tel = '99940-1801'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for dado in cursor:
        print(dado)

from bd import nova_conexao
'''
Esse tipo de abordagem é a mais segura, pois permite ao python
proteger seus dados de ataques como SQL injection
que é alguem injetar código de sql como string
e roubar ou alterar seus dados
A segurança se encontra em usar os args como parâmetro da string

Se quiser usar os args como parâmetro da string os percetuais
tem de estar na string de args e não na string de sql, por exeplo
sql = "SELECT * FROM contatos WHERE nome like %%s%"
ira retornar nomes com 's'

Outra regra, % no começo pega os dados com a letra referente no fim
% no final pega os dados com a letra referente no começo
% dos dois lados pega dado com aquela letra em qualquer lugar
'''
sql = "SELECT * FROM contatos WHERE nome like %s"

with nova_conexao() as conexao:
    nome = input('Contato a localizar: ')
    args = (f'%{nome}%',)

    cursor = conexao.cursor()
    cursor.execute(sql, args)

    for dado in cursor:
        print(dado)

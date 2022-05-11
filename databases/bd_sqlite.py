"""
https://sqlitebrowser.org/dl/
"""

import sqlite3

conexao = sqlite3.connect('basedados_sqlite.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# INSERT

# SQL INJECTION
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Matheus Ariel", 95.95)')
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Josúe Santos", 60.00)')

# COM PARAMS (MODO CERTO)
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Marcio Santos', 55.50))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Joãozino', 'peso': 80})
# cursor.execute('INSERT INTO clientes VALUES (:id,:nome, :peso)', {'id': None, 'nome': 'Lucas Santinho', 'peso': 74})
conexao.commit()

# SELECT

cursor.execute('SELECT * FROM clientes')
dados = cursor.fetchall()

for dado in dados:
    print(dado)
    # print(f'ID: {dado[0]}')
    # print(f'Nome: {dado[1]}')
    # print(f'Peso: {dado[2]}')
    id_, nome, peso = dado
    print(f'ID: {id_}')
    print(f'Nome: {nome}')
    print(f'Peso: {peso}')

    print('\n')

# UPDATE

# cursor.execute('UPDATE clientes SET nome =:nome WHERE id =:id', {'nome': 'Ivan Santos', 'id': 2})
# cursor.execute('UPDATE clientes SET nome =:nome WHERE id =:id', {'nome': 'Paulo Mendes', 'id': 4})
conexao.commit()

# DELETE

# cursor.execute('DELETE FROM clientes WHERE id =:id', {'id': 2})
conexao.commit()

cursor.execute('SELECT nome, peso FROM clientes WHERE peso <= :peso', {'peso': 60})
dados = cursor.fetchall()

print(dados)

cursor.close()
conexao.close()

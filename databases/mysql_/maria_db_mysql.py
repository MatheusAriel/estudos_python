import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        print('conexao fechada')
        conexao.close()


# INSERE UM REGISTRO NA BASE DE DADOS
"""with conecta() as conexao:
    with conexao.cursor() as cursor:
        query = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
                '(%s,%s,%s,%s)'
        cursor.execute(query, ('Mariel', 'Swaznegger', 59,350))
        conexao.commit()"""

# INSERE MULTIPLOS REGISTROS NA BASE DE DADOS, DE UMA ÚNICA VEZ
"""with conecta() as conexao:
    with conexao.cursor() as cursor:
        query = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
                '(%s,%s,%s,%s)'
        dados = [
            ('Anderson', 'Santos', 57, 112),
            ('Muriel', 'Figuereido', 59, 150),
            ('Josué', 'JKosh', 110, 60),
        ]

        cursor.executemany(query, dados)
        conexao.commit()"""

# DELETA UM REGISTRO DA BASE DE DADOS
"""with conecta() as conexao:
    with conexao.cursor() as cursor:
        query = 'DELETE FROM clientes where id = %s'
        
        cursor.execute(query, (6,))
        conexao.commit()"""

# DELETA QTD DETERMINADA DE REGISTROS
"""with conecta() as conexao:
    with conexao.cursor() as cursor:
        query = 'DELETE FROM clientes where id IN (%s, %s, %s)'

        cursor.execute(query, (6, 7, 8))
        conexao.commit()"""

# DELETA REGISTROS EM UM RANGE
"""with conecta() as conexao:
    with conexao.cursor() as cursor:
        query = 'DELETE FROM clientes where id BETWEEN %s AND %s'

        cursor.execute(query, (6, 8))
        conexao.commit()"""

# ATUALIZA UM REGISTO DA BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        query = 'UPDATE clientes SET nome=%s where id=%s'

        cursor.execute(query, ('Roberval', 4))
        conexao.commit()

# LISTA REGISTROS DA BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY nome ASC LIMIT 100')
        results = cursor.fetchall()

        for result in results:
            for k, v in result.items():
                print(f'{k}: {v}')

            print()

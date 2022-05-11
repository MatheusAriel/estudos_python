import sqlite3


class Agenda:

    def __init__(self, arquivo):
        self.connector = sqlite3.connect(arquivo)
        self.cursor = self.connector.cursor()

    def inserir(self, nome, telefone):
        query = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?,?)'
        self.cursor.execute(query, (nome, telefone))
        self.connector.commit()

    def editar(self, nome, telefone, id):
        query = 'UPDATE OR IGNORE agenda SET nome=?, telefone=?  WHERE id=?'
        self.cursor.execute(query, (nome, telefone, id))
        self.connector.commit()

    def excluir(self, id):
        query = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(query, (id,))
        self.connector.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda ORDER BY nome ASC')
        result = self.cursor.fetchall()

        for r in result:
            print(f'ID: {r[0]}')
            print(f'NOME: {r[1]}')
            print(f'TELEFONE: {r[2]}')
            print('\n', '*' * 80, '\n')

    def buscar(self, txt):
        query = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(query, (f'%{txt}%',))
        result = self.cursor.fetchall()

        for r in result:
            print(f'ID: {r[0]}')
            print(f'NOME: {r[1]}')
            print(f'TELEFONE: {r[2]}')
            print('\n', '*' * 80, '\n')

    def fechar(self):
        self.cursor.close()
        self.connector.close()


if __name__ == '__main__':
    agenda = Agenda('agenda.db')
    agenda.inserir('Matheus', '1198256852')
    agenda.inserir('Matheus', '1256969989')
    agenda.inserir('Fabriicio', '15889897')
    # agenda.editar('Marcos', '1256969989', 2)
    agenda.inserir('Matheus Ariel', '7854568956')

    # agenda.excluir(5)
    #agenda.listar()
    print('\n\n\n')
    agenda.buscar('Ma')

    agenda.fechar()

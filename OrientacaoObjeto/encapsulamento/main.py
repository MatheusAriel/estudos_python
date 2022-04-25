"""
_nomevarivale:  entende-se q é privado, não utilizar por boa pratica (private, protected) mas eh public pois pode
editar e acessar

__nomevarivel: proibe metodo ou atributo de ser usado fora da classe - pode ser acessado atraves de:
_NOMEDACLASSE__nomeatributo

ambos tmb funcionam com metódos

"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        print(f'\n{self.__dados}\n')
        for id, nome in self.__dados['clientes'].items():
            print(f'ID: {id} - Nome: {nome}')

    def apagar_cliente(self, id):
        try:
            del self.__dados['clientes'][id]
        except:
            pass


bd = BaseDeDados()
bd.inserir_cliente(1, 'Matheus')
bd.inserir_cliente(2, 'Gabriel')
bd.inserir_cliente(4, 'João')

bd.__dados = 'HAHA'
print(bd.__dados)  # aqui criou outra variavel da instancia
print(bd.__dict__)
print(bd._BaseDeDados__dados)

# bd.apagar_cliente(2)
bd.listar_clientes()
print()
# atraves do get
print(bd.dados)

# erro pois n existe um setter
# bd.dados = 'HAHAH'

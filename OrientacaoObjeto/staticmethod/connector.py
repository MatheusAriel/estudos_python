"""
1 - Se precisar usar a palavra self dentro do método: tem de ser método de instância
2 - Se precisar usar a classe em si dentro do método (cls) tem de ser método de classe
3 - Se não precisar nem de self e nem de cls dentro do método, pode ser um método estático.
"""


class Connector:
    def __init__(self, host, usuario, senha):
        self.host = host
        self.usuario = usuario
        self.senha = senha

    def conectar(self):
        print(f'Conectando em {self.host} com {self.usuario}')

    @classmethod
    def sem_host(cls, usuario, senha):
        return cls('127.0.0.1', usuario, senha)

    @staticmethod
    def sem_host_estatico(usuario, senha):
        return Connector('127.0.0.1', usuario, senha)

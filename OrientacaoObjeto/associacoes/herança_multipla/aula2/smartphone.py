from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if (not self._ligado):
            msg = f'{self._nome} não está ligado'
            print(msg)
            self.log_error(msg)
            return

        if (self._conectado):
            msg = f'{self._nome} já está conectado'
            print(msg)
            self.log_error(msg)
            return

        msg = f'{self._nome} conectado com sucesso !'
        print(msg)
        self.log_info(msg)
        self._conectado = True

    def desconectar(self):
        if (not self._ligado):
            msg = f'{self._nome} não está ligado'
            print(msg)
            self.log_error(msg)
            return

        if (not self._conectado):
            msg = f'{self._nome} já está desconectado'
            print(msg)
            self.log_error(msg)
            return

        msg = f'{self._nome} desconectado com sucesso !'
        print(msg)
        self.log_info(msg)
        self._conectado = False

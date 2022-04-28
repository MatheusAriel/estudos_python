from abc import ABC, abstractclassmethod
import re


class Pessoa(ABC):

    def __init__(self, nome: str, idade: int, documento: str):
        self.nome = nome
        self._idade = idade
        self.documento = documento

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome.upper()

    @property
    def idade(self) -> int:
        return self._idade

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, documento):
        self._documento = re.sub(r'[^0-9]', '', documento)

    @abstractclassmethod
    def exibir_dados_clientes(self) -> None:
        pass

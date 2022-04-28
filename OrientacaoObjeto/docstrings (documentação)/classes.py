"""Descrição ráida e simples sobre a classe

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ultricies dui eu enim efficitur cursus. Cras sit amet
fermentum dui. Pellentesque vitae posuere felis. Sed convallis dui sit amet mattis egestas. Etiam ut eleifend orci. Ut
efficitur dolor ligula, ac volutpat turpis pulvinar quis. Etiam nec elementum nunc. Nunc ligula tellus, finibus a
rutrum ut, feugiat ac lectus. Nullam cursus efficitur est, aliquam semper ligula sodales quis. Nullam a auctor purus.
Sed bibendum vulputate tristique. Proin urna mauris, dignissim ut tempor non, maximus nec mi.

REFERENTE AO MÓDULO ISSO TUDO

"""


class MinhaClasse:
    """Documentação normal
        conforme qualquer outra documentação que voce tenha usado anteriormente
    """

    atributo_1 = 100
    atributo_2 = 'Valor'

    def __init__(self, texto):
        """Inicializador da classe minhaclasse

        :param texto: o texto da classe
        :type texto: str
        """
        self.texto = texto
        self.exibe_texto(texto)

    @staticmethod
    def exibe_texto(texto):
        """Método que exibe um texto de 100 caracteres na tela

            :param texto: um texto de no max 100 caracteres
            :type texto:str

            :return: o texto de no max 100 caracteres
            :rtype: str

            :raises ValueError: se o texto tiver mais q 100 caracteres
            :raises: TypeError: Se o texto não for uma string
        """

        if not isinstance(texto, str):
            raise TypeError("O texto precisa ser uma string")

        if len(texto) > 100:
            raise ValueError("O texto precisa ter 100 caracteres no máximo")

        return texto

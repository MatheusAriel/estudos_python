"""
try:
    import os, sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except ImportError:
    raise
"""

from formata.preco import real


def aumento(preco, porcentagem, formata=False):
    preco_calculado = preco + (preco * (porcentagem / 100))
    return preco_calculado if not formata else real(preco_calculado)


def reducao(preco, porcentagem, formata=False):
    preco_calculado = preco - (preco * (porcentagem / 100))
    return preco_calculado if not formata else real(preco_calculado)

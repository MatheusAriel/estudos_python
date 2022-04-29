import re


class CalculadoraIpv64:
    def __init__(self, ip: str, mascara=None, prefixo=None):

        if mascara is None and prefixo is None:
            raise ValueError('Precisa enviar máscara ou prefixo')

        if mascara and prefixo:
            raise ValueError('Precisa enviar máscara ou prefixo, não ambos.')

        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._set_broadcast()
        self._set_rede()

    @property
    def numeros_ips(self):
        # 2³²
        return 2 ** (32 - self.prefixo)

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def rede(self):
        return self._rede

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        if self._prefixo is None:
            return None
        return self._prefixo

    @ip.setter
    def ip(self, ip):
        if not self._valida_ip(ip):
            raise ValueError('Ip inválido')
        self._ip = ip
        self._ip_bin = self._ip_to_bin(self._ip)

    @mascara.setter
    def mascara(self, mascara):
        if not mascara:
            return

        if not self._valida_ip(mascara):
            raise ValueError('Máscara inválida.')

        self._mascara = mascara
        self._mascara_bin = self._ip_to_bin(mascara)

        if not hasattr(self, 'prefixo') or self.prefixo is None:
            self.prefixo = self._mascara_bin.count('1')

    @prefixo.setter
    def prefixo(self, prefixo):
        if not prefixo:
            return

        try:
            prefixo = int(prefixo)
        except:
            raise TypeError('Prefixo precisa ser um número inteiro')

        if prefixo > 32:
            raise TypeError('Prefixo precisa ter no máximo tamanho de 32 bits')

        self._prefixo = prefixo
        self._mascara_bin = (prefixo * '1').ljust(32, '0')
        # print(self._macara_bin)

        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$')

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_binarios = [bin(int(x))[2:].zfill(8) for x in blocos]

        # print(blocos)
        # print(blocos_binarios)
        # print(''.join(blocos_binarios))

        return ''.join(blocos_binarios)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[x:n + x], 2)) for x in range(0, 32, n)]
        # print('.'.join(blocos))
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.prefixo
        self._set_broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._set_broadcast_bin)
        # print(self._broadcast)
        return self._broadcast

    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self._set_rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._set_rede_bin)
        # print(self._rede)
        return self._rede


if __name__ == '__main__':
    ipv64 = CalculadoraIpv64('192.168.0.1', mascara='255.255.255.0')

    print(ipv64.ip)
    print(ipv64.mascara)
    print(ipv64.rede)
    print(ipv64.broadcast)
    print(ipv64.prefixo)
    print(ipv64.numeros_ips)
    print(ipv64.numeros_ips - 2)

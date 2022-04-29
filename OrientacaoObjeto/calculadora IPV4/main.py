from calculadora_ipv64 import CalculadoraIpv64

# ipv64 = CalculadoraIpv64(ip='192.168.70.10', mascara=255, prefixo=26)

while True:
    ip = input('Informe o IP: ')
    mascara = input('Informe a máscara (caso queira): ')

    if mascara == '':
        mascara = None
        prefixo = input('Informa o prefixo: ')
        if prefixo == '':
            prefixo = None

    try:
        ipv64 = CalculadoraIpv64(ip=ip, mascara=mascara, prefixo=prefixo)

        print(f'IP: {ipv64.ip}')
        print(f'Máscara: {ipv64.mascara}')
        print(f'Rede: {ipv64.rede}')
        print(f'Broadcast: {ipv64.broadcast}')
        print(f'Prefixo: {ipv64.prefixo}')
        print(f'Número de IPs da rede (total): {ipv64.numeros_ips}')
        print(f'Número de IPs da rede (disponíveis): {ipv64.numeros_ips - 2}')
    except (ValueError, TypeError, Exception) as erro:
        print(f'Erro - {erro}')

    print('\n', '*' * 100, '\n')

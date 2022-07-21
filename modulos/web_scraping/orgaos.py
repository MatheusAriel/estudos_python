import requests
from bs4 import BeautifulSoup
from time import perf_counter
import traceback
from time import sleep

z = 1
with open('orgaos.csv', 'w+', encoding='UTF8', newline='') as file:
    url0 = 'https://cnes2.datasus.gov.br/Lista_Tot_Es_Estado_Mantenedora.asp'
    response0 = requests.get(url0)
    html0 = BeautifulSoup(response0.text, 'html.parser')
    table0 = html0.findAll("table")

    for links0 in table0[4].find_all('a', href=True):
        url1 = ('https://cnes2.datasus.gov.br/' + links0['href']).replace(' ', '')
        response1 = requests.get(url1)

        html1 = BeautifulSoup(response1.text, 'html.parser')
        table1 = html1.findAll("table")

        for links1 in table1[4].find_all('a', href=True):
            link_completo = ('https://cnes2.datasus.gov.br/' + links1['href']).replace(' ', '')
            response2 = requests.get(link_completo)

            html2 = BeautifulSoup(response2.text, 'html.parser')
            table2 = html2.findAll("table")

            try:
                for links2 in table2[4].find_all('a', href=True):
                    link_completo_municipio = ('https://cnes2.datasus.gov.br/' + links2['href']).replace(' ', '')

                if 'PREFEITURAMUNICIPAL' in link_completo_municipio or 'PREF MUN' in link_completo_municipio:
                    sleep(2)

                    try:
                        print(link_completo_municipio, z)
                        z += 1
                        response3 = requests.get(link_completo_municipio)
                        html3 = BeautifulSoup(response3.text, 'html.parser')
                        table3 = html3.findAll("table")

                        i = 0
                        for row in table3[4].findAll("tr"):
                            nome = ''
                            cnpj = ''
                            endereco = ''
                            numero = ''
                            complemento = ''
                            cidade = ''
                            cep = ''
                            uf = ''

                            if i == 1:
                                nome = row.findAll('td')[0].text.strip('\n').strip('\t')
                                cnpj = row.findAll('td')[1].text.strip('\n').strip('\t')
                                file.write(f"{nome};{nome};{cnpj};")

                            if i == 3:
                                endereco = row.findAll('td')[0].text.strip('\n').strip('\t')
                                numero = row.findAll('td')[1].text.strip('\n').strip('\t')
                                complemento = row.findAll('td')[2].text.strip('\n').strip('\t')
                                bairro = row.findAll('td')[3].text.strip('\n').strip('\t')
                                file.write(f"{endereco};{numero};{complemento};{bairro};")

                            if i == 5:
                                cidade = row.findAll('td')[0].text.strip('\n').strip('\t')
                                cep = row.findAll('td')[1].text.strip('\n').strip('\t')
                                uf = row.findAll('td')[2].text.strip('\n').strip('\t')
                                file.write(f"{cidade};{cep};{uf}\n")

                            # print(f"{nome};{cnpj};{endereco};{numero};{complemento};{cidade};{cep}")
                            # file.write(f"NOME;endereco;numero;complemento;cidade;cep;uf\n")
                            # print(nome, cnpj, endereco, numero, complemento, cidade, cep, uf, end='|')
                            # file.write(f"{nome};{cnpj};{endereco};{numero};{complemento};{cidade};{cep}\n")
                            # linha = [nome, cnpj, endereco, numero, complemento, cidade, cep, uf]
                            # writer.writerows([nome, cnpj, endereco, numero, complemento, cidade, cep, uf])

                            i += 1

                    except:
                        pass

            except:
                pass

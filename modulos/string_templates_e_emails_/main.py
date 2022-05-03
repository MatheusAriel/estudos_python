from string import Template
from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y %H/%M/%S')
    # corpo_msg = template.substitute(nome='Matheus Ariel',
    #                                 cidade='São Paulo',
    #                                 uf='SP',
    #                                 data=data_atual)

    # assim não gera excessão caso vc n mande uma chave
    corpo_msg = template.safe_substitute(nome='Matheus Ariel',
                                         cidade='São Paulo',
                                         uf='SP',
                                         data=data_atual)

print(corpo_msg)

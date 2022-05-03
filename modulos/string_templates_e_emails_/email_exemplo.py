from string import Template
from datetime import datetime
from dados_email import my_email, my_pass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y %H/%M/%S')
    corpo_msg = template.safe_substitute(nome='Matheus Ariel',
                                         cidade='São Paulo',
                                         uf='SP',
                                         data=data_atual)
msg = MIMEMultipart()
msg['from'] = 'Gilberto emails'
msg['to'] = 'teste@teste.com'  # email do cliente
msg['subject'] = 'Atenção esse é um email de teste'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

try:
    with open('img1.jpg', 'rb') as img:
        imagem = MIMEImage(img.read())
        msg.attach(imagem)
    with open('img2.jpg', 'rb') as img:
        imagem = MIMEImage(img.read())
        msg.attach(imagem)

    with smtplib.SMTP(host='smtp.mailtrap.io', port=2525) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(my_email, my_pass)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso')
except Exception as er:
    print(f'Erro: {er}')

from datetime import datetime


class LogMixin:

    @staticmethod
    def write(msg):
        with open('aula2/log.txt', 'a+') as file:
            data_hora = datetime.now()
            data_hora = data_hora.strftime('%d/%m/%Y %H:%M:%S')
            file.write(msg + f' ### DATA:{data_hora}')
            file.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')

from connector import Connector

db1 = Connector('127.0.0.1', 'João', '1111')
db1.conectar()

db1 = Connector.sem_host('João', '1111')
db1.conectar()

db1 = Connector.sem_host_estatico('João', '1111')
db1.conectar()

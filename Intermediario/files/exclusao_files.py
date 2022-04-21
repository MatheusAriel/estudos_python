import os
try:
    os.remove('teste.txt')
except Exception as error:
    print(error)
except FileNotFoundError as error:
    print(error)

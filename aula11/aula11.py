num1 = (input('Digite um numero: '))
num2 = (input('Digite outro numero: '))

'''
if(num1.isdigit() and num2.isdigit()):
    print('\n', int(num1)+int(num2))
else:
    print('\nDigite numeros validos')
'''

try:
    print('SOMA:', int(num1)+int(num2))
except:
    print('Digite numero válidos')
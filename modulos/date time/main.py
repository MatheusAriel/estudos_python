from datetime import datetime, timedelta

"""
https://docs.python.org/2/library/datetime.html
"""

data = datetime(2020, 4, 30, 13, 26, 2)
print('Date to DB: ', data)
print('Date to BR: ', data.strftime('%d/%m/%Y %H:%M:%S'))

print('*' * 100, '\n\n')

data2 = datetime.strptime('02/05/2022', '%d/%m/%Y')
print(data2)
timestamp = data2.timestamp()
print('Time stamp: ', timestamp)
datetime_timestamp = datetime.fromtimestamp(timestamp)
print(f'time stamp to date {datetime_timestamp}')

print('*' * 100, '\n\n')

data = datetime.strptime('18/09/1993 20:30:00', '%d/%m/%Y %H:%M:%S')
print(f'DATA: {data.strftime("%d/%m/%Y %H:%M:%S")}')

data = data + timedelta(days=10, hours=1, seconds=2 * 60 * 60)

print('DATA +10 dias +1 hora: ', data.strftime('%d/%m/%Y %H:%M:%S'))

print('*' * 100, '\n\n')

d1 = datetime.strptime('18/09/1993 21:30:00', '%d/%m/%Y %H:%M:%S')
print(d1.time())

d2 = datetime.strptime('19/09/1993 22:00:00', '%d/%m/%Y %H:%M:%S')

diff = d2 - d1
print(d1 > d2)
print(diff)

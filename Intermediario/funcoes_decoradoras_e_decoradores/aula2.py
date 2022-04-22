from time import sleep, time


def velocidade(func):
    def interna(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        time_process = (end_time - start_time) * 1000
        print(f'\nO tempo de processo da função {func.__name__}() foi de {time_process:.2f} ms')
        #return result

    return interna


@velocidade
def demora(lenght=5):
    for i in range(lenght):
        print(i,end='')
        #sleep(1)


demora(400)

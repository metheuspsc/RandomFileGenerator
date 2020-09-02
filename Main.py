import random
import string
import time

def GeraTxtAleatorio(linhas):

    start_time = time.time()

    with open('test_{}.txt'.format(linhas), 'w') as f:
        for line in range(linhas):
            f.write(''.join([random.choice(string.ascii_letters) for i in range(60)]))
            f.write('\n')

    end_time = time.time() - start_time

    print('Texto com {} linhas gerado em: {} milisegundos'.format(linhas,end_time*1000))


if __name__ == "__main__":
    GeraTxtAleatorio(10000)
    GeraTxtAleatorio(100000)
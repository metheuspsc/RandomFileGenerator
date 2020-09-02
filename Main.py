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

def OrdenaTxtAleatorio(linhas):

    start_time = time.time()

    with open('test_{}.txt'.format(linhas),'r') as reader:
        
        lines = reader.readlines()
        lines.sort()

    with open('test_{}.txt'.format(linhas),'w') as writer:
        for line in lines:
            writer.write(line)
        
        
    end_time = time.time() - start_time

    print('Texto com {} linhas ordenado em: {} milisegundos'.format(linhas,end_time*1000))

if __name__ == "__main__":
    GeraTxtAleatorio(10000)
    OrdenaTxtAleatorio(10000)
    GeraTxtAleatorio(100000)
    OrdenaTxtAleatorio(100000)
    GeraTxtAleatorio(1000000)
    OrdenaTxtAleatorio(1000000)
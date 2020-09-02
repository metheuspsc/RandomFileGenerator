import random
import string
import time

start_time = time.time()

with open('test_10k.txt', 'w') as f:
    for line in range(10000):
        f.write(''.join([random.choice(string.ascii_letters) for i in range(60)]))
        f.write('\n')

first_time = time.time() - start_time

print('Texto com 10 mil linhas gerado em: {} milisegundos'.format(first_time*1000))

mid_time = time.time()

with open('test_100k.txt', 'w') as f:
    for line in range(100000):
        f.write(''.join([random.choice(string.ascii_letters) for i in range(60)]))
        f.write('\n')

sec_time = time.time() - mid_time

print('Texto com 100 mil linhas gerado em: {} milisegundos'.format(sec_time*1000))

full_time = time.time() - start_time

print('Rotina concluida em: {} milisegundos'.format(full_time*1000))


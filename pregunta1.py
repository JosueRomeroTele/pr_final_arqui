import numpy as np
import threading
import time

# Función para calcular la distancia de Manhattan para un segmento de los vectores
def manhattan_distance_segment(vec1, vec2, start_index, end_index, result, index):
    valor =0
    for i in range(start_index,end_index):
        valor+=abs(vec1[i]-vec2[i])
    result[index]=valor
    # result[index] = np.sum(np.abs(vec1[start_index:end_index] - vec2[start_index:end_index]))

# Función para calcular la distancia de Manhattan utilizando multihilos
def manhattan_distance_multithreaded(vec1, vec2, num_threads):
    segment_size = len(vec1) // num_threads
    threads = []
    results = [0] * num_threads

    for i in range(num_threads):
        start_index = i * segment_size
        if i == num_threads - 1:
            end_index = len(vec1)
        else:
            end_index = (i + 1) * segment_size
        thread = threading.Thread(target=manhattan_distance_segment, args=(vec1, vec2, start_index, end_index, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    return sum(results)

# Generar vectores aleatorios de tamaño 4096
vec1 = np.random.randint(0, 100, size=4096, dtype=np.int32)
vec2 = np.random.randint(0, 100, size=4096, dtype=np.int32)

# Número de hilos a utilizar
# num_threads = 4
hilos = [1,2,4,8,16]
# Medir el tiempo de ejecución
tiempos = list()

rpt = zip(hilos,tiempos)
for x in (hilos):
    num_threads=x
    tiempos_hilo=list()
    for i in range(100):
        # print(num_threads)
        start_time = time.perf_counter()
        distance = manhattan_distance_multithreaded(vec1, vec2, num_threads)
        end_time = time.perf_counter()
        tiempos_hilo.append(end_time-start_time)
    # print(f"Tiempo de ejecución para {x} hilo(s) es {end_time - start_time} segundos")
    tiempos.append(np.median(tiempos_hilo))

for i in rpt:
    print(f'tiempo promedio de ejecucion para {i[0]} hilo es {i[1]}')
    
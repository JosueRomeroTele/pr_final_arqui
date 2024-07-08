import numpy as np
from multiprocessing import Pool, cpu_count
import time
import statistics

# Función para calcular la distancia de Manhattan para un segmento de los vectores
def manhattan_distance_segment(vec1, vec2, start_index, end_index):
    return np.sum(np.abs(vec1[start_index:end_index] - vec2[start_index:end_index]))

# Función para calcular la distancia de Manhattan utilizando multiprocessing
def manhattan_distance_multiprocessing(vec1, vec2, num_processes):
    segment_size = len(vec1) // num_processes
    pool = Pool(processes=num_processes)

    results = pool.starmap(manhattan_distance_segment, [(vec1, vec2, i*segment_size, (i+1)*segment_size) for i in range(num_processes)])

    pool.close()
    pool.join()

    return sum(results)

if __name__ == '__main__':
    # Generar vectores aleatorios de tamaño 4096
    vec1 = np.random.randint(0, 100, size=4096, dtype=np.int32)
    vec2 = np.random.randint(0, 100, size=4096, dtype=np.int32)

    # Obtener el número de núcleos disponibles en el sistema
    num_processes = cpu_count()

    # Medir el tiempo de ejecución utilizando multiprocessing con cpu_count()
    times = []
    num_iterations = 100

    for _ in range(num_iterations):
        start_time = time.time()
        distance = manhattan_distance_multiprocessing(vec1, vec2, num_processes)
        end_time = time.time()
        times.append(end_time - start_time)

    # Calcular la mediana de los tiempos de ejecución
    median_time = statistics.median(times)

    # Mostrar el resultado final
    print(f"Mediana del tiempo de ejecución con {num_processes} procesos (cpu_count()): {median_time} segundos")

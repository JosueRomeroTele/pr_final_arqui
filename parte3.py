import numpy as np
from multiprocessing import Pool,cpu_count
import time
import statistics

# Función para calcular la distancia de Manhattan para un segmento de los vectores
def manhattan_distance_segment(vec1, vec2, start_index, end_index):
    sum = 0
    for i in range(start_index,end_index):
        sum += abs(vec1[i]-vec2[i])
    return sum
    # return np.sum(np.abs(vec1[start_index:end_index] - vec2[start_index:end_index]))

# Función para calcular la distancia de Manhattan utilizando multiprocessing
def manhattan_distance_multiprocessing(vec1, vec2, num_processes):
    segment_size = len(vec1) // num_processes
    pool = Pool(processes=cpu_count)

    results = pool.starmap(manhattan_distance_segment, [(vec1, vec2, i*segment_size, (i+1)*segment_size) for i in range(num_processes)])

    pool.close()
    pool.join()

    return sum(results)

if __name__ == '__main__':
    # Generar vectores aleatorios de tamaño 4096
    vec1 = np.random.randint(0, 100, size=4096, dtype=np.int32)
    vec2 = np.random.randint(0, 100, size=4096, dtype=np.int32)

    # Lista de números de procesos a utilizar
    # num_processes_list = [1, 2, 4, 8, 16]
    num_processes_list = [1]

    # Número de iteraciones por configuración de procesos
    num_iterations = 100

    # Guardar los tiempos de ejecución para cada configuración de procesos
    execution_times = {}

    for num_processes in range(1):
        times = []
        for _ in range(num_iterations):
            start_time = time.perf_counter()
            distance = manhattan_distance_multiprocessing(vec1, vec2, num_processes)
            end_time = time.perf_counter()
            times.append(end_time - start_time)

        # Calcular la mediana de los tiempos de ejecución para esta configuración de procesos
        median_time = np.median(times)
        execution_times[num_processes] = median_time
        print(f"Mediana del tiempo de ejecución con {num_processes} procesos: {median_time} segundos")

    # Mostrar los resultados finales
    for num_processes, median_time in execution_times.items():
        print(f"{num_processes} procesos: {median_time} segundos")

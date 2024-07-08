import numpy as np
import time 
from multiprocessing import cpu_count,Pool
from itertools import repeat

M=100
N=100

def multi_vectores(x: list[np.int32],y : list[np.int32]):
    
    suma =0
    for i in range(len(x)):
        suma = x[i] + y[i]
    
    return suma



if __name__=='__main__':
    resultado = list()
    
    mat_M = np.random.randint(1,100,size=(M,N),dtype=np.int32)
    vector_a = np.random.randint(1,100,size=(M,N),dtype=np.int32)
    args=zip(mat_M,repeat(vector_a))
    
    start= time.perf_counter()
    total = 0
    with Pool(processes=cpu_count()) as p:
        resultado = p.starmap(multi_vectores,args)
        total = np.sum(resultado)
    print(total)
    end = time.perf_counter()
    print(f'tiempo de ejecucion {(end-start):0.3f} segundos')
    
    
    # las operaciones de multiprocesos depende de la cantidad de CPU. la unica opcion
    # en python es multriproceso, pero a costo de cpu.
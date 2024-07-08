import numpy as np
import time 

M=5000
N=5000

def multi_vectores(x: list[np.int32],y : list[np.int32]):
    
    suma =0
    for i in range(len(x)):
        suma = x[i] + y[i]
    
    return suma




if __name__=='__main__':
    resultado = list()
    
    mat_M = np.random.randint(1,100,size=(M,N),dtype=np.int32)
    vector_a = np.random.randint(1,100,size=(M,N),dtype=np.int32)
    
    start= time.perf_counter()
    for vector in mat_M:
        resultado.append(multi_vectores(vector,vector_a))
        
    end = time.perf_counter()
    
    print(f'tiempo de ejecucion {(end-start):0.3f} segundos')
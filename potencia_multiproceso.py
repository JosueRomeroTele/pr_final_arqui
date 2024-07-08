from multiprocessing import Pool
import time


proc = 4
tareas = proc*4

def potencia(n:int, div:int=tareas)->int:
    pot=1
    rango = n//div
    print(rango)
    for i in range(rango):
        pot *=n
    return pot

def main():
    args=[100]*tareas
    p = Pool(processes=proc)
    res = p.map(potencia,args)
    
    p.close()
    p.join()
    
    pot_toal = 1 
    for i in range(len(res)):
        pot_toal *=res[i]
    print(pot_toal)
    
if __name__=='__main__':
    start= time.perf_counter()
    main()
    end = time.perf_counter()
    
    print(f'tiempo de ejecucion: {(end-start):0.3f} segundos')
    
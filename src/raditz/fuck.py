'''
Created on 07/12/2016

@author: 
'''
import logging
import sys
nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

def ordenamiento_raiz(numeros):
    cubetas = [[] for _ in range(10)]
    maximas_posiciones = 0
    numeros_tmp = []
    
    maximo_num = max(numeros)
    logger_cagada.debug("el max num es %s" % maximo_num)
    
    dividendo_act = 1
    while(maximo_num // dividendo_act):
        maximas_posiciones += 1
        dividendo_act *= 10
        
    logger_cagada.debug("shit %s" % maximas_posiciones)
    
    dividendo_act = 1
    numeros_tmp = [x for x in numeros]
    for posicion in range(maximas_posiciones):
        
        for num_act in numeros_tmp:
            lomberto = (num_act // dividendo_act) % 10
            cubetas[lomberto].append(num_act)
            logger_cagada.debug("para la pos %u, el num %u va en la cubeta %u" % (posicion, num_act, lomberto))
        
        logger_cagada.debug("los nums ordenados x pos %u son %s" % (posicion, cubetas))
        
        numeros_tmp.clear()
        
        for cubeta in cubetas:
            while(len(cubeta)):
                numeros_tmp.append(cubeta.pop(0))
                
        logger_cagada.debug("los num semiord %s" % numeros_tmp)
        
        
        dividendo_act *= 10
    
    return numeros_tmp

def raditz_core(numeros):
    tam_numeros = len(numeros)
    
    bitch = ordenamiento_raiz(numeros)
    
    return bitch
    
def raditz_main():
    lineas = list(sys.stdin)
    numeros = []
    
    if(len(lineas)<3):
        linea = lineas[1]
        numeros = [int(x) for x in linea.strip().split(" ")]
        
    else:
        for linea in lineas[1:]:
            numeros.append(int(linea.strip().split(" ")[0]))
        
    logger_cagada.debug("los putos numeros %s" % numeros)
    
    ass = raditz_core(numeros)

    print("[%s]" % (",".join([str(x) for x in ass])))
    

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)   
        raditz_main()


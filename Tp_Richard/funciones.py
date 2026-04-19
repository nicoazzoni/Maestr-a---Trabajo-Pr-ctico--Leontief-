import numpy as np

def calcularLeontief(A):
    # inversa de (I − A) también se conoce como L

    I = np.eye(A.shape[0])
    L = np.linalg.inv(I -A)

    return L

def deltaProduccion(L, delta_d):
    # el delta de la producción consiste en aplicar
    # Leontief sobre el delta de la demanda


    return np.dot(L, delta_d)
#aplico la multiplicación matricial entre
#leontief con el delta

def calcularCoeficientes(Z, totales):
    # formula  = A = ZP−1
    # p debe ser la matriz diagonal con el total producido por el sector
    # y p-1 es su inversa
    inv_p = np.linalg.inv(np.diag(totales))
    A = Z @ inv_p

    return A

def calcularLeontiefInterregional(Arr, Ars, Ass, Asr):
    # formula: Δpr = (I − Arr − Ars(I − Ass)−1Asr)−1Δdr
    I_Arr = np.eye(Arr.shape[0]) #separo en bloques las identidades
    I_Ass = np.eye(Ass.shape[0]) #separo en bloques las identidades


    term_interregional = Ars @ np.linalg.inv(I_Ass - Ass) @ Asr
    L_ir = np.linalg.inv(I_Arr - Arr - term_interregional)

    return L_ir


    
    
    
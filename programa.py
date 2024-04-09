#importan la biblioteca 
import numpy as np

#una forma de crear arreglos ndarray es usando una lista

miLista=[3,5,7,9]
miArreglo=np.array(miLista)


#Dimensiones 
print(miArreglo.ndim) 
print(miArreglo.shape)
print(miArreglo.size)
print(miArreglo.dtype)

miArreglo2=np.array([3,6,7,90])
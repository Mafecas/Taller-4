#importamos la biblioteca Numpy y le agregamos el alias 
import numpy as np
#Impotamos la biblioteca de matplotlib para crear graficas y le agregamos el alias 
import matplotlib.pyplot as plt
#definimos la funcion de matplot y las 3 variables con las que se van a trabajar
def mandelbrot(h, w, maxit=20, r=2):
#creamos un rango de datos que queramos en este caso es -2.5 a 1.5 y genera una lista entre ese rango con un espasci0 definido 4*h+1
    x = np.linspace(-2.5, 1.5, 4*h+1)
#creamos un rango de datos que queramos en este caso es -1.5 a 1.5 y genera una lista entre ese rango con un espasci0 definido 3*w+1
    y = np.linspace(-1.5, 1.5, 3*w+1)
#Asignacion multiple, A y B y se le asigna a x y Y 
    A, B = np.meshgrid(x, y)
    #se realiza una operacion aritmetica, y C es la nueva variable a la que se va asignar 
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                    # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much

    return divtime
plt.clf()
plt.imshow(mandelbrot(400, 400))

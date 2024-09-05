# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Prof.Ing.Jesús González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def line_plot():
    # Generaremos la función y=X^2 (x al cuadrado)
    x = range(-10, 11, 1)
    y = []
    for i in x:
        y.append(i**2)

    fig = plt.figure()
    fig.suptitle('Grafico Ejemplo 1 Y=X**2', fontsize=12)
    ax = fig.add_subplot()

    ax.plot(x, y, c='darkgreen', marker='^', label='función:y=x**2')
    ax.legend()
    ax.grid()
    ax.set_facecolor('whitesmoke')
    plt.show()




if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos de "line_plot" de clase

    # Se desea graficar los valores de "x" e "y" en un gráfico de línea
    # A continuación los datos ya disponibles de "x" e "y" para que utilice:
    x = list(range(-10, 11, 1))

    # Bucle que completa y calcula todos los valores de "y"
    y = []
    for i in x:
        y.append(i**2)

    # Alumno: Crear una "figura" y crear un "ax" con add_subplot
    # Graficar el "line plot" de "y" en función de "x"
    fig = plt.figure()
    ax = fig.add_subplot()
    # Alumno: Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección
    fig.suptitle('Graficar Y=X**2',fontsize=14) 
    ax.plot(x, y, c='darkred', marker='*', label='y=x**2')
    ax.legend()
    # Crear acá su gráfico
    line_plot()

    print("terminamos")

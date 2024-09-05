# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Prof.Ing.Jesús González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def scatter_plot():
    # Demostración de la utilidad del scatter plot
    # Generaremos una linea y=x con ruido sumando
    # valores aleatorios uniformes en cada punto

    sample_size = 20

    x = np.arange(-np.pi, np.pi, 0.1)

    #x = np.linspace(0, 10, sample_size)
    # A los valores de X sumar valores aleatoreos entre -1 y 1
    #y = x + np.random.uniform(-1, 1, sample_size)

    y = np.tanh(x)


    fig = plt.figure()
    fig.suptitle('Scatter', fontsize=16)
    ax2 = fig.add_subplot(1, 2, 2)

    ax2.scatter(x, y, c='darkcyan')
    ax2.set_facecolor('whitesmoke')
    ax2.grid('solid')
    plt.show()
    
if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)

    # Alumno: Graficar la función utilizando "scatter"
    fig = plt.figure()
    ax = fig.add_subplot()
    # utilizando "x" e "y" ya disponible
    ax.scatter(x, y, label='y = tanh(x)', color='green', marker='o')
    # Colocar la leyenda y el label con el nombre de la función
    # Elegir un marker a elección
    ax.set_title('Gráfico de y = tanh(x)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # Crear acá su gráfico
    plt.show()
    scatter_plot()

    print("terminamos")

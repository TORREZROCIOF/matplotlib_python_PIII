# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Prof.Ing.Jesús González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def multi_plot():
    # Dibujar múltiples líneas en un mismo gráfico
   
    #x = list(np.linspace(start=-4, stop=4, num=20))
    x = list(np.linspace(-4, 4, 20))
    
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x, y1, color='green', marker='^', label='y1 = x**2')
    ax.plot(x, y2, color='red', marker='+', label='y2 = x**3')
    
    ax.set_facecolor('whitesmoke')
    ax.set_title("Dos funciones juntas")
    ax.set_ylabel("Y[amplitud]")
    ax.set_xlabel("X[rads]")
    ax.set_xlim([-12, 4*np.pi])  # Limito el eje "Y" entre 0 y 4*pi
    ax.set_ylim([-4, 4])       # Limito el eje "X" entre -4 y 4
    ax.legend()
      
    # Graficar la figura con los 2 axes
    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación ya está disponible, es la siguiente:
    x = list(np.linspace(-4, 4, 20))

    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)

    # Alumno: Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"
    fig = plt.figure()
    ax = fig.add_subplot()
    # Se debe colocar en la leyenda la función que representa
    # cada función
    ax.plot(x, y1, label='y = x^2', color='blue')
    ax.plot(x, y2, label='y = x^3', color='red')
    # Cada función dibujarla con un color distinto
    # a su elección
    ax.legend()
    ax.set_title('Gráfico de funciones y = x^2 y y = x^3')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # Crear acá su gráfico 
    plt.show()
    #multi_plot()  

    print("terminamos")

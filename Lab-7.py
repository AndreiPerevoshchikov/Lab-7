#  Перевощиков Андрей, 367472, вариант 2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from time import perf_counter
import random


#  задание 1
def compar():
    arr1 = []
    arr2 = []
    result = []

    for i in range(1000000):
        arr1.append(random.randint(1, 1000000))
        arr2.append(random.randint(1, 1000000))

    start = perf_counter()
    for i in range(1000000):
        result.append(arr1[i] * arr2[i])
    first_time = perf_counter() - start
    print(first_time, '- время, затраченное на перемножение стандартных списков')

    arr1 = np.random.randint(0, 1000000, 1000000)
    arr2 = np.random.randint(0, 1000000, 1000000)

    start_2 = perf_counter()
    result = np.multiply(arr1, arr2)
    print(perf_counter() - start_2, ' - время, затраченное на перемножение массивов NumPy')


#  задание 2
def hist():
    arr = np.genfromtxt('data2.csv', delimiter=',')
    arr = arr[1:]
    ph = np.array(arr[:, 0], float)
    ph = ph[~np.isnan(ph)]
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot()
    ax.hist(ph, 50, (0, 14), color='lightblue', ec='blue')
    ax.grid()
    plt.title('Гистограмма')
    plt.xlabel('ph')
    plt.ylabel('Частота')
    plt.show()

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot()
    ax.hist(ph, 50, (0, 14), color='lightgreen', ec='green', density=True)
    ax.grid()
    plt.title('Нормализованная гистограмма')
    plt.xlabel('ph')
    plt.ylabel('Частота')
    plt.show()
    print(np.std(ph), '- среднеквадратичное отклонение')


#  Задание 3
def plot3d():
    np.random.seed(40)
    xs = np.linspace(-2*np.pi, 2*np.pi, 100)
    ys = np.sin(xs)*np.cos(xs)
    zs = np.sin(xs)*np.cos(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='*', c='blue')
    plt.title('3D  график')
    plt.show()


#  дополнительное задание
def anim():
    fig = plt.figure()
    line, = plt.plot([], [], 'k')

    plt.xlim(-7, 7)
    plt.ylim(-2, 2)

    writer = PillowWriter(fps=30)
    x_coord = []
    y_coord = []
    with writer.saving(fig, "sin.gif", 100):
        for x in np.linspace(-7, 7, 100):
            x_coord.append(x)
            y_coord.append(np.sin(x))
            line.set_data(x_coord, y_coord)
            writer.grab_frame()


if __name__ == '__main__':
    compar()
    hist()
    plot3d()
    anim()

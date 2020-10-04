import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    n = 1001
    x = np.zeros(n)
    f1 = np.zeros(n)
    f2 = np.zeros(n)

    length = 2 * np.pi

    dx = length / (n - 1)

    for i in range(n):
        x[i] = i * dx
        f1[i] = np.sin(x[i])
        f2[i] = np.cos(x[i])

    fig, ax = plt.subplots(figsize=(8,5), tight_layout=True)
    plt.plot(x, f1, label='sin(x)')
    plt.plot(x, f2, label='cos(x)')

    plt.xlim([0, 2 * np.pi])

    plt.title('our trigonometric function')
    ax.set_xlabel(r'x')
    ax.set_ylabel(r'f(x)')
    ax.legend()

    plt.savefig('sine.png')
    plt.show()



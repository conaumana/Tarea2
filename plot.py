# plot.py
import matplotlib.pyplot as plt

def plot1D(x, y, ejeX, ejeY):
    plt.figure()
    plt.plot(x, y)
    plt.xlabel(ejeX)
    plt.ylabel(ejeY)
    plt.savefig("out1d.png")
    plt.close()

def plot2D(x, y, c, ejeX, ejeY):
    plt.figure()
    plt.scatter(x, y, c=c, cmap='viridis')
    plt.xlabel(ejeX)
    plt.ylabel(ejeY)
    plt.colorbar(label="Tiempo")
    plt.savefig("out2d.png")
    plt.close()

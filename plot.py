# plot.py
import matplotlib.pyplot as plt

def plot1D(x, y, xlabel, ylabel):
    plt.figure()
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig("out1d.png")
    plt.close()

def plot2D(x, y, c, xlabel, ylabel):
    plt.figure()
    plt.scatter(x, y, c=c, cmap='viridis')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar(label="Tiempo")
    plt.savefig("out2d.png")
    plt.close()

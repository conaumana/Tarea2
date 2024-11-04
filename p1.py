# p1.py
import sys
import matplotlib.pyplot as plt
from read import read
from plot import plot1D, plot2D

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = read(input_file)
    if len(data) == 2:
        plot1D(data[0], data[1], "Tiempo", "Posición")
        plt.savefig(output_file)
    elif len(data) == 3:
        plot2D(data[1], data[2], data[0], "x", "y")
        plt.savefig(output_file)

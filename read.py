# read.py
import csv

def read(filename):
    Tiempo = []
    posicion1 = []
    posicion2 = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la cabecera
        for row in reader:
            Tiempo.append(float(row[0]))
            posicion1.append(float(row[1]))
            if len(row) > 2:
                posicion2.append(float(row[2]))

    if values2:
        return Tiempo, posicion1, posicion2
    else:
        return Tiempo, posicion1

# read.py
import csv

def read(filename):
    time = []
    values1 = []
    values2 = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la cabecera
        for row in reader:
            time.append(float(row[0]))
            values1.append(float(row[1]))
            if len(row) > 2:
                values2.append(float(row[2]))

    if values2:
        return time, values1, values2
    else:
        return time, values1

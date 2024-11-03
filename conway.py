import numpy as np
import matplotlib.pyplot as plt
import configparser
import sys

class Celda:
    def __init__(self, estado=False):
        self.estado = estado

    def interactuar(self, vecinos):
        vivos = sum(1 for vecino in vecinos if vecino.estado)
        if self.estado:
            if vivos < 2 or vivos > 3:
                self.estado = False
        else:
            if vivos == 3:
                self.estado = True

class Grilla:
    def __init__(self, tamaño, posiciones_vivas, archivo_exportacion="resultado.png"):
        self.tamaño = tamaño
        self.celdas = [[Celda() for _ in range(tamaño)] for _ in range(tamaño)]
        self.celdas_siguiente = [[Celda() for _ in range(tamaño)] for _ in range(tamaño)]
        self.contador = 0
        self.archivo_exportacion = archivo_exportacion

        # Inicializar celdas vivas
        for x, y in posiciones_vivas:
            self.celdas[x][y].estado = True

    def actualizar_celdas(self):
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                self.celdas[i][j].estado = self.celdas_siguiente[i][j].estado

    def obtener_vecinos(self, x, y):
        vecinos = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.tamaño and 0 <= ny < self.tamaño:
                    vecinos.append(self.celdas[nx][ny])
        return vecinos

    def avanzar(self):
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                vecinos = self.obtener_vecinos(i, j)
                self.celdas_siguiente[i][j].estado = self.celdas[i][j].estado
                self.celdas_siguiente[i][j].interactuar(vecinos)
        self.actualizar_celdas()

    def visualizar(self):
        matriz = np.array([[1 if celda.estado else 0 for celda in fila] for fila in self.celdas])
        plt.imshow(matriz, cmap='binary')
        plt.title(f"Paso {self.contador}")
        plt.axis('off')
        plt.savefig(f"{self.archivo_exportacion.replace('.png', f'_{self.contador}.png')}")
        plt.close()
        self.contador += 1

def leer_datos(archivo):
    config = configparser.ConfigParser()
    config.read(archivo)
    tamaño = int(config['DEFAULT']['tamaño'])
    posiciones_vivas = [tuple(map(int, line.split(','))) for line in config['DEFAULT']['posiciones'].splitlines()]
    return tamaño, posiciones_vivas

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python conway.py 'datos.ini'")
        sys.exit(1)

    # Leer datos del archivo
    tamaño, posiciones_vivas = leer_datos(sys.argv[1])

    # Crear una instancia de la grilla
    grilla = Grilla(tamaño, posiciones_vivas)

    # Ejecutar varios pasos y visualizar el resultado
    for _ in range(10):  # Simular 10 pasos
        grilla.visualizar()
        grilla.avanzar()

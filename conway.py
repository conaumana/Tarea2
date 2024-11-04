import numpy as np
import matplotlib.pyplot as plt

class Celda:
    def __init__(self, estado=False):
        self.estado = estado  # True si está viva, False si está muerta

    def interactuar(self, vecinos):
        # Contar celdas vivas en los vecinos
        vivas = sum(vecino.estado for vecino in vecinos)
        
        if self.estado:  # Si la celda está viva
            if vivas < 2:
                return False  # Muere por soledad
            elif vivas in (2, 3):
                return True  # Sigue viva
            else:
                return False  # Muere por superpoblación
        else:  # Si la celda está muerta
            return vivas == 3  # Renace si hay exactamente 3 celdas vivas


class Grilla:
    def __init__(self, archivo_datos):
        self.tamaño, self.posiciones_vivas = self.cargar_datos(archivo_datos)
        self.celdas = [[Celda() for _ in range(self.tamaño)] for _ in range(self.tamaño)]
        self.celdas_siguiente = [[Celda() for _ in range(self.tamaño)] for _ in range(self.tamaño)]
        self.exportar_archivo = "solucion.txt"
        self.contador = 0
        
        for (x, y) in self.posiciones_vivas:
            self.celdas[x][y].estado = True  # Inicializar las celdas vivas

    def cargar_datos(self, archivo_datos):
        with open(archivo_datos, 'r') as f:
            lineas = f.readlines()
            tamaño = int(lineas[0].strip())
            posiciones_vivas = [tuple(map(int, linea.strip().split(','))) for linea in lineas[1:]]
        return tamaño, posiciones_vivas

    def actualizar_celdas(self):
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                # Actualiza el estado de las celdas
                self.celdas[i][j].estado = self.celdas_siguiente[i][j].estado

    def visualizar(self):
        array = np.array([[1 if celda.estado else 0 for celda in fila] for fila in self.celdas])
        plt.imshow(array, cmap='binary')
        plt.title('Juego de la Vida de Conway')
        plt.axis('off')
        plt.savefig(f'salida_{self.contador}.png')  # Guardar la figura como imagen
        plt.close()  # Cerrar la figura para liberar memoria

    def avanzar(self):
        # Actualiza celdas y calcula nuevos estados
        self.actualizar_celdas()
        
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                vecinos = self.obtener_vecinos(i, j)
                self.celdas_siguiente[i][j].estado = self.celdas[i][j].interactuar(vecinos)
        
        self.contador += 1  # Incrementar el contador de iteraciones

    def obtener_vecinos(self, x, y):
        vecinos = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (0 <= i < self.tamaño) and (0 <= j < self.tamaño) and (i != x or j != y):
                    vecinos.append(self.celdas[i][j])
        return vecinos


# Ejemplo de uso
if __name__ == "__main__":
    # Crear la grilla desde el archivo 'datos.ini'
    grilla = Grilla('datos.ini')

    for _ in range(10):  # Simular 10 iteraciones
        grilla.visualizar()
        grilla.avanzar()

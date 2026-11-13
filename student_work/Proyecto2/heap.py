import matplotlib.pyplot as plt
class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def __len__(self):
        return len(self.arreglo) - 1

    def _intercambiar(self, i, j):
        temp = self.arreglo[i]
        self.arreglo[i] = self.arreglo[j]
        self.arreglo[j] = temp

    def _subir(self, i):
        # sube el elemento de la posición i mientras sea MENOR que su padre
        while i > 1 and self.arreglo[i] < self.arreglo[i // 2]:
            self._intercambiar(i, i // 2)
            i = i // 2

    def _bajar(self, i):
        # baja el elemento de la posición i mientras sea MAYOR que su hijo más pequeño
        n = len(self)
        while 2 * i <= n:
            menor = 2 * i                                   # hijo izquierdo
            if 2 * i + 1 <= n:
                if self.arreglo[2 * i + 1] < self.arreglo[2 * i]:
                    menor = 2 * i + 1                       # hijo derecho (solo si es estrictamente menor)
            if self.arreglo[i] > self.arreglo[menor]:
                self._intercambiar(i, menor)
                i = menor
            else:
                return

    # ---------- operaciones de la página ----------
    def insert(self, valor, imagen=False):
        # Insert: se pone al final y se sube
        self.arreglo.append(valor)
        self._subir(len(self))
        if imagen:
            self.dibujar()

    def remove_smallest(self, imagen=False):
        # Remove Smallest: se saca la raíz, el último pasa a la raíz y se baja
        if len(self) == 0:
            if imagen:
                self.dibujar()
            return None
        menor = self.arreglo[1]
        ultimo = self.arreglo.pop()
        if len(self) > 0:
            self.arreglo[1] = ultimo
            self._bajar(1)
        if imagen:
            self.dibujar()
        return menor

    def build_heap(self, lista, imagen=False):
        # BuildHeap: copia la lista y baja cada nodo interno, desde n//2 hasta 1
        self.arreglo = [float('-inf')]
        n = len(lista)
        i = 0
        while i < n:
            self.arreglo.append(lista[i])
            i += 1
        i = len(self) // 2
        while i >= 1:
            self._bajar(i)
            i -= 1
        if imagen:
            self.dibujar()

    # ---------- imagen ----------
    def _posicion(self, i):
        # nivel del nodo i (la raíz está en el nivel 0) y su coordenada (x, y)
        nivel = 0
        while 2 ** (nivel + 1) <= i:
            nivel += 1
        lugar = i - 2 ** nivel                       # posición dentro del nivel (0, 1, 2, ...)
        x = (lugar + 0.5) / 2 ** nivel               # cada nodo queda centrado en su espacio
        y = -nivel
        return x, y

    def dibujar(self):
        # muestra el árbol del heap en su estado actual
        n = len(self)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.axis('off')
        if n == 0:
            ax.text(0.5, 0.5, 'Heap vacío', ha='center', va='center', fontsize=14)
            plt.show()
            return

        # aristas: de cada nodo a sus hijos
        i = 1
        while i <= n:
            x, y = self._posicion(i)
            hijo = 2 * i
            while hijo <= 2 * i + 1:
                if hijo <= n:
                    xh, yh = self._posicion(hijo)
                    ax.plot([x, xh], [y, yh], color='black', zorder=1)
                hijo += 1
            i += 1

        # nodos con su valor
        i = 1
        while i <= n:
            x, y = self._posicion(i)
            ax.scatter(x, y, s=700, color='white', edgecolors='black', zorder=2)
            ax.text(x, y, str(self.arreglo[i]), ha='center', va='center', fontsize=10, zorder=3)
            i += 1

        niveles = -self._posicion(n)[1]
        ax.set_xlim(0, 1)
        ax.set_ylim(-niveles - 0.5, 0.5)
        plt.show()

    def __repr__(self):
        return str(self.arreglo)


if __name__ == "__main__":
    H = Heap()
    H.insert(10)
    H.insert(4)
    H.insert(7)
    print(H)            # [-inf, 4, 10, 7]
    H.remove_smallest()
    print(H)            # [-inf, 7, 10]

class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        self._percolate_up(len(self.arreglo) - 1)

    def remove_smallest(self):
        if len(self.arreglo) <= 1:
            return None

        if len(self.arreglo) == 2:
            return self.arreglo.pop()

        min_val = self.arreglo[1]
        self.arreglo[1] = self.arreglo.pop()
        self._percolate_down(1)
        return min_val

    def build_heap(self, lista):

        self.arreglo = [float('-inf')] + lista
        i = (len(self.arreglo) - 1) // 2
        while i > 0:
            self._percolate_down(i)
            i -= 1

    def _percolate_up(self, i):

        while i // 2 > 0:
            padre = i // 2
            if self.arreglo[i] < self.arreglo[padre]:
                self.arreglo[i], self.arreglo[padre] = self.arreglo[padre], self.arreglo[i]
                i = padre
            else:
                break

    def _percolate_down(self, i):

        while i * 2 < len(self.arreglo):
            hijo_menor = self._menor_hijo(i)
            if self.arreglo[i] > self.arreglo[hijo_menor]:
                self.arreglo[i], self.arreglo[hijo_menor] = self.arreglo[hijo_menor], self.arreglo[i]
                i = hijo_menor
            else:
                break

    def _menor_hijo(self, i):
        if i * 2 + 1 >= len(self.arreglo):
            return i * 2
        if self.arreglo[i * 2] <= self.arreglo[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

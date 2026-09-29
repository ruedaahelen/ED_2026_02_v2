from goodrich.ch08.linked_binary_tree import LinkedBinaryTree


def es_completo(T):
    """Retorna True si el LinkedBinaryTree T es completo."""
    if len(T) == 0:
        return True
    cola = [T.root()]
    i = 0
    hueco = False          # ¿ya encontramos un hijo que falta?
    while i < len(cola):
        p = cola[i]
        i += 1
        izq = T.left(p)
        der = T.right(p)
        if izq is None:
            hueco = True
        else:
            if hueco:
                return False
            cola.append(izq)
        if der is None:
            hueco = True
        else:
            if hueco:
                return False
            cola.append(der)
    return True


def camino(T, p, q):
    """Retorna el camino de p a q como string: 'H -> D -> B -> E'."""
    subida = []            # nodos desde p hacia arriba
    bajada = []            # nodos desde q hacia arriba (luego se invierten)
    dp = T.depth(p)
    dq = T.depth(q)
    # 1. Igualar profundidades
    while dp > dq:
        subida.append(p)
        p = T.parent(p)
        dp -= 1
    while dq > dp:
        bajada.append(q)
        q = T.parent(q)
        dq -= 1
    # 2. Subir los dos a la vez hasta que se encuentren (ancestro común)
    while p != q:
        subida.append(p)
        bajada.append(q)
        p = T.parent(p)
        q = T.parent(q)
    subida.append(p)       # el ancestro común más bajo
    # 3. Unir: subida + bajada al revés
    nodos = subida
    j = len(bajada) - 1
    while j >= 0:
        nodos.append(bajada[j])
        j -= 1
    # 4. Armar el string
    texto = str(nodos[0].element())
    k = 1
    n = len(nodos)
    while k < n:
        texto += " -> " + str(nodos[k].element())
        k += 1
    return texto


if __name__ == "__main__":
    pass

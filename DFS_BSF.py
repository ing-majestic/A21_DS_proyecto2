class Vertice:
    #constructor
    def __init__(self, i):
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.padre = None
        self.vecinos = []

    def agregaVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)

class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregaVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)

    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVecino(b)
            self.vertices[b].agregaVecino(a)


class Bfs:
    g = Grafica()
    def __ini__(self):
        self.bfs = {}

    def bfs(self, r):
        g = Grafica()
        if r in g.vertices:
            cola = [r]

            g.vertices[r].visitado = True
            g.vertices[r].nivel = 0

            print("("+ str(r) + ", "+ str(g.vertices[r].nivel)+")")

            while (len(cola) > 0):
                act = cola[0]
                cola = cola[1:]

                for v in g.vertices[act].vecinos:
                    if g.vertices[v].visitado == False:
                        cola.append(v)
                        g.vertices[v].visitado = True
                        g.vertices[v].nivel = g.vertices[act].nivel + 1
                        print("(" + str (v) + ", " + str(g.vertices[v].nivel) + ")")

class Dfs:
    g = Grafica()
    def __ini__(self):
        self.dfs = {}

    def dfs(self, r):
        g = Grafica()
        if r in g.vertices:
            g.vertices[r].visitado = True
            for nodo in g.vertices[r].vecinos:
                if g.vertices[nodo].visitado == False:
                    g.vertices[nodo].padre = r
                    print("(" + str(nodo) + ", " + str(r) + ")")
                    g.dfs(nodo)

def main():
    g = Grafica()
    h = Bfs()
    k = Dfs()


    l = [0, 1, 2, 3, 4, 5, 6]
    for v in l:
        g.agregaVertice(v)
        #print(v)

    l = [1, 2, 1, 5, 2, 3, 2, 5, 3, 4, 4, 5, 4, 6]
    for i in range(0, len(l) - 1, 2):
        a = l[i]
        b = l[i + 1]
        g.agregarArista(a, b)
        #print(a, b)

    for v in g.vertices:
        print(v, g.vertices[v].vecinos)

    print ("\n")
    h.bfs(2)
    print ("\n")
    print ("(1, NULL)")
    k.dfs(1)

main()

#import module
from graphviz import Digraph
import random

#Se inicializa la clase encargada de administrar los nodos del Grafo
class Nodo:
    #constructor
    def __init__(self, i):
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.padre = None
        self.vecinos = []
    #Se crea la funcion de agregar vecinos a los nodos
    def agregaVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
# Se inicializa la clase encargada de administrar las Aristas del Grafo
class Arista:
    #constructor
    def __init__(self):
        self.id = 0
    #Funcion para agregar aristas al Grafo
    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVecino(b)
            self.vertices[b].agregaVecino(a)

#Se inicializa la clase Grafo que se encarga de administrar y generar los elementos del Grafo
class Grafo:
    #constructor
    def __init__(self):
        self.id = {}
        self.vertices = {}
    #Funcion para la agregación de vertices al Grafo
    def agregaVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Nodo(v)
    #Función para agregar aristas al Grafo
    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVecino(b)
            self.vertices[b].agregaVecino(a)

    #metodo para calcular BFS
#class Bfs():
#    def __init__(self):
#        self.id = {}

    def bfs(self,r,h2):


        if r in self.vertices:
            cola = [r]

            self.vertices[r].visitado = True
            self.vertices[r].nivel = 0

            print("("+ str(r) + ", "+ str(self.vertices[r].nivel)+")")

            while (len(cola) > 0):
                act = cola[0]
                cola = cola[1:]

                for v in self.vertices[act].vecinos:
                    if self.vertices[v].visitado == False:
                        cola.append(v)
                        self.vertices[v].visitado = True
                        self.vertices[v].nivel = self.vertices[act].nivel + 1
                        a = v
                        b = self.vertices[v].nivel
                        print("(" + str (v) + ", " + str(self.vertices[v].nivel) + ")")
                        h2.agregaNodol(b,a,b)
        name = 'BFS_grafo'
        h2.imprimegrafo(name)

    #Metodo para calcular DFS
#class Dfs():


#    def __init__(self):
#        self.dfs = 0

    def dfs(self, h):


        if h in self.vertices:
            self.vertices[h].visitado = True
            for nodo in self.vertices[h].vecinos:
                if self.vertices[nodo].visitado == False:
                    self.vertices[nodo].padre = h
                    print("(" + str(nodo) + ", " + str(h) + ")")
                    self.dfs(nodo)

#Se inicializa clase que permite crear los archivos de visualizaciónote
#Se genera el grafo en formato GV y en formato PNG para su futuro analisis
class graphviz:
    dot = Digraph(comment='The Round Graph')
    #constructor
    def __init__(self):
        self.graphvis = {}
    #Función que agrega nodo con etiqueta para generar el archivo GV y PNG
    def agregaNodol(self,v,et,el):
        vs = str(v)
        es = str(et)
        ex = str(el)
        self.dot.node(vs, es, xlabel= ex)
    #Función que agrega nodo sin etiqueta para generar el archivo GV y PNG
    def agregaNodo(self,v,et):
        vs = str(v)
        es = str(et)
        self.dot.node(vs, es)
    #Función que permite crear la lista en formato adecuado
    def listaedges(self,l2,a,b):
        c = str(a) + str(b)
        l2.append(c)
    #funcion que agrega arista por arista con una variable c con valor false o true
    def agregaedge(self, a, b):
        c = str(a)
        d = str(b)
        self.dot.edge(c , d, constraint='false')
    #Función que permite agregar la lista de conexiónes
    def agregaedges(self,l2):
        self.dot.edges(l2)
    #Función encargada de generar el archivo GV como el PNG
    def imprimegrafo(self, nom):
        print('-------Impresion y generacion GV de Grafo')
        #self.dot.format = 'png'
        a ='Graphviz-output/'
        b = a + str(nom)+ '.gv'
        self.dot.render(b, view = True)
        #print(self.dot.source) #doctest: +NORMALIZE_WHITESPACE


#clase del modelo Malla
#Función con la que se integra el GRAFO de estudio
class Malla():
    def __init__(self):
        self.id={}

    def malla(self):
        #Llamado de las clases
        g = Grafo()
        j = Grafo()
        h1 = graphviz()
        h2 = graphviz()
        h3 = graphviz()
        #k1 = Bfs()
        #k2 = Dfs()
        #Pide el numero de nodos que tendra el Grafo
        print ("-----GRAFO MALLA------")
        print ("Ingresa el numero de nodos: ")
        N = int(input())
        l = list(range(1,N+1))

        for v in l:
            g.agregaVertice(v)
            j.agregaVertice(v)
            #Se agregan nodos al constructor de GV y PNG
            h1.agregaNodo(v,v)

        #Lista de aristas del Grafo
        l2 = []
        l3 = []
        #ve = [1,2]


        #Ciclo generador de aristas en pares
        for i in l:
            random.shuffle(l)
            x = random.randint(1,len(l))
            for i in range(0, x - 1, 2):
                a = l[i]
                b = l[i + 1]
                #agregan aristas al grafo
                g.agregarArista(a, b)
                j.agregarArista(a, b)
                #Se genera la lista para el archivo GV
                h1.agregaedge(a, b)
                c=str(a)
                d=str(b)
                e='->'
                l2.insert(i, c+e+d)
                l3.insert(i, c)
                l3.insert(i+1, d)

        print('-------Grafo  Conjuntos')
        print('V = %s'%l)
        print('E = %s'%l2)
        #Se imprime encabezado de resultados
        print('-------Grafo lista de adyacentes')
        #Se construye la lista de adyacencia
        for v in g.vertices:
            print(v, g.vertices[v].vecinos)

        #Menu para seleccionar el tipo d ecalculo a realizar en al Grafo
        #print ("Ingresa '1' para bfs o '2' para dfs: ")
        #n2 = int(input())
        # Generación de calculo por bfs
        #if n2 == 1:
        print('-------Grafo calculado BFS')
        g.bfs(1,h2)
        # Generación de calculo por dfs
        #elif n2 == 2:
        print('-------Grafo calculado DFS')
        print ("(1, NULL)")
        j.dfs(1)
        #Generacion y guardado de fuente archivo GV y PNG en \Graphviz-output
        nodos = str(N)
        nom = "1_Malla"
        h1.imprimegrafo(nom+'_'+nodos)
        return (l, l3)

#clase del modelo erdos and enry
class Erdosrenyi():
    #constructor
    def __init__(self):
        self.id={}

    def erdosrenyi(self):
        #Inicializa un grafo
        g = Grafo()
        k = Grafo()
        h = graphviz()
        h2 = graphviz()
        h3 = graphviz()
        l2 = []
        l3 = []
        #Pide el numero de nodos que tendra el Grafo
        print ("-----GRAFO ERDOS ENRY------")
        print ("Ingresa el numero de nodos: ")
        N = int(input())
        l = list(range(1,N+1))

        for v in l:
            g.agregaVertice(v)
            k.agregaVertice(v)
            #Se agregan nodos al constructor de GV y PNG
            h.agregaNodo(v,v)

        #Pide el rango d eprobabilidad P
        #print("Ingresa el valor de probabilidad de cada nodo: ")
        #P = float(input())
        P = float(1)
        #l representa los nodos que tomara en cuenta el grafo, P representa el numero flotante de probabilidad entre 0.1 y 1.0
        for i in l:
            x = random.randint(1,len(l))
            for j in range(0, x - 1, 2):
                if i < j:
                    #tomando un numero random R
                    R = random.random()
                    #Verificar si R < P
                    if (R < P):
                        # Agrega las aristas para el grafo
                        g.agregarArista(i, j)
                        k.agregarArista(i, j)
                        #Se genera la lista para el archivo GV
                        h.agregaedge(i, j)
                        c=str(i)
                        d=str(j)
                        e = '->'
                        l2.insert(i, c+e+d)
                        l3.insert(i, c)
                        l3.insert(i+1, d)
        #agrega la lista de vetices
        print('-------Grafo  Conjuntos')
        print('V = %s'%l)
        print('E = %s'%l2)
        #Se imprime encabezado de resultados
        print('-------Grafo lista de adyacentes')
        #Se construye la lista de adyacencia
        for v in g.vertices:
            print(v, g.vertices[v].vecinos)
        #Menu para seleccionar el tipo d ecalculo a realizar en al Grafo
        #print ("Ingresa '1' para bfs o '2' para dfs: ")
        #n2 = int(input())
        # Generación de calculo por bfs
        #if n2 == 1:
        print('-------Grafo calculado BFS')
        g.bfs(1, h2)
        # Generación de calculo por dfs
        #elif n2 == 2:
        print('-------Grafo calculado DFS')
        print ("(1, NULL)")
        k.dfs(1)
        nodos = str(N)
        nom = "2_ErdosRenyi"
        h.imprimegrafo(nom+'_'+nodos)
        return(l, l3)

class Gilbert():
    #constructor
    def __init__(self):
        self.id={}

    def gilbert(self):
        #Inicializa un grafo
        g = Grafo()
        k = Grafo()
        h = graphviz()
        h2 = graphviz()
        h3 = graphviz()
        l2 = []
        l3 = []
        #Pide el numero de nodos que tendra el Grafo
        print ("-----GRAFO GILBERT------")
        print ("Ingresa el numero de nodos: ")
        N = int(input())
        l = list(range(1,N+1))

        for v in l:
            g.agregaVertice(v)
            k.agregaVertice(v)
            #Se agregan nodos al constructor de GV y PNG
            h.agregaNodo(v,v)

        #Pide el rango d eprobabilidad P
        print("Ingresa el valor de probabilidad de cada nodo: ")
        P = float(input())
        #l representa los nodos que tomara en cuenta el grafo, P representa el numero flotante de probabilidad entre 0.1 y 1.0
        for i in l:
            x = random.randint(1,len(l))
            for j in range(0, x - 1, 2):
                if i < j:
                    #tomando un numero random R
                    R = random.random()
                    #Verificar si R < P
                    if (R < P):
                        # Agrega las aristas para el grafo
                        g.agregarArista(i, j)
                        k.agregarArista(i, j)
                        #Se genera la lista para el archivo GV
                        h.agregaedge(i, j)
                        c=str(i)
                        d=str(j)
                        e = '->'
                        l2.insert(i, c+e+d)
                        l3.insert(i, c)
                        l3.insert(i+1, d)
        #agrega la lista de vetices
        print('-------Grafo  Conjuntos')
        print('V = %s'%l)
        print('E = %s'%l2)
        #Se imprime encabezado de resultados
        print('-------Grafo lista de adyacentes')
        #Se construye la lista de adyacencia
        for v in g.vertices:
            print(v, g.vertices[v].vecinos)
        #Menu para seleccionar el tipo d ecalculo a realizar en al Grafo
        #print ("Ingresa '1' para bfs o '2' para dfs: ")
        #n2 = int(input())
        # Generación de calculo por bfs
        #if n2 == 1:
        print('-------Grafo calculado BFS')
        g.bfs(1, h2)
        # Generación de calculo por dfs
        #elif n2 == 2:
        print('-------Grafo calculado DFS')
        print ("(1, NULL)")
        k.dfs(1)
        #Generacion y guardado de fuente archivo GV y PNG en \Graphviz-output
        nodos = str(N)
        nom = "3_Gilbert"
        h.imprimegrafo(nom+'_'+nodos)
        return(l, l3)

#Funcion principal de llamado del programa
def main():
    #Lamado a clase del modelo
    a = Malla()
    b = Erdosrenyi()
    c = Gilbert()

    #ejecución de la funcion del modelo
    a.malla()
    #Se ejecuta erdos que a su vez devuelve las cadenas de vertices y aristas
    #a variables para poder ser usadas en otras clases o funciones
    l, l3 = b.erdosrenyi()
    #print(l)
    #print(l3)
    c.gilbert()
main()

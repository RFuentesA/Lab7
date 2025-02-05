#from List import *

class Heap():
    def __init__(self, size = 0, arreglo = []):
        self.__size = size
        self.__arreglo = arreglo

    def getSize(self):
        return self.__size
    
    def setSize(self, size):
        self.__size = size
    
    def getArreglo(self):
        return self.__arreglo
    
    def setArreglo(self, arreglo):
        self.__arreglo = arreglo
    
    def parent(self, i):
        padrecito = round(i/2) - 1
        if padrecito < 0:
            return 0
        else:
            return padrecito
    
    def hijoIzquierdo(self, i):
        return 2*i + 1
    
    def hijoDerecho(self, i):
        return 2*i + 2
    
    def maxHeapify(self, i):
        if self.__arreglo != None: #Verifico si el arreglo esta vacio.
            arreglo = self.__arreglo
            #self.setArreglo(arreglo) Si el arreglo contiene algo lo ingresa como atributo del nuevo objeto.
            self.__size = len(arreglo) #Se actualiza el tamaño para que tome el tamaño del arreglo.
            tamañoHeap = self.getSize() #variable que guarda el tamaño del heap.
        else:
            print("El arreglo que diste esta vacio. ")
        l = self.hijoIzquierdo(i) #l va a tomar el indice del hijo izquierdo.
        r = self.hijoDerecho(i) #r va a tomar el indice del hijo derecho.
        if l <= tamañoHeap and arreglo[l]>arreglo[i]:          #-----
            mayor = l                                              #|
        else:                                                      #|
            mayor = i                                              #|
        if r <= tamañoHeap and arreglo[r]>arreglo[mayor]:          #|
            mayor = r                                              #---- Se asegura que el indice con el mayor numero quede en la posicion correcta. 
        if mayor != i:                                             #|
            temp = arreglo[i]                                      #|
            arreglo[i] = arreglo[mayor]                            #|
            arreglo[mayor] = temp                                  #|
            self.maxHeapify(mayor)                             #----- 
        return self.__arreglo
    
    def buildMaxHeap(self):
        for i in range(len(self.__arreglo) // 2 - 1, -1, -1): #Arranca desde la mitad del arreglo.
            self.maxHeapify(i) #Usa el método para asegurarse que el el mayor vaya siempre arriba.
        return self.__arreglo
    
    def heapSort(self):
        self.buildMaxHeap()
        for i in range(len(self.__arreglo)-1, 0, -1):
            temp = self.__arreglo[i]
            self.__arreglo[i] = self.__arreglo[0]
            self.__arreglo[0] = temp
            self.__size -= 1
            self.maxHeapify(0)
        return self.__arreglo
        

       
h1 = Heap()
arreglito = [1, 2, 3, 4, 5, 6, 7]
h1.setArreglo(arreglito)
#print(h1.maxHeapify(2))
#print(h1.buildMaxHeap())
print(h1.heapSort())
#print(h1.parent(3))
#print(h1.self.__arreglo)
#print(h1.hijoDerecho(1))
    
    
        
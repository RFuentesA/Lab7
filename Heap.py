from List import *

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
        return round((i/2) - 1)

h1 = Heap(0, None)
arreglo1 = [12, 31, 24, 9, 11]
h1.setArreglo(arreglo1)
#print(h1.parent(6))
print(round(h1.getArreglo()[]))

    
    
        
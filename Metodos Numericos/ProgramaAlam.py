class PriorityQueue:
    def __init__(self):
        self.__data = list() #[]

    def is_empty(self):
        return len(self.__size) == 0

    def length(self):
        return len(self.__size)

    def enqueue(self,prioridad,elem):
        self.__data.append(elem)
        """recorre=list()
        if prioridad >= 0:
            if not self.is_empty():
                i=0
                while i >= int(prioridad):
                    salva = self.__data.pop(len(self.__size))
                    recorre.append(salva)
                    i+=1
                self.__data[prioridad].enqueue(elem)
                j=0
                while j <= len(recorre):
                    salva = recorre.pop(0)
                    self.__data.append(elem)
                    j+=1
            else:
                self.__data.append(elem)

            self.__size += 1"""


    def dequeue(self):
        if not self.is_empty():
            return self.__data.pop(0)
        else:
            return None

    def to_string(self):
        cadena = ""
        for elem in self.__data:
            cadena += "|" + str(elem)
        cadena += "|"
        return cadena

#from colas import Queue,BoundePriorityQueue
maestres = {"prioridad":4,"descripcion":"Maestre","personas":["Juan P","Diego H"]}
mujeres = {"prioridad":3,"descripcion":"Mujeres","personas":["Fernanda Y","Daniela M"]}
cpa=PriorityQueue()
cpa.enqueue(maestres["prioridad"], maestres)
cpa.enqueue(mujeres["prioridad"],mujeres)
print(cpa.to_string())
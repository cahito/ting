class Queue:
    def __init__(self):
        self._data = []
        self.__length = 0

    def __len__(self):
        return self.__length

    def __str__(self):
       return str(self._data)

    def enqueue(self, value):
        self._data.append(value)
        self.__length += 1

    def dequeue(self):
        retirado = self._data.pop(0)
        self.__length -= 1
        return retirado

    def search(self, index):
        if index not in range(len(self)):
            raise IndexError("Elemento inexistente")
        return self._data[index]

from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    # def __str__(self):
    #    return str(self._data)

    def __iter__(self):
        return iter(self._data)

    def __repr__(self) -> str:
        return f"queue({[cada for cada in self._data]})"

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.popleft()

    def search(self, index):
        if index not in range(len(self)):
            raise IndexError("Elemento inexistente")
        return self._data[index]

class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        if self.is_empty():
            return None

        return self._data.pop(0)

    def search(self, index):
        if not (-1 < index < len(self._data)):
            raise IndexError("Invalid Index")

        return self._data[index]

    def is_empty(self):
        return not len(self._data)

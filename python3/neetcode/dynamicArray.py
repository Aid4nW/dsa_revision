class DynamicArray:
    """
    Trivial Dynamic Array implementation as Python handles memory
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = []

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # Resize array if full. 
        if self.getCapacity() == self.getSize():
            self.resize()

        self.array.append(n)

    def popback(self) -> int:
        return self.array.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.capacity
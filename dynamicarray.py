


class DynamicArray():
    
    def __init__(self):
        self.size = 0  #default starting size of 0
        self.capacity = 10 #default starting capacity of 10
        self.arr = [None] * capacity

    def append(self, value):
        if self.size = self.capacity:
            self.resize()
            
        
        self.arr[size] = value
        self.size += 1


    def resize(self):       #default resize to double the current capacity
        self.capacity = self.capacity * 2
        newArr = [None] * self.capacity

        #Copy existing to new array
        for i in range(self.size):
            newArr[i] = self.arr[i]
        self.arr = newArr

    def pushback(self, value):
        if self.size = self.capacity:
            self.resize()

        self.arr[self.size] = value
        self.size += 1

    def popback(self):

        if self.size > 0:
            self.size -= 1

    def get(self, i):
        if i >= self.size:
            raise Exception("Out of bounds")
            return
        return self.arr[i]

    def insert(self, i, value):
        if i >= self.size:
            raise Exception("Out of bounds")
            return
        
        self.arr[i] = value

    def print(self):
        for i in range(self.size):
            print(self.arr[i])
        print()




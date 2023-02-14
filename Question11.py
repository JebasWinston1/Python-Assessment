''' Do this in a function.
    1. class: A initialize with 2 values x and y
     methods: a) add, -> add and return x and y
              b) sub, -> find x - y
              c) swap
    2. class B -> subclass of A
     methods: a) sub -> Check if x < y. Then swap x and y. Then call A's sub function.
              b) swap -> swap x and y. '''

class A():
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x+self.y
    
    def sub(self):
        return self.x-self.y

    def swap(self):
        pass

class B(A):
    def __init__(self, x, y):
        super().__init__(x, y)

    def sub(self):
        if self.x < self.y:
            self.x,self.y = self.y,self.x   
            return super().sub()

    def swap(self):
        print(f"Before Swapping: x = {self.x} and y = {self.y}")
        self.x,self.y = self.y,self.x

obj1 = A(10, 20)
obj2 = B(30, 40)
print("----------------------------------------")
print("Class A".center(40," "))
print("----------------------------------------")
print("Values:")
print(f"x = {obj1.x}")
print(f"y = {obj1.y}")
print("----------------------------------------")
print(f"Addition: {obj1.add()}")
print(f"Subtraction: {obj1.sub()}")
print("----------------------------------------")
print("Class B".center(40," "))
print("----------------------------------------")
print("Values:")
print(f"x = {obj2.x}")
print(f"y = {obj2.y}")
print("----------------------------------------")
print(f"Subtraction: {obj2.sub()}")
obj2.swap()
print(f"After Swapping: x = {obj2.x} and y = {obj2.y}")
print("----------------------------------------")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent constructor
        self.breed = breed
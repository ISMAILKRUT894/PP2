class Counter:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self   # iterator returns itself

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
def generate(i):
    yield i*i
m = generate(5)
print(next(m))    
print(next(m))
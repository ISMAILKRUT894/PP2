#1
def square_upto(n):
    for i in range(n + 1):
        yield i * i

# test
N = 10
for sq in square_upto(N):
    print(sq)
#2
def evens_upto(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
print(",".join(str(x) for x in evens_upto(n)))
#3
def div_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# test
n = 100
for x in div_by_3_and_4(n):
    print(x)
#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# test
for val in squares(3, 8):
    print(val)
#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

# test
for x in countdown(5):
    print(x)

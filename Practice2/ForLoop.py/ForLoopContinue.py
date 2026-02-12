a = [12, 34, 11, 76, 98]
max = a[0]
for i in range(1, len(a)):
    if a[i] < max:
        max = a[i]
print(max)
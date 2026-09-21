

oblongo = lambda n : any(x * (x + 1) == n for x in range(1, n))
print(oblongo(10))
print(oblongo(72))


triangular = lambda n: any(x * (x + 1)/2 == n for x in range(1, n))

print(bool(triangular(10)))
print(bool(triangular(5)))
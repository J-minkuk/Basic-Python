t = (1, 2, 3)
print(type(t))

print(len(t))


def calc(a, b):
    return a + b, a * b


print(calc(3, 4))

args = (4, 5)
print(calc(*args))

print('\n')

a = set([1, 2, 3])
print(a)
print(type(a))

b = list(a)
print(b)
print(type(b))

c = tuple(b)
print(c)
print(type(c))

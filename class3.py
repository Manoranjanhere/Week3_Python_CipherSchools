def generate_squares(n):
    for i in range(1,n):
        yield i**2#lazy loading       
for i in generate_squares(10000):
    print(i)

def generate_squares(n):
    return[i**2 for i in range(1,n)]
for x in generate_squares(10):
    print(x)



from time import sleep
def func():
    yield
    sleep(5)
    print("ended")
    print("hello")
func()
print("world")

def func():
    print("start")
    yield 1
    print("yielded 1")
    yield 2
    print("yielded 2")
it=iter(func())
a = (i**2 for i in range(10))
print(type(a))
for i in a:
    print(i)
a = generate_squares(10)
for i in a:
    print(next(a))
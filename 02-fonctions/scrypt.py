def say_hello(name: str = None):


    if name is None:
        name = 'World'


    print(f'hello', name)
    #return f'Hello, {name}!'


say_hello('greg')

def square(x):
    return x * x

result = square(5)
print(result)


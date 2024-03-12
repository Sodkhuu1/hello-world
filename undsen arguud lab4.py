X = 5

def foo():
    Y = 10
    print(X + Y)

def bar():
    X = 7
    foo()

bar()
print(X)


X = 2

def foo(Y):
    global X
    X += Y

def bar():
    global X
    X *= 2

foo(3)
bar()
print(X)


X = 5

def foo():
    print(X)

def bar():
    global X
    X = 10
    foo()

bar()



def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(result)

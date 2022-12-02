import cython

def fib(n: cython.int) -> cython.int:
    a: cython.int = 0
    b: cython.int = 1

    i: cython.int = 1
    while i < n:
        a, b = b, a + b
        i += 1
    
    return b

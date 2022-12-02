def fib(n: int) -> int:
    a: int = 0
    b: int = 1

    i: int = 1
    while i < n:
        a, b = b, a + b
        i += 1
    
    return b

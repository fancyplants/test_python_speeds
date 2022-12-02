def fib(int n):
    # cdef int a, b, i
    cdef int a = 0
    cdef int b = 1
    cdef int i = 1

    while i < n:
        a, b = b, a + b
        i += 1
    
    return b

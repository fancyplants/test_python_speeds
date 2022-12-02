import timeit

count = 100


onlypy = timeit.timeit(f'fib({count})', setup='from fib_python import fib')
cython_basic = timeit.timeit(f'fib({count})', setup='from fib_cython_basic import fib')
cython_anno = timeit.timeit(f'fib({count})', setup='from fib_cython_annotated import fib')
cython_actual = timeit.timeit(f'fib({count})', setup='from fib_cython_actual import fib')
mypyc = timeit.timeit(f'fib({count})', setup='from fib_mypyc import fib')

print('onlypy:', onlypy)
print('cython_basic:', cython_basic, f'{onlypy / cython_basic:.5f}x')
print('cython_annotated:', cython_anno, f'{onlypy / cython_anno:.5f}x')
print('cython_actual:', cython_actual, f'{onlypy / cython_actual:.5f}x')
print('mypyc:', mypyc, f'{onlypy / mypyc:.5f}x')

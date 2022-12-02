from setuptools import setup
from Cython.Build import cythonize


setup(
    ext_modules=cythonize(['fib_cython_basic.py', 'fib_cython_annotated.py', 'fib_cython_actual.pyx'])
)

# Speed Test

A fun, probably unreliable microbenchmark to see some Python compilation methods and their speeds.
Running on my computer gets these results with a count of `100` in `times.py`:


```
onlypy: 2.9647939000005863
cython_basic: 2.1839042000001427 1.35757x
cython_annotated: 0.07778579999921931 38.11485x
cython_actual: 0.05594159999964177 52.99802x
mypyc: 3.0363961000002746 0.97642x
```

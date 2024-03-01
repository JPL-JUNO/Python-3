In [2]: %%timeit l = list(range(10))
   ...: l[5]
   ...:
   ...:
18.5 ns ± 0.598 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)

In [3]:

In [3]: %%timeit l = list(range(1_000_000))
   ...: l[10_000]
   ...:
   ...:
17.6 ns ± 0.47 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)

In [4]:
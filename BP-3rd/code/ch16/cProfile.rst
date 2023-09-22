>>> import cProfile
>>> from my_math1 import product
>>> cProfile.run("product(1, 2)")
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 my_math1.py:40(product)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

如果通过第二个参数向 run 提供一个文件名（如'my_math1.profile'），分析结果将保存到这个文件中

>>> # cProfile.run("product(1, 2)", "my_math1.profile")

然后，就可使用模块 pstats 来研究分析结果了

>>> import pstats
>>> p = pstats.Stats("my_math1.profile")
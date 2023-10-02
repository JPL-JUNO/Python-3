range(1, 5)
do_reduce(1, 2)
do_reduce(3, 3)
do_reduce(6, 4)
result: 10

do_reduce(99, 1)
do_reduce(100, 2)
do_reduce(102, 3)
do_reduce(105, 4)
result: 109

Single item in sequence: 1

do_reduce(99, 1)
Single item in sequence with initializer: 100

Empty sequence with initializer: 99

Error: reduce() of empty iterable with no initial value

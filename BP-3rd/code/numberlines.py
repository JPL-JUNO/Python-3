# numberlines.py                                   #  1
import fileinput                                   #  2
                                                   #  3
for line in fileinput.input(inplace=True):         #  4
    line = line.rstrip()                           #  5
    num = fileinput.lineno()                       #  6
    print('{:<50} # {:2d}'.format(line, num))      #  7

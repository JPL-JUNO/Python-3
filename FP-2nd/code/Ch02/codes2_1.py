"""
@Description: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-16 13:37:12
"""
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

for color in colors:
    for size in sizes:
        print((color, size))

tshirts = [(size, color) for size in sizes for color in colors]

symbols = 'ABCDEF'
tuple(ord(symbol) for symbol in symbols)
import array
array.array('I', (ord(symbol) for symbol in symbols))


for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)

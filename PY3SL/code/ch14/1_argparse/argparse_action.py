"""
@Title: 参数动作
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-12-04 21:24:40
@Description: 
"""

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-s', action='store', dest='simple_value',
                    help='Store a simple value')
parser.add_argument('-c', action='store_const', dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')
# -t, -f 选项被配置为修改不同的选项值，分别存储 True 或 False
parser.add_argument('-t', action='store_true',
                    default=False, dest='boolean_t',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=True,
                    dest='boolean_f', help='Set a switch to false')
parser.add_argument('-a', action='append',
                    dest='collection',
                    default=[],
                    help='Add repeated values to a list')
# -A, -B 的 dest 值相同，因此它们的常量值会被追加到同一个列表
parser.add_argument('-A', action='append_const',
                    dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add different values to list')
parser.add_argument('-B', action='append_const',
                    dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0')
results = parser.parse_args()
print('simple_value     = {!r}'.format(results.simple_value))
print('constant_value   = {!r}'.format(results.constant_value))
print('boolean_t        = {!r}'.format(results.boolean_t))
print('boolean_f        = {!r}'.format(results.boolean_f))
print('collection       = {!r}'.format(results.collection))
print('const_collection = {!r}'.format(results.const_collection))

"""
@Description: 元组不仅仅是不可变列表
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-20 13:29:43
"""

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, .66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
                ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    # tuple unpacking
    print('%s/%s' % passport) # %格式化运算符理解元组结构，把每一项当作不同的字段
    
for country, _ in traveler_ids:
    print(country)
    
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
assert a == b
b[-1].append(99)
assert a != b


def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True
tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])
assert fixed(tf) == True
assert fixed(tm) == False
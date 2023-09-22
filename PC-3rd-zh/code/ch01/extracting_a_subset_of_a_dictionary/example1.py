"""
@Title: 从字典中提取子集
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 15:08:42
@Description: 
"""
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Make a dictionary of all prices over 200✅
p1 = {key: value for key, value in prices.items() if value > 200}

# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}

# 字典推导式的方案更加清晰，而且实际运行起来也要快很多❌
p1 = dict((key, value) for key, value in prices.items() if value > 200)

# 计时测试表明这种解决方案几乎要比第一种慢上 1.6 倍。❌
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: prices[key] for key in prices.keys() & tech_names}

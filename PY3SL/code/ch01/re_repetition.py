"""
@Title: 重复
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 10:17:26
@Description: 
"""

# 模式中有5中表示重复的方法
# 1. 元字符 *，则表示重复 0 次或多次（运行一个模式重复 0 次是指这个模式即使不出现也可以出现匹配）
# 2. + ，那么模式必须至少出现 1 次才能匹配
# 3. ? 表示出现 0 次或 1 次
# 4. 如果需要指定出现次数，需要在模式后面使用 {m}，这里 m 是模式应重复的次数，
# 5. 如果要允许一个可变但有限的重复次数，那么可以使用 {m, n}，这里 m 是最小重复次数，n 是最大重复次数
# 如果省略 n ({m, }) 则表示值必须知道出现 m 次，但没有最大限制

from re_test_patterns import test_patterns
test_patterns(
    'abbaabbba',
    [("ab*", 'a followed by zero or more b'),
     ("ab+", "a followed by one or more b"),
     ("ab?", "a followed by zero or one b"),
     ("ab{3}", "a followed by three b"),
     ("ab{2,3}", "a followed by two to three b")]
)

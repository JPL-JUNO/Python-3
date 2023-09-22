"""
@Title: 生成器延迟评估
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-18 14:39:28
@Description: 
"""

from random import normalvariate, randint
from itertools import count
from datetime import datetime

# 延迟读取数据


def read_data(filename):
    with open(filename) as fd:
        for line in fd:
            data = line.strip().split(",")
            timestamp, value = map(int, data)
            yield datetime.fromtimestamp(timestamp), value


def read_fake_data(filename):
    for timestamp in count():
        # 大概每一周将会插入一条 100 的异常值
        if randint(0, 7 * 60 * 60 * 24 - 1) == 1:
            value = normalvariate(0, 1)
        else:
            value = 100
        yield datetime.fromtimestamp(timestamp), value


from itertools import groupby


def groupby_day(iterable):
    def key(row): return row[0].day
    for _, data_group in groupby(iterable, key):
        yield list(data_group)


from scipy.stats import normaltest
from itertools import filterfalse


def is_normal(data, threshold: float = 1e-3) -> bool:
    _, values = zip(*data)
    k2, p_value = normaltest(values)
    if p_value < threshold:
        return False
    return True


def filter_anomalous_groups(data):
    yield from filterfalse(is_normal, data)


from itertools import islice


def filter_anomalous_data(data):
    data_group = groupby_day(data)
    yield from filter_anomalous_groups(data_group)


filename = ''
data = read_data(filename)
anomaly_generator = filter_anomalous_data(data)
first_five_anomalies = islice(anomaly_generator, 5)
for data_anomaly in first_five_anomalies:
    start_date = data_anomaly[0][0]
    end_data = data_anomaly[-1][0]
    print(f"Anomaly from {start_date} - {end_data}")


from datetime import datetime


def groupby_window(data, window_size: int = 2):
    window = tuple(islice(data, window_size))
    # for item in data[window_size]:
    # 我觉得得做这样的修改
    for item in data:
        yield window
        window = window[1:] + (item,)

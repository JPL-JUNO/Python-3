"""
@File         : item19.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-04-20 19:45:51
@Email        : cuixuanstephen@gmail.com
@Description  : 当函数返回多个值时，切勿拆分三个以上的变量
"""


def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)

    return minimum, maximum


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

minimum, maximum = get_stats(lengths)  # Two return values
print(f"Min: {minimum}, Max: {maximum}")


def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled


longest, *middle, shortest = get_avg_ratio(lengths)
print(f"Longest:  {longest:>4.0%}")
print(f"Shortest: {shortest:>4.0%}")


def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count
    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2:
        median = sorted_numbers[middle]
    else:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    return minimum, maximum, average, median, count


minimum, maximum, average, median, count = get_stats(lengths)
print(f"Min: {minimum}, Max: {maximum}")
print(f"Average: {average}, Median: {median}, Count: {count}")

# Correct:
minimum, maximum, average, median, count = get_stats(lengths)

# Oops! Median and average swapped:
minimum, maximum, median, average, count = get_stats(lengths)

minimum, maximum, average, median, count = get_stats(lengths)

minimum, maximum, average, median, count = get_stats(lengths)
(minimum, maximum, average, median, count) = get_stats(lengths)
(minimum, maximum, average, median, count) = get_stats(lengths)

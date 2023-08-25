"""
@Title: 异序词检测示例
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-25 14:25:15
@Description: 如果一个字符串只是重排了另一个字符串的字符，那么这个字符串就是另一个的异序词
"""

# 为了简化问题，假设要检查的两个字符串长度相同，并且都是由 26 个英文字母的小写形式组成的。


def anagram_solution_checking_off(s1, s2):
    """
    清点第 1 个字符串的每个字符，看看它们是否都出现在第 2 个字符串中。如果是，那么两个
    字符串必然是异序词。清点是通过用 Python 中的特殊值 None 取代字符来实现的。
    对于 s1 中的 n 个字符，检查每一个时都要遍历 s2 中的 n 个字符。
    要匹配 s1 中的一个字符，列表中的 n 个位置都要被访问一次。因此，访问次数就成了从 1 到 n
    的整数之和。
    这个方案的时间复杂度是 O(n^2)
    """
    a_list = list(s2)
    pos_1 = 0
    still_ok = True
    while pos_1 < len(s1) and still_ok:
        pos_2 = 0
        found = False
        while pos_2 < len(a_list) and not found:
            if s1[pos_1] == a_list[pos_2]:
                found = True
            else:
                pos_2 = pos_2 + 1
        if found:
            a_list[pos_2] = None
        else:
            still_ok = False
        pos_1 = pos_1 + 1
    return still_ok


def anagram_solution_sort(s1, s2):
    """
    如果按照字母表顺序给字符排序，异序词得到的结果将是同一个字符串。
    调用两次 sort 方法不是没有代价
    排序的时间复杂度基本上是 O(n^2) 或者 O(nlogn)
    """
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()
    a_list2.sort()

    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if a_list1[pos] == a_list2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches


def anagram_solution_brute_force(s1, s2):
    """
    蛮力解决问题的方法基本上就是穷尽所有的可能。就异序词检测问题而言，可以用 s1 中
    的字符生成所有可能的字符串，看看 s2 是否在其中。
    """
    pass


def anagram_solution_count(s1, s2):
    """
    最后一个方案基于这样一个事实：两个异序词有同样数目的 a、同样数目的 b、同样数目
    的 c，等等。要判断两个字符串是否为异序词，先数一下每个字符出现的次数。因为字符可能有
    26 种，所以使用 26 个计数器，对应每个字符。每遇到一个字符，就将对应的计数器加 1。最后，
    如果两个计数器列表相同，那么两个字符串肯定是异序词
    这种方法的复杂度是 T(n) = 2n + 26，即 O(n)
    """
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(s1):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok

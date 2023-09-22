"""
@Description: 接卸 iTunes 播放列表
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-19 10:07:21
"""
import plistlib
import numpy as np
import matplotlib.pyplot as plt
import argparse


def get_plist(file_name):
    with open(file_name, 'rb') as fp:
        plist = plistlib.load(fp)
    return plist


def find_duplicates(file_name: str) -> None:
    """查找重复并提取重复至文件中"""
    print("Finding duplicate tracks in %s..." % file_name)
    # 读取一个播放列表
    # plist = plistlib.readPlist(file_name)  # 被弃用
    plist = get_plist(file_name)
    # get the tricks from the Tracks dictionary
    tracks = plist["Tracks"]
    track_names: dict[str:tuple] = {}
    for _, track in tracks.items():
        try:
            # 获取字典中每个音轨的名称和市场
            name = track["Name"]
            duration = track["Total Time"]
            # 检查当前乐曲的名称是否已在被构建的字典中
            if name in track_names:
                # 将每个音轨的长度除以1000，由毫秒转为秒，并四舍五入到最近的秒，以进行检查
                # 这意味着，只有毫秒差异的两个音轨被认为是相同的
                if duration // 1000 == track_names[name][0] // 1000:
                    count = track_names[name][1]
                    track_names[name] = (duration, count + 1)
            else:
                # 如果程序第一次遇见音轨的名称，就创建一个新条目
                track_names[name] = (duration, 1)
        except:
            pass

    dups = []
    for k, v in track_names.items():
        if v[1] > 1:
            dups.append((v[1], k))
    if len(dups) > 0:
        print("Found %d duplicates. Track names saved to tup.txt" % len(dups))
    else:
        print("No duplicate track found!")
    f = open("dups.txt", "w")
    for val in dups:
        f.write("[%d] %s\n" % (val[0], val[1]))
    f.close()
    # with open("dups.txt", "w") as f:
    #     for val in dups:
    #         f.write("[%d] %s\n" % (val[0], val[1]))


def find_common_tracks(file_names: list[str]):
    # 保存从每个播放列表创建的一组对象
    track_names_sets = []
    for file_name in file_names:
        track_names = set()
        plist = get_plist(file_name)
        # plist = plistlib.readPlist(file_name)
        tracks = plist["Tracks"]
        for _, track in tracks.items():
            try:
                track_names.add(track["Name"])
            except:
                pass
        track_names_sets.append(track_names)
    # 获取集合直接按共同音轨的集合，python * 运算符可以展开参数列表
    common_tracks = set.intersection(*track_names_sets)
    if len(common_tracks) > 0:
        f = open("common.txt", 'wb')
        for val in common_tracks:
            s = "%s\n" % val
            f.write(s.encode("UTF-8"))
        f.close()
        print("%d common tracks found. Track names written to common.txt." %
              len(common_tracks))
    else:
        print("No common tracks!")


def plot_stats(file_name):
    # plist = plistlib.readPlist(file_name)
    plist = get_plist(file_name)
    tracks = plist["Tracks"]
    # 保存评分和时长，在 iTunes 播放列表中，评分是一个整数，范围是[0，100]
    ratings = []
    durations = []

    for _, track in tracks.items():
        try:
            ratings.append(track["Album Rating"])
            durations.append(track["Total Time"])
        except:
            pass
    # if [] in (ratings, durations):
    if ratings == [] or durations == []:
        print("No valid Album Rating/Total Time data in %s." % file_name)
        return
    x = np.array(durations, np.int32)
    # 转换成分钟
    x = x / 60000.0
    y = np.array(ratings, np.int32)
    plt.subplot(2, 1, 1)
    plt.plot(x, y, 'o')
    plt.axis([0, 1.05 * np.max(x), -1, 110])
    # plt.xlabel("Track duration")
    plt.ylabel("Track rating")

    plt.subplot(2, 1, 2)
    plt.hist(x, bins=20)
    plt.xlabel("Track duration")
    plt.ylabel("Count")
    plt.show()


def main():
    desc_str = """
    This program analyzes playlist files (.xml) exported from iTunes
    """
    parser = argparse.ArgumentParser(description=desc_str)
    # 该程序可以做三件不同的事情，如发现播放列表之间的共同
    # 音轨，绘制统计数据，或发现播放列表中重复的曲目。但是，一个时间程序只能做
    # 其中一件事，如果用户决定同时指定两个或多个选项，我们不希望它崩溃。argparse
    # 模块为这个问题提供了一个解决方案，即相互排斥的参数分组。
    group = parser.add_argument_group()

    # 命令行选项，并输入应该将解析值存入的变量名
    group.add_argument("--common", nargs="*", dest="plFiles", required=False)
    group.add_argument("--stats", dest="plFile", required=False)
    group.add_argument("--dup", dest="plFileD", required=False)

    # 实际解析
    args = parser.parse_args()

    if args.plFiles:
        find_common_tracks(args.plFiles)
    elif args.plFile:
        plot_stats(args.plFile)
    elif args.plFileD:
        find_duplicates(args.plFileD)
    else:
        print("These are not the tracks you are looking for.")


if __name__ == "__main__":
    main()

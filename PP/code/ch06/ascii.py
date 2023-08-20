"""
@Description: ASCII 文本图形
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-20 11:19:05
"""
from PIL import Image
import numpy as np
import sys
import random
import argparse
import math


# 70级的灰度梯度
g_scale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10级的灰度梯度
g_scale2 = "@%#*+=-:. "


def convert_image_to_ascii(file_name, cols, scale, more_levels):
    # Image.open() 打开输入图像文件，Image.convert() 将该图像转换为灰度
    # 图像。“L”代表 luminance，是图像亮度的单位。
    image = Image.open(file_name).convert("L")
    W, H = image.size[0], image.size[1]
    w = W / cols
    # 利用垂直比例系数（作为 scale 传入），计算它的高度
    h = w / scale
    # 用这个网格高度来计算行数
    rows = int(H / h)

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    # ASCII 图像先作为一个字符串列表保存
    a_img = []
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        if j == rows - 1:
            y2 = H
        a_img.append("")
        for i in range(cols):
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            if i == cols - 1:
                x2 = W
            img = image.crop((x1, y1, x2, y2))
            avg = int(get_average_L(img))
            if more_levels:
                g_s_val = g_scale1[int((avg * 69) / 255)]
            else:
                g_s_val = g_scale2[int((avg * 9) / 255)]
            # 在 j 行进行追加
            # 在文本行中添加找到的 ASCII 值 gsval，代码循环，
            # 直到处理完所有行。
            a_img[j] += g_s_val
    return a_img


def get_average_L(image):
    """计算灰度图像中每一小块的平均亮度"""
    # 图像小块作为 PIL Image 对象传入
    im = np.array(image)
    w, h = im.shape
    # np.average(w * h)
    return np.average(im.reshape(w * h))


def main():
    desc_str = """This program coverts an image into ASCII art."""
    parser = argparse.ArgumentParser(description=desc_str)

    parser.add_argument("--file", dest="img_file", required=True)
    parser.add_argument("--scale", dest="scale", required=False)
    parser.add_argument("--out", dest="out_file", required=False)
    parser.add_argument("--cols", dest="cols", required=False)
    parser.add_argument("--more_levels", dest="more_levels",
                        action="store_true")

    args = parser.parse_args()

    img_file = args.img_file
    out_file = "out.txt"
    if args.out_file:
        out_file = args.out_file
    scale = .43
    if args.scale:
        scale = float(args.scale)
    cols = 80
    if args.cols:
        cols = int(args.cols)
    print("Generating ASCII art...")

    a_img = convert_image_to_ascii(img_file, cols, scale, args.more_levels)
    f = open(out_file, 'w')
    for row in a_img:
        f.write(row + '\n')
    f.close()

    print("ASCII art written to %s" % out_file)


if __name__ == '__main__':
    main()

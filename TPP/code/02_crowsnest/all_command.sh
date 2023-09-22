mkdir 02_crowsnest

cd 02_crowsnest

# make test
pytest -xv test.py

# 使用模板来生成文件
python bin/new.py 02_crowsnest/crowsnest.py

# 执行一些测试
pytest -xv test.py

python crowsnest.py -h
# usage: crowsnest.py [-h] word

# Crow's Nest -- choose the correct article

# positional arguments:
#   word        A word
# 你需要定义一个单词参数，这是一个位置参数
# options:
#   -h, --help  show this help message and exit
# -h, --help 是由 argparse 自动生成的参数，可以用来创建文档

python crowsnest.py narwhal
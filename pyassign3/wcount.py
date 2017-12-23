"""wcount.py: count words from an Internet file.

__author__ = "Dengjiameng"
__pkuid__  = "1700011718"
__email__  = "counterd@pku.edu.cn"
"""

import sys
import re
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """

    # your code goes here
    dir = {} # 新建字典表
    lines = lines.lower()  # 大写转小写
    words = re.findall(r'[a-z]+',lines) # 找出文本中所有单词
    for letter in words: # 统计各单词出现频率
       if letter in dir:
         dir[letter] += 1
       else:
         dir[letter] = 1
    dict = sorted(dir.items(), key=lambda e:e[1], reverse=True)  # 按值排序 降序
    dt = {}
    for (m,n) in dict:  # 将包含元组的list转换为字典表
        dt.setdefault(m,[]).append(n)
    count = 0
    for key, value in dt.items():
        count += 1
        ss = value[0]
        var = key+"\t\t\t"+str(ss)
        print(var)
        if count == topn:
            break

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
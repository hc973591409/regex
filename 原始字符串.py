import re


def r_string():
    mm = "c:\\a\\b\\c"
    print(mm)
    # c:\a\b\c
    m = re.match("c:\\\\", mm)
    # 非原始字符串，所以匹配的时候，单斜杠要处理成双斜杠
    print(m.group())
    # c:\
    # 使用原始字符串，只需要在匹配规则前面加r就可以
    r_m = re.match(r"c:\\", mm)
    print(r_m.group())

# Python中字符串前⾯加上 r 表示原⽣字符串 ，
# >>c:\a\b\c
# >>c:\
# >>c:\


def main():
    r_string()


if __name__ == '__main__':
    main()

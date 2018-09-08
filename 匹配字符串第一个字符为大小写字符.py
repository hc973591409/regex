# 示例1：
# 需求：匹配出，⼀个字符串第⼀个字⺟为⼤⼩字符，后⾯都是⼩写字⺟并且
# 这些⼩写字⺟可有可⽆
import re


def regex_1():
    res = re.match(r"[A-Z][a-z]*", 'Mm')
    print(res.group())
    res = re.match(r"[A-Z][a-z]*", 'M')
    print(res.group())

# 需求：匹配出，变量名是否有效


def regex_2():
    res = re.match(r"[A-Za-z_]+[\w_]", 'name')
    print(res.group())
    res = re.match(r"[A-Za-z_]+[\w_]", '__name')
    print(res.group())
    res = re.match(r"[A-Za-z_]+[\w_]", '1__name')
    print(res.group())

# 匹配数字 0-99


def regex_3():
    res = re.match(r"[1-9]?[\d]$", '10')
    print(res.group())
    res = re.match(r"[1-9]?[\d]$", '8')
    print(res.group())
    res = re.match(r"[1-9]?[\d]$", '9')
    print(res.group())
# 需求：匹配出，8到20位的密码，可以是⼤⼩写英⽂字⺟、数字、下划线


def regex_4():
    res = re.match(r"[\w]{8,20}", 'hu_af1afdsfaf')
    print(res.group())
    res = re.match(r"[\w]{8,20}", '1ad12f23s34455ff66')
    print(res.group())


# 题⽬1：匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
def regex_email():
    pattern = r'[\w]{4,20}@163.com'
    res = re.match(pattern, '_9_h1asdfj@163.com')
    print(res.group())


def regex_5():
    res = re.match(r".*\bver\b", 'ho ver abc')
    print(res.group())
    res = re.match(r".*\Bver\B", 'hoverabc')
    print(res.group())

# 匹配0-100导入任意数字


def regex_6():
    pattern = re.compile(r'[1-9]?\d$|100$')
    res = re.match(pattern, '99')
    print(res.group())

# 需求：匹配出163、126、qq邮箱之间的数字


def regex_7():
    pattern = re.compile(r'\w{4,20}@(126|163|qq)\.(com|cn)')
    res = re.match(pattern, '973591409@qq.com')
    print(res.group())

# 需求：html  小括号匹配分组


def regex_8():
    pattern = re.compile(r'<(\w+)><(\w+)>(.*)</\2></\1>')
    res = re.match(pattern, '<h1><p>这是一个测试网页</p></h1>')
    print(res.groups())

# 需求：(?P<name>) 分组起别名   (?P=name) 引⽤别名为name分组匹配到的字符串


def regex_9():
    pattern = re.compile(
        r'<(?P<key1>\w+)><(?P<key2>\w+)>(.*)</(?P=key2)></(?P=key1)>')
    res = re.match(pattern, '<h1><p>这是一个测试网页</p></h1>')
    print(res.groups())


def main():
    regex_9()


if __name__ == '__main__':
    main()

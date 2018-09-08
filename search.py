# 需求：匹配出⽂章阅读的次数
import re

def regex_1():
    pattern = re.compile(r'\d+')
    res = re.search(pattern, "文章的阅读量为9999")
    print(res.group())

def regex_2():
    pattern = re.compile(r'\d+')
    res = re.findall(pattern, "python = 9999, c = 7890, c++ = 12345")
    print(res)

def regex_3():
    pattern = re.compile(r'\d+')
    res = re.sub(pattern, "998", 'python = 997')
    # 返回替换后的字符串
    print(res)

def add(tmp):
    num = int(tmp.group())
    num += 10
    return str(num)

def regex_4():
    pattern = re.compile(r'\d+')
    res = re.sub(pattern, add, 'python = 997')
    # 返回替换后的字符串
    print(res)

def regex_5():
    string = '''<div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接⼝、后台等服务器端相关⼯作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的⾃我驱动⼒和职业素养，⼯作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、⼀年以上 Python 开发经验，掌握⾯向对象分析和设计，了解设计模式</p
>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使⽤ MySQL/PostgreSQL 中
的⼀种<br></p>
<p>4、掌握NoSQL、MQ，熟练使⽤对应技术解决⽅案</p>
re模块的⾼级⽤法
33
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>⼤数据，数理统计，机器学习，sklearn，⾼性能，⼤并发。</p>
</div>
'''
    pattern = re.compile(r"<p>(.*)</p>")
    res = re.findall(pattern, string)
    for text in res:
        print(text)

def regex_6():
    pattern = re.compile(r':| |#')
    string = 'sfaisd:wafs fasdf # f9w38r # password'
    str_list = re.split(pattern, string)
    print(str_list)

# 用？去除贪婪模式
def regex_7():
    string='''<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/\
1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/\
11/13/1213973_201611131917_small.jpg" style="display: inline;">'''
    print(string)
    pattern = re.compile(r'https:.*?.jpg')
    res = re.findall(pattern, string)
    print(res)

def regex_8():
    string  = '''http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
'''
    pattern = re.compile(r"http://.*?/")
    res = re.findall(pattern, string)
    for url in res:
        print(url)

def main():
    regex_8()

if __name__ == '__main__':
    main()



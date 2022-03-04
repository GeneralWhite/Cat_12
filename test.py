# 首先我们导入 requests 和 BeautifulSoup库
import requests
from bs4 import BeautifulSoup
#   123
for i in range(10):
    url = 'http://58921.com/alltime/wangpiao?page=' + str(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3776.400 QQBrowser/10.6.4212.400'
        }
    # 通过 requests 的 get 方法请求该网页
    r = requests.get(url = url, headers = headers)
    r.encoding = 'utf-8'  # 防止出现乱码
    html = r.text  # 以文本的形式将代码搞下来
    soup = BeautifulSoup(html, 'html.parser')
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')
    for tr in trs:
        # 我们已经定位到了 tr 标签，电影信息都存放在 tr 标签中
        tds = tr.find_all('td')
        pm = tds[0].string
        bt = tds[1].string
        zcc = tds[3].string
        with open('电影票房.txt', 'a', encoding = 'utf-8') as fp:
            fp.write(pm + '-' + bt + '-' + zcc + '\n')
        print(pm + '-' + bt + '-' + zcc)

# 将总网票房前五的电影的总场次做成柱状图
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

for i in range(1):
    url = 'http://58921.com/alltime/wangpiao?page=' + str(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3776.400 QQBrowser/10.6.4212.400'
        }
    r = requests.get(url = url, headers = headers)
    r.encoding = 'utf-8'  # 防止出现乱码
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')
    y = []
    x = []
    for tr in trs:
        tds = tr.find_all('td')
        pm = tds[0].string
        bt = tds[1].string
        zcc = tds[3].string
        x.append(bt)
        y.append(float(zcc[:-1]))
    matplotlib.rcParams['font.family'] = 'SimHei'
    N = 5
    z = y[:5]
    x1 = np.arange(N)
    str1 = x[:5]
    # 绘图 横轴是电影名称 纵轴是播放的总场次
    p1 = plt.bar(x1, height = z, width = 0.25, label = "总场次", tick_label = str1)
    # 添加数据标签
    for a, b in zip(x1, z):
        plt.text(a, b, '%.0f' % b, ha = 'center', va = 'bottom', fontsize = 10)
    # 添加图例
    plt.legend()
    # 展示图形
    plt.show()

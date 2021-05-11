import pandas as pd
import requests
from lxml import etree
import re
import time
import random
import csv

headers = {
    'Referer': 'http://wlwz.changsha.gov.cn/',
    'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'

}
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
headers['User-Agent'] = random.choice(user_agent_list)

total_adr = []
# 设置爬取页数范围，容易被封ip，区间可以调小点
for i in range(0, 500):
    url = f'http://wlwz.changsha.gov.cn/webapp/cs2020/email/index.jsp?cflag=1&emailList.offset={0 + i * 13}&emailList.desc=false'
    html = requests.get(url, headers=headers)
    time.sleep(0.5)
    print(f'正在获取第{i}页...')
    try:
        parse = etree.HTML(html.text)
        adr_list = parse.xpath('/html/body//div/div/table//tr/td[2]/a/@href')
        #         print(adr_list)
        total_adr.extend(adr_list)
    except Exception as e:
        print(e)
        continue
print('finished!!')

# 新建csv，设置csv名称及格式
csvf = open('cs_city0-500信箱w.csv', 'a+', encoding='utf-8', newline='')
fieldnames = ['公民诉求文本', '公民诉求提交时间', '回复部门', '处理时间', '政府回应文本', '主题名称']
writer = csv.DictWriter(csvf, fieldnames=fieldnames)
writer.writeheader()
regex = '<td class="td_label2">(.*?)</td>'
pattern = re.compile(regex, re.S)

for i in range(len(total_adr)):
    url = f'http://wlwz.changsha.gov.cn{total_adr[i]}'
    print(url)
    time.sleep(0.5)

    html2 = requests.get(url).text

    content = pattern.findall(html2)

    # peopletext
    # 去除html标签
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', content[2].strip())
    peopletext = dd.replace('&nbsp;', '')
    peopletext = peopletext.replace('\r\n', '')
    peopletext = peopletext.replace('\t', '')

    p_time = content[1]
    slove_place = content[4]
    slove_time = content[3]
    # 简单的数据清洗
    govreply = content[5].strip()
    dr2 = re.compile(r'<[^>]+>', re.S)
    govreply = dr.sub('', govreply)
    govreply = govreply.replace('\r\n\t\t\t\t\r\n', '')
    govreply = govreply.replace('\n', '')
    govreply = govreply.replace('满意度', '')
    govreply = govreply.replace('&nbsp;', '')
    govreply = govreply.replace(' ', '')

    theme = content[0]

    data = {

        '公民诉求文本': peopletext,
        '公民诉求提交时间': p_time,
        '回复部门': slove_place,
        '处理时间': slove_time,
        '政府回应文本': govreply,
        '主题名称': theme,
    }
    # 存入csv

    writer.writerow(data)

print('ok!!')

# #关闭csvf
csvf.close()
 
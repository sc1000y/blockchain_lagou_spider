#!/usr/bin/env python
# encoding=utf-8

import json
import requests
import xlwt
import time
from lxml import etree
import random
from fake_useragent import UserAgent
import sys
import csv


#获取存储职位信息的json对象，遍历获得公司名、福利待遇、工作地点、学历要求、工作类型、发布时间、职位名称、薪资、工作年限
def get_json(url,datas):

    ua = UserAgent()
    my_headers = {'User-Agent': ua.random,
            'Host':'www.lagou.com',
'Connection': 'keep-alive',
'Content-Length': '46',
'Origin': 'https://www.lagou.com',
'X-Anit-Forge-Code': '0',
#'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'X-Requested-With': 'XMLHttpRequest',
'X-Anit-Forge-Token': 'None',
'Referer': 'https://www.lagou.com/jobs/list_%E5%8C%BA%E5%9D%97%E9%93%BE?px=default&city=%E5%8C%97%E4%BA%AC',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language':'en-US,en;q=0.9'}
    cookies={
'Cookie': 'JSESSIONID=ABAAABAACEBACDGC64B9ED223689E9891B25C1224EEC9B8; _ga=GA1.2.1941849206.1531218458; _gid=GA1.2.2089849367.1531218458; user_trace_token=20180710182739-df2acc9f-842b-11e8-993d-5254005c3644; LGSID=20180710182739-df2acf1c-842b-11e8-993d-5254005c3644; LGUID=20180710182739-df2ad1e7-842b-11e8-993d-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531218458; index_location_city=%E5%8C%97%E4%BA%AC; X_HTTP_TOKEN=c8e190ab14ed1fe2e576ce24ad50062e; _gat=1; TG-TRACK-CODE=index_navigation; LGRID=20180710192215-7f954b85-8433-11e8-993d-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531221734; SEARCH_ID=683756ed08234452bfffd7ce52457839'
}

    time.sleep(20 + random.randint(0,20))
    content = requests.post(url=url,cookies=cookies,headers=my_headers,data=datas)
    # content.encoding = 'utf-8'
    result = content.json()
    print(result)
    info = result['content']['positionResult']['result']
    # print info
    info_list = []
    for job in info:
        information = []
        information.append(job['positionId']) #岗位对应ID
        information.append(job['companyFullName']) #公司全名
        information.append(job['companyLabelList']) #福利待遇
        information.append(job['district']) #工作地点
        information.append(job['education']) #学历要求
        information.append(job['firstType']) #工作类型
        information.append(job['formatCreateTime']) #发布时间
        information.append(job['positionName']) #职位名称
        information.append(job['salary']) #薪资
        information.append(job['workYear']) #工作年限
        arr=split_price(job['salary'])
        information.append(arr[0])
        information.append(arr[1])
        info_list.append(information)
        #将列表对象进行json格式的编码转换,其中indent参数设置缩进值为2
        print(json.dumps(info_list,ensure_ascii=False,indent=2))
        print(info_list)
    return info_list


def main():
    page = 8#int(input('输入抓取页数:'))
    # kd = raw_input('请输入你要抓取的职位关键字：')
    # city = raw_input('请输入你要抓取的城市：')
    info_result = []
    title = ['岗位id','公司全名','福利待遇','工作地点','学历要求','工作类型','发布时间','职位名称','薪资','工作年限','','']
    info_result.append(title)
    for x in range(1,page+1):
        #url = 'https://www.lagou.com/jobs/positionAjax.json.json?px=new&needAddtionalResult=false'
        url='https://www.lagou.com/jobs/positionAjax.json?jd=%E4%B8%8D%E9%9C%80%E8%A6%81%E8%9E%8D%E8%B5%84&px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
        datas = {
            'first': True,
            'pn': x,
            'kd':'区块链',
            'px':'default',
        }
        info = get_json(url,datas)
        info_result = info_result+info
        out = open('C:\\work\\python\\lagouzp.csv','a', newline='',encoding='utf-8-sig')
        csv_write = csv.writer(out,dialect='excel')
        csv_write.writerows(info_result)
        
def split_price(str):
    nu=['','']
    arr=str.split("-")
    if len(arr)==2:
        return arr
    else:
        return nu
if __name__ == '__main__':
    main()



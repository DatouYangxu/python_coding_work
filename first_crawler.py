"""
第一个爬虫
"""
#1.导入库
import requests #用来访问网页
from bs4 import BeautifulSoup #用来解析网页内容
import pandas as pd
#2.定义爬虫函数
def crawl_zol():
    #要爬取的网页地址
    url = "https://nb.zol.com.cn/yxb/"
    #设置请求头，模拟浏览器访问
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0'
    }
    #3。发送请求
    response = requests.get(url,headers=headers)
    response.encoding= 'gb2312'#设置编码
    #4.解析HTML
    soup = BeautifulSoup(response.text,'lxml')
    #5。提取数据
    laptops=[]
    #找到所有笔记本项
    items = soup.select('#stations_t li')

    for item in items[:5]:#只选取前五个
        try:
            #提取笔记本名称
            name_elem = item.select_one('name-l')
            name=name_elem.text.strip() if name_elem else "未知"

            #提取价格
            price_elem=item.select_one('money_r')
            price=price_elem.text.strip() if price_elem else "未知"

            #保存到列表
            laptops.append({
                '名称':name,
                '价格':price
            })
        except:
            continue#如果出错，跳过这个项

    #6.保存数据
    df = pd.DataFrame(laptops)
    df.to_csv('笔记本数据.csv',index=False,encoding='utf-8-sig')
    print(f"爬取完成！共保存了{len(df)}条数据")

    return df
#7.运行爬虫
if __name__ == '__main__':
    data = crawl_zol()
    print(data.head())#显示前五行数据
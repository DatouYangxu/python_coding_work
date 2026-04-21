import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def crawl_zol_laptops(pages=3):
    """爬取中关村在线笔记本数据"""
    base_url = "https://detail.zol.com.cn/notebook_advSearch/subcate16_{}_market-false.html"
    
    all_laptops = []
    
    for page in range(1, pages + 1):
        print(f"正在爬取第{page}页...")
        
        # 1. 发送请求
        url = base_url.format(page)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers)
        response.encoding = 'gb2312'  # 重要：ZOL使用gb2312编码
        
        # 2. 解析HTML
        soup = BeautifulSoup(response.text, 'lxml')
        
        # 3. 提取数据（需要根据实际页面调整选择器）
        products = soup.select('.list-box .list-item')
        
        for product in products:
            try:
                # 提取基本信息
                name_elem = product.select_one('.pro-info .name a')
                price_elem = product.select_one('.price .price-type')
                
                if name_elem and price_elem:
                    laptop = {
                        '名称': name_elem.text.strip(),
                        '价格': price_elem.text.strip(),
                        '链接': 'https:' + name_elem['href'] if name_elem.get('href') else ''
                    }
                    all_laptops.append(laptop)
            except:
                continue
        
        # 礼貌延迟
        time.sleep(2)
    
    # 4. 保存数据
    df = pd.DataFrame(all_laptops)
    df.to_csv('zol_laptops.csv', index=False, encoding='utf-8-sig')
    print(f"爬取完成，共{len(df)}条数据")
    
    return df

# 运行爬虫（爬3页，约30-45条数据，足够比赛使用）
if __name__ == '__main__':
    crawl_zol_laptops(pages=3)
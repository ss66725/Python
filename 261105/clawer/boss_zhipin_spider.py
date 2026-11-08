#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BOSS直聘员工点评数据采集脚本
================================
使用方法：
1. 在本地浏览器登录 BOSS直聘 (https://www.zhipin.com)
2. 按 F12 打开开发者工具 -> Network 标签
3. 刷新页面，找到任意一个 API 请求（如 joblist.json）
4. 复制请求头中的 Cookie 值
5. 将 Cookie 粘贴到脚本底部的 YOUR_COOKIE_HERE 位置
6. 运行脚本：python boss_zhipin_spider.py

注意：
- BOSS直聘有较强反爬机制，建议在本地运行（有登录态的浏览器环境）
- 脚本已加入随机延迟和错误重试机制
- 采集数据保存在 Comment.xlsx 文件中
"""

import requests
import json
import time
import random
import re
from bs4 import BeautifulSoup
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from urllib.parse import urlencode

# ==================== 配置区域 ====================

# 【重要】在此粘贴你的BOSS直聘Cookie（从浏览器开发者工具中获取）
YOUR_COOKIE = 'YOUR_COOKIE_HERE'

# 目标公司列表（按用户要求的分类）
COMPANIES = {
    "深圳本地": ["华为", "比亚迪", "汇川技术", "越疆科技", "优必选", "大疆创新"],
    "国产机器人龙头": ["埃斯顿", "新松机器人", "埃夫特", "珞石机器人", "李群自动化"],
    "智能装备/集成": ["明珞装备", "华工科技", "瑞松科技"],
    "外资四大家族": ["发那科", "ABB", "库卡", "安川电机"],
}

# 目标城市代码（深圳）
CITY_CODE = "101220100"

# 请求配置
REQUEST_TIMEOUT = 15
MAX_RETRIES = 3
REQUEST_DELAY = (2, 5)  # 随机延迟2-5秒

# ==================== 核心爬虫类 ====================

class BossZhiPinSpider:
    """BOSS直聘爬虫类"""
    
    def __init__(self, cookie):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://www.zhipin.com/',
            'Cookie': cookie,
        })
        self.base_url = 'https://www.zhipin.com'
        
    def get(self, url, params=None, headers=None):
        """发送GET请求，带重试机制"""
        for attempt in range(MAX_RETRIES):
            try:
                resp = self.session.get(
                    url, 
                    params=params, 
                    headers=headers,
                    timeout=REQUEST_TIMEOUT,
                    allow_redirects=True
                )
                # 检查是否被反爬
                if '安全验证' in resp.text or 'verify' in resp.url:
                    print(f"  [警告] 触发安全验证，可能需更新Cookie")
                    return None
                    
                if resp.status_code == 200:
                    return resp
                elif resp.status_code == 403:
                    print(f"  [警告] 403禁止访问，等待后重试...")
                elif resp.status_code == 429:
                    print(f"  [警告] 请求过于频繁，等待更长时间...")
                    
            except requests.exceptions.Timeout:
                print(f"  [超时] 第{attempt+1}次尝试失败")
            except requests.exceptions.ConnectionError:
                print(f"  [连接错误] 第{attempt+1}次尝试失败")
            except Exception as e:
                print(f"  [错误] {e}")
                
            if attempt < MAX_RETRIES - 1:
                delay = random.randint(5, 15)
                print(f"  等待{delay}秒后重试...")
                time.sleep(delay)
                
        print(f"  [失败] 达到最大重试次数")
        return None
        
    def search_company(self, company_name):
        """搜索公司，返回公司ID和基本信息"""
        url = f'{self.base_url}/wapi/zpgeek/search/company.json'
        params = {
            'query': company_name,
            'city': CITY_CODE,
        }
        
        print(f"\n[搜索公司] {company_name}")
        resp = self.get(url, params=params)
        if not resp:
            return None
            
        try:
            data = resp.json()
            if data.get('code') != 0:
                print(f"  [API错误] code={data.get('code')}, msg={data.get('message')}")
                return None
                
            zpData = data.get('zpData', {})
            companies = zpData.get('companyList', [])
            if companies:
                company = companies[0]
                company_id = company.get('companyId')
                company_name_full = company.get('companyName', company_name)
                print(f"  [找到] {company_name_full} (ID: {company_id})")
                return {
                    'id': company_id,
                    'name': company_name_full,
                    'logo': company.get('logo', ''),
                    'scale': company.get('scaleName', ''),
                    'industry': company.get('industry', ''),
                }
            else:
                print(f"  [未找到] 未找到公司: {company_name}")
                return None
        except json.JSONDecodeError:
            print(f"  [解析错误] 无法解析JSON响应")
            return None
            
    def get_company_reviews(self, company_id, company_name):
        """获取公司员工点评（尝试多个API端点）"""
        reviews = []
        
        # 方法1: 尝试评论API
        review_endpoints = [
            f'{self.base_url}/wapi/zpgeek/company/reviews',
            f'{self.base_url}/wapi/zpgeek/compass/reviews',
            f'{self.base_url}/wapi/zpgeek/company/comment',
        ]
        
        for endpoint in review_endpoints:
            print(f"\n  [尝试API] {endpoint}")
            params = {'companyId': company_id, 'page': '1', 'pageSize': '20'}
            resp = self.get(endpoint, params=params)
            
            if not resp:
                continue
                
            try:
                data = resp.json()
                if data.get('code') == 0:
                    zpData = data.get('zpData', {})
                    # 尝试不同的数据结构
                    comments = zpData.get('comments', zpData.get('reviews', zpData.get('list', [])))
                    if comments:
                        print(f"  [成功] 获取到 {len(comments)} 条评论")
                        for comment in comments:
                            review = self.parse_review(comment)
                            if review:
                                reviews.append(review)
                        return reviews
                    else:
                        print(f"  [无数据] API返回结构: {list(data.keys())}")
                        # 打印完整响应以便调试
                        print(f"  [调试] zpData keys: {list(zpData.keys()) if zpData else 'empty'}")
                else:
                    print(f"  [API错误] code={data.get('code')}, msg={data.get('message')}")
            except json.JSONDecodeError:
                print(f"  [解析错误] 无法解析JSON")
            except Exception as e:
                print(f"  [错误] {e}")
                
        # 方法2: 尝试通过公司主页HTML解析
        print(f"\n  [尝试HTML解析] 访问公司主页")
        company_url = f'{self.base_url}/company/{company_id}'
        resp = self.get(company_url)
        if resp and '员工评价' in resp.text:
            print(f"  [发现] 公司主页包含员工评价内容")
            # 这里可以添加HTML解析逻辑
            # 由于BOSS直聘动态加载，HTML中可能不含完整评论数据
            
        return reviews
        
    def parse_review(self, comment):
        """解析单条评论数据"""
        try:
            # 尝试提取各字段（根据不同API结构的适配）
            job_info = comment.get('jobName', comment.get('position', comment.get('job', '')))
            user_name = comment.get('userName', comment.get('nickname', comment.get('author', '')))
            read_num = comment.get('readCount', comment.get('readNum', comment.get('views', '')))
            content = comment.get('content', comment.get('comment', comment.get('text', '')))
            
            # 清理内容
            content = content.strip() if content else ''
            job_info = job_info.strip() if job_info else ''
            user_name = user_name.strip() if user_name else '匿名用户'
            
            # 格式化阅读量
            if read_num and isinstance(read_num, (int, float)):
                read_num = f'{int(read_num)}阅读'
            elif not read_num:
                read_num = ''
                
            return {
                '岗位': job_info,
                'user-name': user_name,
                'read-num': read_num,
                'content': content,
            }
        except Exception as e:
            print(f"  [解析错误] {e}")
            return None
            
    def search_reviews_by_keyword(self, keyword, max_results=20):
        """通过关键词搜索员工点评（牛人社区等）"""
        reviews = []
        url = f'{self.base_url}/wapi/zpgeek/search/issue.json'
        
        params = {
            'query': f'{keyword} 员工评价',
            'page': '1',
            'pageSize': str(max_results),
        }
        
        print(f"\n[关键词搜索] {keyword}")
        resp = self.get(url, params=params)
        if not resp:
            return reviews
            
        try:
            data = resp.json()
            if data.get('code') == 0:
                zpData = data.get('zpData', {})
                issues = zpData.get('issues', zpData.get('list', []))
                print(f"  [找到] {len(issues)} 条相关结果")
                
                for issue in issues:
                    review = {
                        '岗位': issue.get('jobTitle', issue.get('position', '')),
                        'user-name': issue.get('userName', issue.get('authorName', '匿名用户')),
                        'read-num': f'{issue.get("readCount", 0)}阅读' if issue.get('readCount') else '',
                        'content': issue.get('content', issue.get('title', '')),
                    }
                    if review['content']:
                        reviews.append(review)
            else:
                print(f"  [API错误] code={data.get('code')}")
        except Exception as e:
            print(f"  [错误] {e}")
            
        return reviews


# ==================== 数据保存 ====================

def save_to_excel(reviews, output_path='Comment.xlsx'):
    """保存评论数据到Excel文件"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "员工点评"
    
    # 表头样式
    header_font = Font(name='微软雅黑', size=11, bold=True, color='FFFFFF')
    header_fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
    header_alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    thin_border = Border(
        left=Side(style='thin'), right=Side(style='thin'),
        top=Side(style='thin'), bottom=Side(style='thin')
    )
    
    # 写入表头
    headers = ["岗位", "user-name", "read-num", "content"]
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_alignment
        cell.border = thin_border
    
    # 写入数据
    data_alignment = Alignment(vertical='top', wrap_text=True)
    for row_idx, review in enumerate(reviews, 2):
        for col_idx, header in enumerate(headers, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=review.get(header, ''))
            cell.alignment = data_alignment
            cell.border = thin_border
            cell.font = Font(name='微软雅黑', size=10)
    
    # 设置列宽
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 18
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 60
    
    # 冻结首行
    ws.freeze_panes = 'A2'
    
    wb.save(output_path)
    print(f"\n[保存成功] 共保存 {len(reviews)} 条点评数据到 {output_path}")


# ==================== 主流程 ====================

def main():
    """主执行函数"""
    print("=" * 60)
    print("BOSS直聘员工点评数据采集脚本")
    print("=" * 60)
    
    # 检查Cookie配置
    if YOUR_COOKIE == 'YOUR_COOKIE_HERE':
        print("\n[错误] 请先配置你的BOSS直聘Cookie！")
        print("1. 浏览器打开 https://www.zhipin.com 并登录")
        print("2. 按F12打开开发者工具 -> Network标签")
        print("3. 刷新页面，点击任意请求")
        print("4. 在Headers中找到Request Headers里的Cookie")
        print("5. 复制Cookie值并粘贴到脚本的YOUR_COOKIE变量中")
        return
        
    # 初始化爬虫
    spider = BossZhiPinSpider(YOUR_COOKIE)
    all_reviews = []
    
    # 遍历所有公司
    for category, companies in COMPANIES.items():
        print(f"\n{'='*40}")
        print(f"分类: {category}")
        print(f"{'='*40}")
        
        for company_name in companies:
            print(f"\n{'─'*30}")
            print(f"[开始采集] {company_name}")
            
            # 1. 搜索公司
            company_info = spider.search_company(company_name)
            if not company_info:
                print(f"  [跳过] 无法找到公司: {company_name}")
                continue
                
            # 2. 获取员工点评
            company_reviews = spider.get_company_reviews(
                company_info['id'], company_name
            )
            
            # 为每条评论添加公司标签
            for review in company_reviews:
                review['公司分类'] = category
                review['公司名称'] = company_info['name']
            
            all_reviews.extend(company_reviews)
            print(f"  [小计] {company_name}: {len(company_reviews)} 条")
            
            # 3. 关键词搜索补充
            keyword_reviews = spider.search_reviews_by_keyword(company_name, max_results=5)
            for review in keyword_reviews:
                review['公司分类'] = category
                review['公司名称'] = company_info['name']
            all_reviews.extend(keyword_reviews)
            print(f"  [补充] {company_name}: +{len(keyword_reviews)} 条")
            
            # 随机延迟避免被封
            delay = random.randint(*REQUEST_DELAY)
            print(f"  等待{delay}秒...")
            time.sleep(delay)
            
    # 去重
    seen = set()
    unique_reviews = []
    for review in all_reviews:
        content_hash = hash(review.get('content', '')[:50])
        if content_hash not in seen:
            seen.add(content_hash)
            unique_reviews.append(review)
            
    # 保存结果
    output_path = 'Comment.xlsx'
    save_to_excel(unique_reviews, output_path)
    
    print(f"\n{'='*60}")
    print(f"采集完成！")
    print(f"  总采集: {len(all_reviews)} 条")
    print(f"  去重后: {len(unique_reviews)} 条")
    print(f"  保存文件: {output_path}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()

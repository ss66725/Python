# -*- coding: utf-8 -*-
"""
📚 爬虫教学示例（你的第一个爬虫程序）
====================================
学习目标：
1. 用 requests 库向网站发送请求，获取网页内容
2. 用 BeautifulSoup 库解析 HTML，提取想要的数据
3. 把数据保存到文件

需要先安装的库（已经帮你装好了）：
    pip install requests beautifulsoup4
"""

import requests          # 用来发请求、获取网页
from bs4 import BeautifulSoup  # 用来解析网页结构

# 我们要访问的网址（example.com 是一个专门用于教学测试的网站，很稳定）
url = "https://example.com"

# ---------- 第 1 步：发送请求，获取网页 ----------
print("⏳ 正在访问:", url)
response = requests.get(url)

# status_code 是服务器返回的状态码：
#   200 = 成功  404 = 页面不存在  403 = 被禁止访问  503 = 服务器暂时不可用
print("✅ 状态码:", response.status_code)

# ⚠️ 重要：真实爬虫里，服务器不一定总返回 200！
# 所以要学会判断。如果请求失败，就不往下做了，避免程序崩溃。
if response.status_code != 200:
    print("❌ 请求失败！可能是网站暂时不可用，或被反爬了。")
    print("   提示：可以稍后重试，或检查网址是否正确。")
    raise SystemExit(1)

# 网页的全部内容（HTML 代码）存在 response.text 里
html = response.text
print("📄 网页内容长度:", len(html), "个字符")

# ---------- 第 2 步：解析 HTML ----------
# 把 HTML 文本交给 BeautifulSoup，它会把网页变成一棵可查询的"树"
soup = BeautifulSoup(html, "html.parser")

# ---------- 第 3 步：提取数据 ----------
# 1. 提取网页标题（<title> 标签里的文字）
title = soup.title.string
print("🏷️ 网页标题:", title)

# 2. 提取一级标题（<h1> 标签）
h1 = soup.find("h1")
print("📌 一级标题:", h1.get_text() if h1 else "没有找到")

# 3. 提取所有段落（<p> 标签）的文字
paragraphs = soup.find_all("p")
print("📝 共有", len(paragraphs), "个段落")
for i, p in enumerate(paragraphs):
    text = p.get_text()
    print(f"   第{i+1}段: {text[:50]}...")

# ---------- 第 4 步：保存数据到文件 ----------
with open("爬取结果.txt", "w", encoding="utf-8") as f:
    f.write(f"网页标题: {title}\n")
    f.write(f"一级标题: {h1.get_text() if h1 else '无'}\n")
    for i, p in enumerate(paragraphs):
        f.write(f"段落{i+1}: {p.get_text()}\n")

print("💾 结果已保存到『爬取结果.txt』")
print("🎉 恭喜！你完成了一个完整的爬虫程序！")

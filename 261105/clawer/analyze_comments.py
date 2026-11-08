#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BOSS直聘员工点评数据分析脚本
================================
使用方法：
1. 确保 Comment.xlsx 文件中已采集到数据
2. 运行脚本：python analyze_comments.py
3. 脚本将输出分析结果并生成分析报告

分析内容包括：
- 数据概览（总条数、各公司分布）
- 阅读量TOP评论
- 关键词频率分析
- 各公司点评情感倾向
"""

import pandas as pd
import numpy as np
from collections import Counter
import re
import os

# ==================== 数据加载 ====================

def load_data(file_path='Comment.xlsx'):
    """加载Excel数据"""
    if not os.path.exists(file_path):
        print(f"[错误] 文件 {file_path} 不存在，请先运行爬虫脚本采集数据")
        return None
        
    try:
        df = pd.read_excel(file_path)
        print(f"[加载成功] 共 {len(df)} 条点评数据")
        print(f"列名: {list(df.columns)}")
        return df
    except Exception as e:
        print(f"[错误] 读取文件失败: {e}")
        return None


# ==================== 数据概览 ====================

def overview(df):
    """数据概览"""
    print("\n" + "=" * 60)
    print("【数据概览】")
    print("=" * 60)
    
    print(f"\n总点评数: {len(df)} 条")
    print(f"\n各字段非空统计:")
    for col in df.columns:
        non_null = df[col].notna().sum()
        print(f"  {col}: {non_null}/{len(df)}")
    
    # 如果有公司分类列
    if '公司分类' in df.columns:
        print(f"\n按公司分类统计:")
        print(df['公司分类'].value_counts().to_string())
        
    if '公司名称' in df.columns:
        print(f"\n按公司统计:")
        print(df['公司名称'].value_counts().to_string())


# ==================== 阅读量分析 ====================

def analyze_reads(df):
    """阅读量分析"""
    print("\n" + "=" * 60)
    print("【阅读量分析】")
    print("=" * 60)
    
    # 提取阅读量数字
    def extract_read_num(val):
        if pd.isna(val):
            return 0
        match = re.search(r'(\d+)', str(val))
        return int(match.group(1)) if match else 0
        
    df['read_count'] = df['read-num'].apply(extract_read_num)
    
    # 按阅读量排序
    top_reads = df.nlargest(10, 'read_count')
    print("\n阅读量TOP10评论:")
    print("-" * 50)
    for idx, row in top_reads.iterrows():
        content = str(row.get('content', ''))[:50]
        print(f"  阅读{row['read_count']} | {row.get('user-name', '?')} | {content}...")
        
    # 阅读量统计
    print(f"\n阅读量统计:")
    print(f"  最高: {df['read_count'].max()}")
    print(f"  最低: {df['read_count'].min()}")
    print(f"  平均: {df['read_count'].mean():.1f}")
    print(f"  中位数: {df['read_count'].median():.1f}")


# ==================== 关键词分析 ====================

def keyword_analysis(df):
    """关键词频率分析"""
    print("\n" + "=" * 60)
    print("【关键词频率分析】")
    print("=" * 60)
    
    # 合并所有评论文本
    all_text = ' '.join(df['content'].dropna().astype(str))
    
    # 常用职场关键词
    keywords = [
        '加班', '薪资', '福利', '晋升', '管理', '氛围', '压力',
        '面试', '离职', '入职', '绩效', '年终奖', '股票', '期权',
        '房补', '餐补', '团建', '培训', '成长', '发展', '团队',
        '领导', '同事', '工作强度', '996', '大小周', '调休',
        '华为', '比亚迪', '加班多', '钱多', '事少', '累', '爽',
    ]
    
    print("\n高频词汇统计:")
    word_counts = {}
    for kw in keywords:
        count = all_text.count(kw)
        if count > 0:
            word_counts[kw] = count
            
    if word_counts:
        sorted_words = sorted(word_counts.items(), key=lambda x: -x[1])
        for word, count in sorted_words[:20]:
            print(f"  {word}: {count}次")
    else:
        print("  未检测到关键词（评论数据可能较简短）")
        
    # 评论长度统计
    df['content_len'] = df['content'].astype(str).str.len()
    print(f"\n评论内容长度统计:")
    print(f"  平均长度: {df['content_len'].mean():.1f} 字符")
    print(f"  最长: {df['content_len'].max()} 字符")
    print(f"  最短: {df['content_len'].min()} 字符")


# ==================== 情感倾向分析 ====================

def sentiment_analysis(df):
    """简易情感倾向分析"""
    print("\n" + "=" * 60)
    print("【情感倾向分析】")
    print("=" * 60)
    
    # 正面和负面关键词
    positive_words = ['好', '棒', '优秀', '满意', '不错', '推荐', '喜欢', '舒服', '福利好', '薪资高']
    negative_words = ['差', '坑', '垃圾', '累', '加班', '坑人', '别来', '离职', '劝退', '坑爹']
    
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    
    for content in df['content'].dropna():
        text = str(content)
        pos = sum(1 for w in positive_words if w in text)
        neg = sum(1 for w in negative_words if w in text)
        
        if pos > neg:
            positive_count += 1
        elif neg > pos:
            negative_count += 1
        else:
            neutral_count += 1
            
    total = len(df)
    print(f"\n情感分布:")
    print(f"  正面倾向: {positive_count}条 ({positive_count/total*100:.1f}%)")
    print(f"  负面倾向: {negative_count}条 ({negative_count/total*100:.1f}%)")
    print(f"  中性: {neutral_count}条 ({neutral_count/total*100:.1f}%)")


# ==================== 生成分析报告 ====================

def generate_report(df, output_path='分析报告.md'):
    """生成Markdown格式分析报告"""
    report = """# BOSS直聘员工点评数据分析报告

## 一、数据概览

"""
    report += f"- 总点评数: {len(df)} 条\n"
    
    if '公司名称' in df.columns:
        report += "\n## 二、各公司点评分布\n\n"
        report += df['公司名称'].value_counts().to_markdown() + "\n"
        
    if 'read-num' in df.columns:
        report += "\n## 三、阅读量TOP10\n\n"
        def extract_num(val):
            import re
            if pd.isna(val): return 0
            m = re.search(r'(\d+)', str(val))
            return int(m.group(1)) if m else 0
        df_copy = df.copy()
        df_copy['read_num'] = df_copy['read-num'].apply(extract_num)
        top10 = df_copy.nlargest(10, 'read_num')
        report += "| 排名 | 公司 | 用户名 | 阅读量 | 评论内容 |\n"
        report += "|------|------|--------|--------|----------|\n"
        for i, (_, row) in enumerate(top10.iterrows(), 1):
            content = str(row.get('content', ''))[:40]
            report += f"| {i} | {row.get('公司名称', '')} | {row.get('user-name', '')} | {row['read_num']} | {content} |\n"
            
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"\n[报告已生成] {output_path}")


# ==================== 主流程 ====================

def main():
    """主执行函数"""
    print("=" * 60)
    print("BOSS直聘员工点评数据分析工具")
    print("=" * 60)
    
    # 加载数据
    df = load_data('Comment.xlsx')
    if df is None:
        return
        
    # 执行各项分析
    overview(df)
    analyze_reads(df)
    keyword_analysis(df)
    sentiment_analysis(df)
    generate_report(df)
    
    print("\n" + "=" * 60)
    print("分析完成！")
    print("=" * 60)


if __name__ == '__main__':
    main()

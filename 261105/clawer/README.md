# BOSS直聘员工点评采集工具

## 文件说明

| 文件 | 说明 |
|------|------|
| Comment.xlsx | 采集数据存储文件（已创建表头） |
| boss_zhipin_spider.py | BOSS直聘员工点评爬虫脚本 |
| analyze_comments.py | 数据分析脚本 |
| README.md | 本使用说明 |

## 重要说明

**BOSS直聘具有严格的反爬虫机制**，服务器端IP已被封锁（返回错误码35："您的IP地址存在异常行为"），因此无法在服务器端直接采集数据。

请按照以下步骤在**本地电脑**上运行爬虫脚本：

## 使用步骤

### 第一步：获取BOSS直聘Cookie

1. 使用Chrome浏览器打开 https://www.zhipin.com 并登录你的账号
2. 按 `F12` 打开开发者工具
3. 切换到 **Network**（网络）标签页
4. 刷新页面（`Ctrl+R` 或 `Cmd+R`）
5. 在请求列表中找到任意一个请求（例如 `joblist.json` 或 `company.json`）
6. 点击该请求，在右侧 **Headers** 标签页中找到 **Request Headers**
7. 找到 `Cookie:` 那一行，复制后面的整个值
8. 将复制的Cookie值粘贴到 `boss_zhipin_spider.py` 脚本中的 `YOUR_COOKIE` 变量处（替换 `YOUR_COOKIE_HERE`）

### 第二步：安装依赖

```bash
pip install requests beautifulsoup4 openpyxl pandas
```

### 第三步：运行爬虫

```bash
python boss_zhipin_spider.py
```

脚本会自动：
1. 搜索你配置的目标公司
2. 尝试通过API获取员工点评数据
3. 同时通过关键词搜索补充数据
4. 自动去重
5. 保存结果到 `Comment.xlsx`

### 第四步：运行分析

```bash
python analyze_comments.py
```

脚本会输出：
- 数据概览
- 阅读量TOP10评论
- 关键词频率分析
- 情感倾向分析
- 生成 Markdown 格式分析报告

## 如果API被封锁的备选方案

如果BOSS直聘API仍然返回错误，你可以：

1. **使用浏览器自动化方案**：安装 Selenium + ChromeDriver，通过浏览器自动化方式采集（可以绕过部分反爬）
2. **手动复制**：在BOSS直聘APP或网页端手动查看员工点评，复制内容到Excel中
3. **使用第三方数据平台**：如看准网、脉脉等平台可能提供更开放的数据接口

## 采集的公司列表

| 分类 | 公司 |
|------|------|
| 深圳本地 | 华为、比亚迪、汇川技术、越疆科技、优必选、大疆创新 |
| 国产机器人龙头 | 埃斯顿、新松机器人、埃夫特、珞石机器人、李群自动化 |
| 智能装备/集成 | 明珞装备、华工科技、瑞松科技 |
| 外资四大家族 | 发那科、ABB、库卡、安川电机 |

## 采集字段说明

| 字段 | 说明 |
|------|------|
| 岗位 | 评论者的职位 + 工作年限 |
| user-name | 评论人的昵称 |
| read-num | 评论的阅读量（带"阅读"字样） |
| content | 评论的完整正文内容 |

## 注意事项

1. 请遵守BOSS直聘的 robots.txt 和使用条款
2. 控制请求频率，避免对服务器造成压力
3. Cookie会过期，过期后需要重新获取
4. 采集数据仅用于个人分析和学习目的

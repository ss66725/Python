from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ---------------------- 高频词数据 ----------------------
word_freq = [
    ('工作', 126), ('薪资', 98), ('发展', 87), ('环境', 72), ('压力', 68),
    ('管理', 61), ('成长', 56), ('福利', 52), ('培训', 49), ('团队', 45),
    ('氛围', 42), ('加班', 40), ('制度', 38), ('设备', 36), ('提升', 34),
    ('平台', 32), ('待遇', 31), ('同事', 29), ('机会', 28), ('稳定', 27),
    ('枯燥', 26), ('轻松', 25), ('领导', 24), ('技术', 23), ('资源', 22),
    ('后勤', 21), ('弹性', 20), ('保障', 20), ('高效', 19), ('安全', 19),
    ('复杂', 18), ('学习', 18), ('晋升', 17), ('沟通', 17), ('忙碌', 16),
    ('充实', 16), ('规划', 15), ('资源', 15), ('完善', 14), ('友好', 14),
    ('强度', 13), ('流程', 13), ('创新', 12), ('稳定', 12), ('舒心', 11),
    ('广阔', 11), ('协作', 10), ('劳累', 10), ('保障', 10), ('潜力', 9)
]
freq_dict = dict(word_freq)

# ---------------------- 词云配置 ----------------------
# Windows 字体：r"C:\Windows\Fonts\simhei.ttf"
# Mac 字体：r"/System/Library/Fonts/PingFang.ttc"
# 这里先用黑体，你根据自己系统修改 font_path
wc = WordCloud(
    font_path=r"C:\Windows\Fonts\simhei.ttf",
    background_color="white",
    width=1200,
    height=800,
    max_words=50,
    max_font_size=220,
    min_font_size=10,
    contour_width=1,
    contour_color="#4682B4",
    random_state=42,
    prefer_horizontal=0.7
)

wc.generate_from_frequencies(freq_dict)

# 保存图片
wc.to_file("top50_wordcloud.png")
print("✅ 词云图已保存：top50_wordcloud.png")

# 绘图展示
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(12, 8), dpi=100)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("员工评价高频名词、形容词词云", fontsize=16, pad=15)
plt.tight_layout()
plt.show()

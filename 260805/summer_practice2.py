def parse_int_list(prompt):
    text = input(prompt).strip()
    if not text:
        print("输入不能为空")
        raise SystemExit(1)
    try:
        return [int(x) for x in text.split()]
    except ValueError:
        print("输入无效，请输入以空格分隔的整数")
        raise SystemExit(1)

weekly_sales = parse_int_list('请输入一周的销售额，用空格分隔: ')
print('本周销售总额:', sum(weekly_sales))

import random
random_numbers = [random.randint(0, 10) for _ in range(7)]
print('随机生成的 7 个数字:', random_numbers)

rainfall = parse_int_list('请输入每个月降水量，用空格分隔: ')
print('降水量总和:', sum(rainfall))
print('最大降水量是', max(rainfall))
print('最小降水量是', min(rainfall))
print('平均降水量是', sum(rainfall) / len(rainfall))


def greater_than(values, threshold):
    return [value for value in values if value > threshold]

values = parse_int_list('请输入列表，用空格分隔: ')
try:
    threshold = int(input('请输入数字: ').strip())
except ValueError:
    print('输入无效，请输入一个整数')
    raise SystemExit(1)

result = greater_than(values, threshold)
print('最后的结果是', result)

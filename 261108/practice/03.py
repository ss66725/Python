name = input("请输入用户名：")
print(f"{name}，欢迎登录")

goods = {
    "面包": 2,
    "牛奶": 2.4,
    "可乐": 5,
    "咖啡": 35,
    "香蕉": 7.5,
    "苹果": 10,
    "芒果": 11.3
}

whole_price = 0
for name,price in goods.items():
    whole_price += price*100
print(f"补货的总价值为{whole_price}")

whole_price = 0
def assess_product(name,single_price,number):
    whole_price = single_price * number
    print(f"{name}的总价值:{whole_price}元")
    if number < 5:
        print("状态：库存告急，请补货！")
    elif number > 30:
        print("状态：库存积压，建议促销。")
    else:
        print("状态：库存健康。")

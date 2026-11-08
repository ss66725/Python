try:
    num = int(input("请输入一个整数: "))
except ValueError:
    print("输入无效，请输入一个整数")
    raise SystemExit(1)

if num <= 1:
    print('既不是质数，也不是合数')
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print('为质数')
    else:
        print('为合数')

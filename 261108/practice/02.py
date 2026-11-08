name = input('Please input your name!')
print(f"Hello {name}")
class Goods:
    all_goods = []

    def check_number(self):
            if self.number <= 500:
                print(f"You need to buy more {self.name}")

    @staticmethod
    def print_all():
        for g in Goods.all_goods: 
            print(f"name:{g.name}",f"whole_price{g.whole_price}")

    def __init__(self,name,number,single_price):
        self.name = name
        self.number = number
        self.single_price = single_price
        self.whole_price = number * single_price
        Goods.all_goods.append(self)
        
banana = Goods('banana',36,548)
orange = Goods('orange',599,654)
apple = Goods('apple',2121,15999)

for g in Goods.all_goods:
    g.check_number()
Goods.print_all()

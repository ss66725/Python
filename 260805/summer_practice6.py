string=input('string plz!!')
dict1={}
for chara in string:
    if chara in dict1:
        dict1[chara]+=1
    else:
        dict1[chara]=1
print('字典为:',dict1)
    
dict2={'tom':888,'jerry':999,'alice':777}
menu=input('找名字?加名字?删除名字?退出?')
while menu!='退出':
    if menu=='找名字':
        name=input('输入名字')
        if name in dict2:
            print('找到了,名字为{0},数值为{1}'.format(name,dict2[name]))
        else:
            print('木有啊')
    elif menu=='加名字':
        name=input('输入名字')
        if name in dict2:
            print('名字已存在,数值为{0}'.format(dict2[name]))
        else:
            value=input('输入数值')
            dict2[name]=value
            print('添加成功,名字为{0},数值为{1}'.format(name,dict2[name]))
    elif menu=='删除名字':
        name=input('输入名字')
        if name in dict2:
            del dict2[name]
            print('删除成功')
        else:
            print('木有!')
    else:
        print('你输错了!!')
    menu=input('找名字?加名字?删除名字?退出?')
print('退了!')

set1=set()    
string=input('随便输什么!')
for number in string:
    set1.add(number)
list1=list(set1)
print('唯一单词列表为:',list1)
set2=set()
set2.update(list1)
print('集合为:',set2)

string1=input('想写啥写啥!!')
string2=input('想写啥写啥!!')
a=set(string1)|set(string2)
b=set(string1)&set(string2)
c=set(string1)-set(string2)
d=set(string1)^set(string2)
print('两个一起:',a)
print('两个共有:',b)
print('前特有:',c)
print('前后特有:',d)

class Person:
    def __init__(self,name,adress,age,phone):
        self.name = name
        self.adress = adress
        self.age = age
        self.phone = phone
        
    def get_name(self):
        return self.name
    
    def get_adress(self):
        return self.adress
    
    def get_age(self):
        return self.age
    
    def get_phone(self):
        return self.phone
    
    def set_name(self,name):
        self.name = name
        
    def set_adress(self,adress):
        self.adress = adress
    
    def set_age(self,age):
        if age >= 0:
            self.age = age
        else:
            print('名字不能为负数!')
        
    def set_phone(self,phone):
        self.phone = phone
    
    def __str__(self):
        return f'姓名:{self.name}| 地址:{self.adress}| 年龄:{self.age}| 电话:{self.phone}'
    
def main():
    me = Person("李雷", "北京市海淀区中关村", 25, "138-0000-1111")
    friend = Person("韩梅梅", "上海市浦东新区陆家嘴", 24, "139-0000-2222")
    family = Person("李爸爸", "北京市朝阳区望京", 55, "137-0000-3333")
    
    print('我的个人信息为')
    print(me)
    print('\n 朋友的个人信息为')
    print(friend)
    print('\n 家人的个人信息为')
    print(family)

    
    


    
    
    
    
    
                                      
from inspect import AGEN_CLOSED, AGEN_CREATED
from types import new_class


class Pet:
    def __init__(self,name,animal_type,age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        
    def set_name(self,new_name):
        self.name = new_name
        
    def set_animal_type(self,new_type):
        self.animal_type = new_type
        
    def set_age(self,new_age):
        self.age = new_age
        
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.animal_type
    
    def get_age(self):
        return self.age
    
Pet_name = input('请输入宠物的名字!')
Pet_type = input('请输入宠物的类别!')
Pet_age = input('请输入宠物的年龄!')

my_pet=Pet(Pet_name,Pet_type,Pet_age)

print('名字',my_pet.get_name())
print('类别',my_pet.get_type())
print('年龄',my_pet.get_age())

class Car:
    def __init__(self,model,year,make):
        self.year = year
        self.model = model
        self.year = year
        self.make = make
        self.speed = 0
        
    def accelerate(self):
        self.speed += 5
        
    def brake(self):
        if self.speed > 0:
            self.speed -= 5
    
    def get_speed(self):
        return self.speed

my_car=Car('Model Y',2026,'Tesla')
print(my_car)

for i in range(5):
    my_car.accelerate()
    print('加速加速*',{i+1})
    
for i in range(5):
    my_car.brake()
    print('减速减速 *',{i+1})
    
class Employee:
    def __init__(self,emp_id,name,dept,job):
        
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.job = job
        
    def self_name(self,n):
        self.name = n
        
    def self_dept(self,d):
        self.dept = d
        
    def self_job(self,j):
        self.job = j
        
    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Department: {self.dept}, Job: {self.job}"

def main():
    employees = {}   

    while True:
        print('\n'+'='*30)
        print('1.查找员工')
        print('2.添加员工')
        print('3.修改员工')
        print('4.删除员工')
        print('5.所有员工')
        print('6.退出了了')
        print('='*30)
        
        choice=input('要干什么?')
        
        if choice == '1':
            emp_id=input('请输入员工')
            if emp_id in employees:
                print(employees[emp_id])
            else:
                print('没人!') 
        
        elif choice == '2':
            emp_id=input('请输入新员工ID')
            if emp_id in employees:
                print('不是,有人了')
                continue
            name = input('请输入新员工的姓名')
            dept = input('请输入新员工的部门')
            job = input('请输入新员工的职位')
            employees[emp_id] = Employee(emp_id,name,dept,job)
                        
        elif choice == '3':
            emp_id=input('请输入要修改的员工ID')
            if emp_id not in employees:
                print('找不到,人呢?')
                continue
            emp = employees[emp_id]
            new_name = input('新名字')
            if new_name :
                emp.self_name(new_name)
            new_dept = input('新部门')
            if new_dept :
                emp.self_dept(new_dept)
            new_job = input('新职位')
            if new_job :
                emp.self_job(new_job)
            print('修改成功!')
                
                        
        elif choice == '4':
            emp_id=input('请输入要删除的员工')
            if emp_id in employees:
                del employees[emp_id]
                print('删除了')
            else:
                print('没有人啊??!')
                        
        elif choice == '5':
            if not employees:
                print('你没有员工哈哈')
            else:
                for emp in employees.values():
                    print(emp)
            
        elif choice == '6':
            print(886)
            break
        
if __name__ == '__main__':
    main()
    
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
            print('年龄不能为负数!')
        
    def set_phone(self,phone):
        self.phone = phone
    
    def __str__(self):
        return f'姓名:{self.name}| 地址:{self.adress}| 年龄:{self.age}| 电话:{self.phone}'
    
def main1():
    me = Person("李雷", "北京市海淀区中关村", 25, "138-0000-1111")
    friend = Person("韩梅梅", "上海市浦东新区陆家嘴", 24, "139-0000-2222")
    family = Person("李爸爸", "北京市朝阳区望京", 55, "137-0000-3333")
    
    print('我的个人信息为')
    print(me)
    print('\n 朋友的个人信息为')
    print(friend)
    print('\n 家人的个人信息为')
    print(family)
    
    print('\n 改下我的名字')
    me.set_name("李雷雷")
    print(me.get_name())
    print('\n 改下我的地址')
    me.set_adress("北京市海淀区中关村软件园")
    print(me.get_adress())
    print('\n 改下我的年龄')
    me.set_age(26)
    print(me.get_age())
    print('\n 改下我的电话')
    me.set_phone("138-0000-0000")
    print(me.get_phone())
    
    print('年龄是负数吗?')
    me.set_age(-5)
    print('实际年龄还是',me.get_age())
    
if __name__ == '__main__':
    main1()
    
    
    
    
    
        
            
                            
        
                
            
            
        
        
    
        
        

    
    




    
    
        
        
        
     
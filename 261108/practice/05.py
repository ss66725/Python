szpu={'name':'深圳职业技术大学', 'address':'南山西丽',
      'department':          [{'name_dep':'本科教育学院','major':6,'teacher':30},
			                  {'name_dep':'人工智能学院','major':5,'teacher':144},
                              {'name_dep':'电信学院','major':8,'teacher':108},
                              {'name_dep':'机电学院','major':6,'teacher':132},
                              {'name_dep':'建环学院','major':7,'teacher':89},
                              {'name_dep':'汽车学院','major':5,'teacher':68}]  }
                            


def getInfo(szpu, find_college):
    department = szpu['department']
    for i in department:
        if i['name_dep'] == find_college:
            return f"{i['name_dep']} 共有 {i['major']} 个专业，教师 {i['teacher']} 人"
    return "无此学院"    
    
find_college = input("请输入要查询的学院：")
retInfo = getInfo(szpu, find_college)

print(retInfo)



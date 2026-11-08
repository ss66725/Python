name=input('请输入你的名字,分为人名,中间名,姓氏,用空格分割').split()
if len(name)<3:
    print('输入无效,请输入名,中间名,和姓氏')
else:
    first_name=name[0]
    middle_name=name[1]
    last_name=name[2]
    initials=first_name[0]+middle_name[0]+last_name[0]
    print('你的名字缩写为:'+initials)

list1=input('请输入一系列数字,用空格分隔开').split()
if not list1:
    print('你什么都没输入,请重试!')
else:
    try:
        list2=[int(i) for i in list1] 
        summary1=0
        for i in list2:
            summary1+=i
        print('你输入的数字和为:'+str(summary1))
    except ValueError:
        print('你输的是数字么?请重试!')
        
def extract_vowel(list):
    list_vowel=[]
    for char in list:
        if char.lower() in 'aeiou':
            list_vowel.append(char)
    return list_vowel

def extract_consonant(list):
    list_consonant=[]
    for char in list:
        if char.lower() not in 'aeiou':
            list_consonant.append(char)
    return list_consonant

numbers=input('请输入一个字符串')
vowel_list=extract_vowel(numbers)
consonants_list=extract_consonant(numbers)
print('元音字母为:'+str(vowel_list))
print('辅音字母为:'+str(consonants_list))
print('元音字母的个数为:'+str(len(vowel_list)))
print('辅音字母的个数为:'+str(len(consonants_list)))

English=input('请输入一个英文句子,用空格分割').upper().split()
Latin=[]
for word in English:
    if len(word)>1:
        Latin.append(word[1:]+word[0]+'AY')
    else:
        Latin.append(word+'AY')
print('转化为小猪拉丁语为:'+str(Latin))



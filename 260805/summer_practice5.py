string=input('string please!')
chara_dict={}
for chara in string:
    if chara in chara_dict:
        chara_dict[chara]+=1
    else:
        chara_dict[chara]=1
print('字典为:',chara_dict)
chara_list=[]    
for key,value in chara_dict.items():
    chara_list.append((key,value))
chara_list.sort(key=lambda x:x[1])
print('最少的元素为{0},数目为{1}'.format(chara_list[0][0], chara_list[0][1]))
print('最多的元素为{0},数目为{1}'.format(chara_list[-1][0], chara_list[-1][1]))

security_dict={'a':'z','c':'1','g':'%','z':'@'}
string=input('请输入要加密的字符!')
security_string=''
for chara in string:
    if chara in security_dict:
        security_string+=security_dict[chara]
    else:
        security_string+=chara
print('加密后的字符为:',security_string)
open_dict={value:key for key,value in security_dict.items()}
open_string=''
for chara in security_string:
    if chara in open_dict:
        open_string+=open_dict[chara]
    else:
        open_string+=chara
print('解密后的文件为:',open_string)
    

        
    

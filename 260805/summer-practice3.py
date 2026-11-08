print('hello world')
answer=input('输入你的选择题答案.用空格分离').split()
correct = [
    "A", "C", "A", "A", "D",
    "B", "C", "A", "C", "B",
    "A", "D", "C", "A", "D",
    "C", "B", "B", "D", "A"
]
correct_number=0
for i in range(20):
    if answer[i]==correct[i]:
        correct_number+=1
if correct_number>=15:
    print('恭喜你通过考试!总共答对' + str(correct_number) + '题')
else:
    print('很遗憾没有通过!总共答对' + str(correct_number) + '题')
    

    
    
        


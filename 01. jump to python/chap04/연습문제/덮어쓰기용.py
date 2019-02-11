a=open('./방명록.txt','r',encoding='UTF-8')
b=a.read()
print('임꺽정' in b)
a.close()
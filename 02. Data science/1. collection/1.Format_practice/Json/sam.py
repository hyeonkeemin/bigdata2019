b=[]
b.append({'가':{}})
b[0]['가']=[]
b.append({'나':[]})
b[1]['나']={}
b[1]['나']={'나는':'바보'}
b[1]['나'].update({'쟤는':'천재'})
print(b)

for i in b:
    print(i)
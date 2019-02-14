list = [1,3,2,5,-1,-2,-3]
num1, num2 = [], []
for i in list:
    if i < 0 :
        num1.append(i)
    elif i > 0 :
        num2.append(i)

print(num1+num2)

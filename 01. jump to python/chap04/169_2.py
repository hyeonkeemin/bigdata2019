f=open('sample.txt')
lines = f.readline()
f.close()

total=0
for line in lines:
    score = int(lines)
    total += score

average=total/len(lines)
f=open("result.txt", 'w')
f.write(str(average))
f.close()

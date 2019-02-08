f=open('sample.txt')
while True:
    lines = f.readline()
    if not lines: break
    print(lines, end='')
f.close()

total=0
for line in lines:
    score = int(lines)
    total += score
    print(score)
    print(total)

average=total/10
f=open("result.txt",'w')
f.close()

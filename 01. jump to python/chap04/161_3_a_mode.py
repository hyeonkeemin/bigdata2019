f=open('./file2.txt','a')
# f.write("hello daegu~") # 이전 파일의 마지막 위치에서 값을 추가. 줄단위로 입력하고 싶으면 메세지의 마지막에 \n 붙일것
# f.write('\nhello buSSSSan~')
my_message='''hello seoul!
hello jeju
hello incheon
'''
f.write(my_message)
f.close()
# f=open("d:\foo.txt",'w') # 절대경로. 경로 미지정시 현재 있는 디렉토리에 생성
                              # unix 계열에서는 실행이 안될수도 있당
# f=open("d:/새파일2.txt",'w') # 경로에 \나 /나 차이없다
# f=open("d:\mypath\foo.txt",'w')
# f=open("d:/mypath/새파일2.txt",'w')
# f=open("d:\mypath\new\foo.txt",'w') # 오류. 절대경로 지정할 땐 백슬러쉬로 쓸 경우 \n같은 특수문자열에 걸림 안댐
# f=open("d:\\mypath\\new\\foo.txt",'w') # 그래서 실수를 줄이기 위해 경로표시 시 모든 \를 \\로 바꿔준댱
# f=open("d:/mypath/new/새파일2.txt",'w') # /를 한번만 사용해도 됨. 하위 버전과 연동되는진 확인 필요

f.close()

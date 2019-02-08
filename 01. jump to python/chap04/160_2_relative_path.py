# f=open("d:\새파일.txt",'w') # 절대경로. 경로 미지정시 현재 있는 디렉토리에 생성
                              # unix 계열에서는 실행이 안될수도 있당

# f=open("./새파일3.txt",'w') # 현재 경로에 파일 생성
                            # windows, unix 모든 운영체제에서 통용된당
# f=open("../새파일4.txt",'w')
# f=open("../../../mypath/new/새파일3.txt",'w')
# 위 코드만 비교하면 f=open('d:/mypath/new/newfile.txt')가 간결하지만 d드라이브가 없는 컴퓨터엔 오류가 뜰 것

# 연습
# f=open("../path_exer/새파일.txt",'w')
# f=open("../path_exer/new1/새파일.txt",'w')
# f=open("../path_exer/renew1/새파일.txt",'w')
# 상대경로는 소스코드를 기준으로 예측가능한 경로를 활용해야 한다.
f=open("../Path_exer/renew1/새파일2.txt",'w') # 대소문자 구분 안함. windows 운영체제에서만 가능한 결과.
# 그러나 호환성을 위해 windows에서도 대소문자를 가리는 것이 좋다.
f.close()

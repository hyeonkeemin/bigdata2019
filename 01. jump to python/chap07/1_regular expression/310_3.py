import re
p = re.compile('\w+\spython$', re.MULTILINE) # python$ : python 으로 끝나는 문자열 매치
                                              # re.MULTILINE : ^, $ 메타문자를 문자열의 각 라인마다 적용
dest_str='''python one python debug
life is too short
python two
you need python
python three
i will study python'''

m = p.findall(dest_str)
print(m)
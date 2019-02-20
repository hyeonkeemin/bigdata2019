from xml.etree.ElementTree import parse
tree = parse('note.xml')
note = tree.getroot() # 최상위 노드를 가져옴

print(note.get('date'))
print(note.get('foo'))
print(note.get('foo', '읎다')) # 찾는게 없으면 두번째 값 출력
print(note.keys()) # keys는 애트리뷰트의 키 값을 리스트로 리턴
print(note.items()) # items는 key, value 쌍을 리턴함(딕셔너리와 거의 비슷)

# xml 태그 접근하기
from_tag = note.find('from') # 태그 하위에 from과 일치하는 첫 번째 태그를 찾아서 리턴, 없으면 none
print(from_tag.text) # 뒤에 .text를 붙이면 해당 값을 바로 가져올 수 있다구
from_tags = note.findall('from') # 태그 하위에 from과 일치하는 모든 태그를 리스트로 리턴
from_text = note.findtext('from') # 태그 하위에 from과 일치하는 첫 번째 태그의 텍스트 값 리턴

# 특정 태그의 모든 하위 엘리먼트를 순차적으로 처리하기
# childs = note.getiterator()
# childs = note.getchildren()

note.getiterator('from') # 첫 번째 인수로 다음과 태그명을 받을 수도 있다
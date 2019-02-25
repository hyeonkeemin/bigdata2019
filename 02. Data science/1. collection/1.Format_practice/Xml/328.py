from problem.etree.ElementTree import Element,dump, SubElement

note = Element('note')
to = Element('to') # 자식노드
to.text = 'Tove' # 현재 엘리먼트(tag)에 값 추가
note.append(to) # 부모노드에 자식노드 추가

# SubElement(note,'from').text = 'jani' # SubElement를 활용하여 자식 노드 추가

from_tag = Element('from')
from_tag.text = 'jani'
note.append(from_tag) # SunElement를 쓰나 이거 세줄 쓰나 결과는 똑같

dump(note)
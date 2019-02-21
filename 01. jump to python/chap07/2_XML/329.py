from xml.etree.ElementTree import Element,dump, SubElement

note = Element('note')
to = Element('to') # 자식노드
to.text = 'Tove' # 현재 엘리먼트(tag)에 값 추가

note.append(to) # 부모노드에 자식노드 추가

SubElement(note,'from').text = 'jani' # SubElement를 활용하여 자식 노드 추가
dump(note)

dummy = Element('dummy')
note.insert(1,dummy) # 더미노드에 값이 없을경우 요렇게 처리도 가능. 태그에 값이 없을 경우 < /> 형태로 나옴
dump(note)

note.remove(dummy)  # 부모노드를 기준으로 찾아 들어감
dump(note)
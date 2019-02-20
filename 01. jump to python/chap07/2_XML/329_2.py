from problem.etree.ElementTree import Element,dump, SubElement

note = Element('note', date='20120104', to='tove') # 직접 date와 to의 속성정의
# to = Element('to') # 자식노드
# to.text = 'Tove' # 현재 엘리먼트(tag)에 값 추가
# note.append(to) # 부모노드에 자식노드 추가

SubElement(note,'from').text = 'jani' # SubElement를 활용하여 자식 노드 추가
SubElement(note, 'heading').text = 'reminder'
SubElement(note, 'body').text = "don't forget me this weekend"
dump(note)

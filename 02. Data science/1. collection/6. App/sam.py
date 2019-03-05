# ex2_xml.py

import xml.etree.ElementTree as ET

input = '''
<world>
    <nations>
        <nation x = '1'>
            <id>001</id>
            <name>Korea</name>
            <capital>Seoul</capital>
        </nation>
        <nation x = '2'>
            <id>002</id>
            <name>Taiwan</name>
            <capital>Taipei</capital>
        </nation>
    </nations>
</world>'''

stuff = ET.fromstring(input)  # XML을 읽을 수 있게 트리형태로 변환
lst = stuff.findall('nations/nation')  # XML트리에서 nations/nation안의 subtrees를 불러온다
print('The number of nations:', len(lst))  # nation이 몇 개인지 출력

# nation 노드를 하나하나 돌리면서 name, id, capital을 출력하고 nation노드에서 속성 x를 출력
# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Capital city', item.find('capital').text)
#     print('Attribute', item.get("x"))


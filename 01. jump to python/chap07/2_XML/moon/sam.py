from xml.etree.ElementTree import parse
tree = parse('students_info.xml')
root = tree.getroot()

a = []
man=0;woman=0
major_major=0
age_20=0;age_30=0;age_40=0
lang_name_python=0;lang_experience=0;lang_level_high=0

for i in root.findall('student'):
    name = i.get('name')
    sex = i.get('sex')
    age = i.findtext('age')
    major = i.findtext('major')
    lang=[]
    profile = list((name,sex,age,major,lang))
    a.append(profile)
    for x in i.iter('practicable_computer_languages'):
        for y in x:
            lang_name = y.get('name')
            lang_level = y.get('level')
            for z in y:
                lang_period = z.get('value')
                lang.append(list((lang_name,lang_level,lang_period)))
print(a)


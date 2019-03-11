import pandas
import sqlite3
from xml.etree.ElementTree import SubElement, parse

input_file = 'Student_Info_DB_Scheme.xlsx'
output_file = 'Sudent_info_DB_Scheme_result.xls'

tree = parse('students_info_ver2.xml')
root = tree.getroot()

xml_data = []

for info in root.iter('student'):
    data_list = []
    data_list.append(info.get('ID'))
    data_list.append(info.get('name'))
    data_list.append(info.get('sex'))
    data_list.append(info.findtext('age'))
    data_list.append(info.findtext('major'))

    for info_2 in root.iter('language'):


print(xml_data)

data_frame = pandas.read_excel(input_file)




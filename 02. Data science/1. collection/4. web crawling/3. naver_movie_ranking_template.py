import urllib.request
from bs4 import BeautifulSoup
import re
import csv

html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')

tag_str = str(soup)
name_type = re.compile('title=["](?P<name>.+)["][>](?P=name)')
up_down_type = re.compile('alt=["]([a-z]+)["]')
change_type = re.compile('"range ac"[>](\w+)[<]/td')
name = name_type.findall(tag_str)
up_down = up_down_type.findall(tag_str)
up_down.pop(0)
change = change_type.findall(tag_str)
change.pop(0)

# print(name)
# print(up_down)
# print(change)


# NAME=[];UP_DOWN=[];CHANGE=[]
# TYPE = re.compile('title=["]((?P<name>.+))["][>](?P=name)\s+alt=["]([a-z]+)\s+range ac"[>](\w+)[<]/td')
# b = TYPE.findall(tag_str)
# if TYPE.groups(1):
#     NAME.append(TYPE.groups(1))
# elif TYPE.groups(2):
#     NAME.append(TYPE.groups(2))
# elif TYPE.groups(3):
#     CHANGE.append(TYPE.groups(3))
#
# print(NAME)
# print(UP_DOWN)
# print(CHANGE)

# print(name)









'''
# print(soup)
# print(soup.prettify())


# tag = soup.findAll('div', attrs={'class': 'tit3'})
# up_down = soup.find('img', attrs={'src ': 'http://imgmovie.naver.net/2007/img/common/icon_na_1.gif'})

tag2 = tag_normal.findAll('a')
tag2_str = []
name = []
name_type = re.compile('title=["](.+)["]')

for a in tag2:
    tag2_str.append(str(a))
for naming in tag2_str:
    name.append(name_type.search(naming).group(1))


tag3 = tag_normal.findAll('td', attrs={'class':'ac'})
tag3_str=[]
rank_type = re.compile('alt=["]([0-9][0-9]?[0-9])["]')
rank = []
tag5_str= []

for b in tag3:
    tag3_str.append(str(b))
for ranking in tag3_str:
    try:
        rank.append(rank_type.search(ranking).group(1))
    except:
        tag5_str.append(ranking)

tag4 = tag_normal.findAll('td', attrs={'class':'range ac'})
tag4_str=[]
change=[]
change_type = re.compile('[>](\w*)[<]')
for c in tag4:
    tag4_str.append(str(c))
for changing in tag4_str:
    change.append(change_type.search(changing).group(1))

up_down = []
up_down_type = re.compile('alt=["](\w+)["]')
trash=0
for up_down_ing in tag5_str:
    try:
        up_down.append(up_down_type.search(up_down_ing).group(1))
    except:
       trash+=1
change_final = []
for i in range(len(up_down)):
    if up_down[i] == 'na':
        change_final.append(change[i])
    elif up_down[i] == 'up':
        change_final.append('+'+change[i])
    elif up_down[i] == 'down':
        change_final.append('-'+change[i])

f = open('movie_info.csv','w',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['순위', '이름', '변동'])
for i in range(len(change_final)):
    csv_writer.writerow([i+1,name[i],change_final[i]])
f.close()
'''
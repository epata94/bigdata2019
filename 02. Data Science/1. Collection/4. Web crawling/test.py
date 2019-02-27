from bs4 import BeautifulSoup
from pandas import DataFrame
import urllib.request

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
# print(soup)
# print(soup.prettify())

result =[]
name_list = []
range_list = []
up_down_list = []

tags =  soup.findAll('div', attrs={'class':'tit3'})
for tag in tags:
    name_list.append(tag.a.string)

up_down_info = soup.findAll('img', attrs={'class':'arrow'})
for up_down in up_down_info:
    up_down_list.append(up_down.attrs['alt'])

range_info = soup.findAll('td', attrs={'class':'range ac'})
for ranges in range_info:
    range_list.append(ranges.string)


for i in range(0,49):
    result.append({
        'rank': str(i+1),
        'name': name_list[i],
        'range': range_list[i],
        'up_down': up_down_list[i]
    }
    )

rank_table = DataFrame(result, columns=('rank','name','range', 'up_down'))
rank_table.to_csv("naver_rank.csv", encoding="utf-8", mode= 'w', index=False)
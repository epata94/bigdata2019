import urllib.request
from pandas import DataFrame
import xml.etree.ElementTree as ET
import datetime
import os

now_date=datetime.datetime.now()
date=now_date.strftime('%Y%m%d_%H%M%S')

dir_name='V3_Bigdata'
dir_delimeter='\\'
file_dir='nene'
file_name=str(date)
file_limit=3
csv='.csv'

def make_dir(index):
    os.mkdir(dir_name+dir_delimeter+file_dir+str(index))

def make_file(index):
    result = []
    response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

    xml = response.read().decode('UTF-8')
    root = ET.fromstring(xml)

    for element in root.findall('item'):
        store_name = element.findtext('aname1')
        store_sido = element.findtext('aname2')
        store_gungu = element.findtext('aname3')
        store_address = element.findtext('aname5')
        result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

    nene_table = DataFrame(result,columns=('store','sido','gungu','store_address'))

    path=dir_name+dir_delimeter+file_dir+str(index)+dir_delimeter+file_name+csv
    nene_table.to_csv(path, encoding="utf8",mode='w',index=True)

def file_count():
    index=len(os.listdir(dir_name))
    if len(os.listdir(dir_name+dir_delimeter+file_dir+str(index)))==3:
        index+=1
        make_dir(index)
    return index

print("Start")
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
if not os.path.exists(dir_name+dir_delimeter+file_dir+'1'):
    make_dir(1)
    make_file(1)

make_file(file_count())
print("End")
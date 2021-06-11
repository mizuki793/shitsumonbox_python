#api/question.py
#userの番号を取得する
#from bs4 import BeautifulSoup
from flask 
import request
import json 
import urllib
import sys
import codecs


def get(name,num):
    #u_name = name.decode('utf-8')
    u_name = name
    num = int(num)

    f = open(u_name + '_'+ str(num)+'.json','w',encoding='UTF-8')
    f.write('{"items":[')
    cnt =0

    if num %3==0:
        cnt = num // 3
    else:
        cnt = num //3 + 1
    
    item = 0
    for i in range(cnt):
#        print('page=' + str(i+1))
        readObj = requests.get('https://peing.net/api/v2/items/?type=answered&account='+ u_name + '&page=' + str(i+1))        
        data = readObj.json()
        data = str(data['items'])
        
        if data=='[]':
            break
        if i !=0:
            data = ',' + data 
        item = item + data.count('answer_body')
        data = data.replace('[','').replace(']','').replace("'",'"')
        data = data.replace('None','0').replace('True','1').replace('False','0')
        data = data.replace(',',',\n')
        f.write(data)

    
    f.write('],')
    f.write('"item_num":'+ str(item) + '}')
    f.close()
    return "ファイルを作成しました"

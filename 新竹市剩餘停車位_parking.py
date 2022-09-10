# -*- coding: UTF-8 -*-
__author__ = "DDENG"
#0421======美化網頁、解決雙引問題 -> 用加號不要用逗號
#0421======將停車場名稱變標題

import numpy as np
import json
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x

import ssl
from urllib.parse import urlparse,unquote
context = ssl._create_unverified_context()


a=""
if len(sys.argv)>1:
    a=sys.argv[1]

url="https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=CEA6A12132133278&u=77DFE16E459DFCE30371C36CCE30AFF2620C9FA93F99248767110C1E4071F137831A929FA3EEAC4CEF65FED104ED70277A428AF9E2DD97F775312AF02CEFBF568EE5B5014AEB8CB8FFE734E9E5C3463762153B60165E0C0A1EA4A98178AE77696764CE2385107EED"
req=httplib.Request(url)
try:
    reponse = httplib.urlopen(req, context=context)



    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents = reponse.read()   #解決亂碼
        else:
            contents = reponse.read()
        data = json.loads(contents)
        #print(data)

        # 抓汽車剩餘位資料
        if a=='car':
            print('<body style="background-color:#aaaaaa">')  # 網頁背景(灰)
            j=1
            for i in data:
                carnum=int(i["汽車剩餘車位"])
                if carnum> 0:
                    car="編號:"+str(j)+"<br>"+"停車場名稱:"+i["停車場名稱"]+"<br>"+"地址:"+i["地址"]+"<br>"+"平日收費方式:"+i["平日收費方式"]+"<br>"+"假日收費方式:"+i["假日收費方式"]+"<br>"+"汽車總車位:"+i["汽車總車位"]+"<br>"+"汽車剩餘車位:"+i["汽車剩餘車位"]+"<br>"
                    print(car, "<br>")  # html
                    print("<hr>")  # 加線作區隔
                    j+=1
        # 抓機車剩餘位資料
        if a=='scooter':
            print('<body style="background-color:#aaaaaa">')  # 網頁背景(灰)
            j=1
            for i in data:
                sconum=int(i["機車剩餘車位"])
                if sconum> 0:
                    scooter="編號"+str(j)+"<br>"+"停車場名稱:"+i["停車場名稱"]+"<br>"+"地址:"+i["地址"]+"<br>"+"平日收費方式:"+i["平日收費方式"]+"<br>"+"假日收費方式:"+i["假日收費方式"]+"<br>"+"機車總車位:"+i["機車總車位"]+"<br>"+"機車剩餘車位:"+i["機車剩餘車位"]+"<br>"
                    print(scooter, "<br>")
                    print("<hr>")  # 加線作區隔
                    j+=1


except:                                                                 #  處理網路連線異常
    print("error")



"""

停車場名稱、地址、營運時間、平日收費方式、假日收費方式、汽車總車位、
汽車剩餘車位、機車總車位、機車剩餘車位、X座標、Y座標
"""

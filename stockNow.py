import scrollphathd as sphd
from scrollphathd.fonts import font5x7
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup

temp = 70

def showMeKospiSise():
    soup_sise = requests.get("http://finance.naver.com/sise/")
    soup_sise_BF = BeautifulSoup(soup_sise.text, "html.parser")
    temp = soup_sise_BF.find_all('ul')[6]
    temp1 = temp.find_all('span')[1].text
    temp2 = temp.find_all('span')[2].text
    temp2 = temp2.replace("상승"," ▲")
    temp2 = temp2.replace("\n","")
    return(temp1, temp2)

def showMeKosdaqSise():
    soup_sise = requests.get("http://finance.naver.com/sise/")
    soup_sise_BF = BeautifulSoup(soup_sise.text, "html.parser")
    temp = soup_sise_BF.find_all('ul')[6]
    temp1 = temp.find_all('span')[6].text
    temp2 = temp.find_all('span')[2].text
    temp2 = temp2.replace("상승"," ▲")
    temp2 = temp2.replace("\n","")
    return(temp1, temp2)

sphd.set_brightness(0.5)
sphd.rotate(degrees= 180)
stockString = ""
sphd.write_string(stockString, font=font5x7)

while True:
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.1)

    KOSPI = '0'
    kosdaq = '0'
    temp_time = datetime.now()
    
    if (temp != datetime.now().minute):
        print("다운받기 시작!")
        temp_KOSPI = showMeKospiSise()
        temp_kosdaq = showMeKosdaqSise()
        KOSPI = temp_KOSPI[0]
        kosdaq = temp_KOSPI[0]
        #print("%s, %s:%s Now"%(temp_time.day,temp_time.hour, temp_time.minute))
        temp_time_string = ("%s.%s %s:%s Now "%(temp_time.month,temp_time.day,temp_time.hour, temp_time.minute))
        #print(temp_time_string)
        
        if ((KOSPI != temp_KOSPI) or (kosdaq != temp_kosdaq)):
            KOSPI = temp_KOSPI
            kosdaq = temp_kosdaq
            #print("KOSPI: %s(%s) KOSDAQ: %s(%s)" %(temp_KOSPI[0],temp_KOSPI[1], temp_kosdaq[0],temp_kosdaq[1]))
            temp_stock_string =("KOSPI: %s( %s) KOSDAQ: %s( %s)" %(temp_KOSPI[0],temp_KOSPI[1], temp_kosdaq[0],temp_kosdaq[1]))
            #print(temp_stock_string)
            #print(temp_time_string,temp_stock_string)
            stockString = temp_time_string + temp_stock_string

        sphd.clear()
        sphd.write_string(stockString, font=font5x7)
 
    temp = temp_time.minute

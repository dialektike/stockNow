from datetime import datetime
import requests
from bs4 import BeautifulSoup

temp = 70

while True:
    KOSPI = '0'
    kosdaq = '0'
    
    if (temp != datetime.now().minute):
        print("다운받기 시작!")
        soup_sise = requests.get("http://finance.naver.com/sise/")
        soup_sise_BF = BeautifulSoup(soup_sise.text, "html.parser")
        temp = soup_sise_BF.find_all('ul')[6]
        temp_KOSPI = temp.find_all('span')[1].text
        temp_kosdaq = temp.find_all('span')[6].text
        
        temp = datetime.now().minute
    
    print(temp)
    
    if ((KOSPI != temp_KOSPI) or (kosdaq != temp_kosdaq)):
        KOSPI = temp_KOSPI
        kosdaq = temp_kosdaq
    
    print("KOSPI: %s, KOSDAQ: %s NOW" %(KOSPI, kosdaq))
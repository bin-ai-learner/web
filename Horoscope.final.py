import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import datetime

def main():
    k = {'雙魚' : 11,
     '水瓶': 10 ,
     '魔羯': 9 ,
     '射手': 8 ,
     '天蠍':7,
     '天秤':6,
     '天平':6,
     '處女':5,
     '獅子':4,
     '巨蟹':3,
     '雙子':2,
     '金牛':1,
     '牡羊':0,
     '白羊':0,
    }

    m ={
        '-1':datetime.date.today()-datetime.timedelta(days=1),
        '0':datetime.date.today(),
        '1':datetime.date.today()+ datetime.timedelta(days=1),
        '2':datetime.date.today()+ datetime.timedelta(days=2),
        '3':datetime.date.today()+ datetime.timedelta(days=3),
        '4':datetime.date.today()+ datetime.timedelta(days=4),
        '5':datetime.date.today()+ datetime.timedelta(days=5)
        }

    while True:
        j = input("星座(兩個字): ")
        l = input("想要的日期(-1=昨天，0=今天，類推至多為5):")   
        if len(j) > 2:
            print("請輸入兩個字")
        elif j not in k :
            print("不是星座或錯別字，請重新輸入")
        else:
            break
        
         
        if not isinstance(l, int):
            print("日期必須是數字")
        else:
            break


    if j in k:
        headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
        if l in m:
            url = f"https://astro.click108.com.tw/daily_11.php?iAstro={k[j]}&iType=0&iAcDay={m[l]}"
            # print(url)
            respone = requests.get(url,headers= headers)
    if respone.status_code==200:
        with open('output.html','w', encoding="UTF-8") as f:
            f.write(respone.text)
        value = m[l]
        print(f"\n爬蟲結果成功以下為{value}運勢",end="")
        # print(respone.text)
    else:
        print("沒拿到")

   
    soup = BeautifulSoup(respone.text,"html.parser")
    today_lucky = soup.find_all("div",class_="LUCKY")
    artical = soup.find_all("div",class_="TODAY_CONTENT")
   
    print(f"\n\n幸運數字：{today_lucky[0].h4.text}",end='　　')
    print(f"幸運顏色：{today_lucky[1].h4.text}",end='　　')
    print(f"開運方位：{today_lucky[2].h4.text}",)
    print(f"今日吉時：{today_lucky[3].h4.text}",  end='　　')   
    print(f"幸運星座：{today_lucky[4].h4.text}",)
    for div in artical:
        print(div.text)
   

if __name__ == "__main__":
    main()

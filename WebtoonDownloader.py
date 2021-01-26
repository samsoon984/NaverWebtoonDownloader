import requests
import os
import sys
import time
import random
from bs4 import BeautifulSoup



headers={

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'

}


def goDownload():
    Title_Id = str(input("Title_Id: "))
    name = str(input("Name: "))
    startNum = int(input("Start Number: "))
    lastNum = int(input("End Number: "))
    if Title_Id == "":
        print("Plz input Title_Id!")
        time.sleep(2)
        sys.exit(0)
    else:
        
        try:
            if not(os.path.isdir(name)):
                os.makedirs(os.path.join(name))
                print("making directory..")
        except:
            print("already exist..")
    getNum = startNum
    while getNum <= lastNum:
        try:
            if not(os.path.isdir(f"./{name}/{getNum}")):
                os.makedirs(os.path.join(f"./{name}/{getNum}"))
                print("making directory..")
        except:
            print("already exist..")
        print(f"Number: {getNum}")
        url = f"https://comic.naver.com/webtoon/detail.nhn?titleId={Title_Id}&no={getNum}"
        res = requests.get(url=url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        li_list = []
        data1_list=soup.findAll('div',{'class':'wt_viewer'})
        for data1 in data1_list:
            li_list.extend(data1.findAll('img'))
        i = 1
        for li in li_list:
            img_src = str(li['src'])
            with open(f"./{name}/{getNum}/{i}.jpg", "wb") as f:
                data = requests.get(url=img_src, headers=headers).content
                f.write(data)
            i += 1
            time.sleep(random.uniform(0,1))
        getNum += 1





goDownload()
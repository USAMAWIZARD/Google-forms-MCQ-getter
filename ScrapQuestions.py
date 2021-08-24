from bs4 import BeautifulSoup
import sys
import requests


def getpage(url):
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, "html.parser")

    alloptionsoup = soup.findAll('script', attrs={'type': 'text/javascript'})
    optiontoparse = [i.string for i in alloptionsoup]
    for data in optiontoparse:
        if data.startswith("var"):
            data = data.replace('var FB_PUBLIC_LOAD_DATA_ = ', '')
            data = data.replace(';', '')
            data = data.replace('null,', '')
            temp = eval(data)
            print(temp)


getpage(sys.argv[1])

from bs4 import BeautifulSoup
import sys
import requests
import json
import re

from requests.api import options
QuesitonAndOptions = {}  # {"question":{"option1","option2","option3","optin4}}

url = "https://docs.google.com/forms/d/e/1FAIpQLSfZhFkXX_hyoChxAsGrcIQ_Too7aRkzRUeqZsnw2a6LeufWzg/viewform?edit2=2_ABaOnucjWH4peJPBmW72i9JOPiWGUYJPYvmC1LGgyFfN7J2apRy3htlWGfv0XCJbMQ"
page = requests.get(url)
content = page.content
soup = BeautifulSoup(content, "html.parser")

alloptionsoup = soup.findAll('script', attrs={'type': 'text/javascript'})
optiontoparse = [i.string for i in alloptionsoup]
for data in optiontoparse:
    if data.startswith('var'):
        print(data)

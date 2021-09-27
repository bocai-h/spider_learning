import pdb
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.baidu.com")
bsObj = BeautifulSoup(html.read())
# pdb.set_trace()
print(bsObj.script)

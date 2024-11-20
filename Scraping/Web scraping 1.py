import pandas as pd
from bs4 import BeautifulSoup
import requests
url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
result=requests.get(url)
soup=BeautifulSoup(result.text,"lxml")
table=soup.find_all("table")[1]
titles=soup.find_all("th")
alltitles= [title.text.strip() for title in titles]
#rows=soup.find_all("tr")
#for row in rows:
#   datainsideofrow=row.find_all("td")
#   individualrowdata=[data.text.strip() for data in datainsideofrow]
#print(datainsideofrow)
extract1=table.find_all("tr")
for extractone in extract1:
    extract2=extractone.find_all("td")
    individualrowtable=[extracttwo.text.strip() for extracttwo in extract2]
    allrows=[]
    if individualrowtable:
        allrows.append(individualrowtable)
    for x in allrows:
        x=pd.DataFrame(x)
        print(x)


import pandas as pd
from bs4 import BeautifulSoup
import requests
url="https://www.scrapethissite.com/pages/simple/"
result=requests.get(url)
soup=BeautifulSoup(result.text,"lxml")
contents=soup.find_all("div")
countries_names=soup.find_all("h3",class_="country-name")
countries_capital=soup.find_all("span",class_="country-capital")
countries_population=soup.find_all("span",class_="country-population")
countries_area=soup.find_all("span",class_="country-area")
emptylist=[]
for name,capital,population,size in zip(countries_names,countries_capital,countries_population,countries_area):
    name=name.get_text(strip=True)
    capital=capital.get_text(strip=True)
    population=population.get_text(strip=True)
    size=size.get_text(strip=True)
    emptylist.append([name, capital,population,size])
df =pd.DataFrame(emptylist)
print(df)
df.to_csv(r"F:\scraping\countries_scraped_.csv")



import requests
from bs4 import BeautifulSoup

def get_city_photo(city_name):
    url = "https://www.google.com/search?sca_esv=04aa412ff406bf20&sca_upv=1&q={}&udm=2".format(city_name)
    r = requests.get(url)
    txt = r.text

    soup = BeautifulSoup(r.content,'html.parser')

    elements = soup.find_all('img')

    return elements[10]['src']
    
    

print (get_city_photo('chicago'))


    


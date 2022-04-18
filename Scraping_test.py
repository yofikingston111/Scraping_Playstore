import os

import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/apps/details?id=com.arkanamajusejahtera.irace'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}

def get_all_items():
    url = 'https://play.google.com/store/apps/details?id=com.arkanamajusejahtera.irace'

    params = {
        'id':'com.arkanamajusejahtera.irace'
    }
    appslist = []
    r = requests.get(url, params=params, headers=headers)

    #check status code
    # temp file
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    f = open('temp/pages.html', 'w+', encoding="utf-8")
    f.write(r.text)
    f.close()

    soup = BeautifulSoup(r.text, 'html.parser')

    results =soup.find('div', attrs={'class': 'ZfcPIb'})

    contents = results.find('div', attrs={'class': 'JNury Ekdcne'}).find_all('main', attrs={'class':'LXrl4c'})


    #scraping proccess
    for content in contents:
        try:
            review = content.find('div', attrs={'class': 'UD7Dzf'}).find('jscontroller', attrs={'jscontroller':'LVJlx'})
        except:
            review = content.find_all('span', attrs={'jsname':'bN97Pc'})

        total_user = content.find('span', attrs={'class':'EymY4b'}).text
        try:
            rating = content.find('div', attrs={'class': 'K9wGie'}).find('div', attrs={'aria-label':'Rated 4.7 stars out of five stars'}).text
        except:
            rating = content.find('div', attrs={'class': 'Rated 4.7 stars out of five stars'}).text


        data_dict = {
            'review': review,
            'Total User': total_user,
            'rating': rating
        }
        appslist.append(data_dict)

    #data append
    print(data_dict)
    return appslist

if __name__ == '__main__':
    get_all_items()




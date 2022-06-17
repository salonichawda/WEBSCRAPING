import requests
import json
from bs4 import BeautifulSoup
import pprint

def scrap_top_list():

    url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies"

    page=requests.get(url)

    soup=BeautifulSoup(page.text,'html.parser')

    main_div=soup.find("div",class_="panel-body content_body allow-overflow bestof_container")
    # print(main_div)
    year=soup.find("ul", class_="dropdown-menu").get_text().replace(" ","").split()
    # print(year)
    tbody=soup.find('table',class_='table')
    
    trs= tbody.find_all('tr')
    # print(trs)
    # return trs

    top_movie_list=[]

    for tr in trs[1:]:
        # print(tr)

        position1=tr.find('td',class_='bold').get_text().strip()
        # print(position1)

        position=position1[:-1]

        # print(position)

        name=tr.find('a',class_='unstyled articleLink').get_text().split()
        # print(name)

        n=""
        for i in range(len(name)):

            n+=name[i]
        # print(n)

        rating=tr.find("td", class_="no-wrap").get_text().strip()

        # print(rating)
        
        link=tr.find('a',class_='unstyled articleLink')

        url=link["href"]

        link1="https://www.rottentomatoes.com"+url

        # print(link1)
        
        detailes={}

        detailes['Position']=position
        detailes['Name']=n
        detailes['Rating']=rating
        detailes['Url']=link1
        for i in range(len(year)):
            detailes["Year"]=year[i]
        top_movie_list.append(detailes)

        # detailes={}

    with open("movie_list1.json","w") as f:

        json.dump(top_movie_list, f,indent=6)

    return top_movie_list

top_movie_list=scrap_top_list()
    
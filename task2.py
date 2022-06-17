import requests
import json
from bs4 import BeautifulSoup
import pprint
from task1 import top_movie_list

def group_by_year(movie):

    years=[]
    d={}
    for i in movie:
        if i["Year"] not in years:
            years.append(i['Year'])
    # print(years) 
    for i in years:
        d[i]=[]
    # print(d)
    for j in movie:
        year=j['Year']
        # print(year)
        for k in d:
            if str(k)==str(year):
                d[k].append(j)
    # return d

    with open("movie_year2.json","w") as f:
        json.dump(d, f,indent=6)

    return d

# group_by_year(top_movie_list)

dec=group_by_year(top_movie_list)
    
# scrap_top_list()









# d={'a':2,'b':5}
# k=str(input('enter key:'))
# if k in d:
#     del d[k]
#     print(d)
# elif k not in d:
#     d[k]=6
#     print(d)


# def list1(l):
#     n=int(input('enter:'))
#     sum=0
#     for i in range(len(l)):
#         if n<l[i]:
#             sum+=l[i]
#     return sum
# print(list1([1,2,3,4,5,6,7,8,9,10]))
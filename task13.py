# import requests
# import json
# from bs4 import BeautifulSoup
# import pprint
# import os
# from task1 import top_movie_list
# from task5 import movie_list
# from task12 import cast_list
# from task12 import scrape_movie_cast
# # print(cast_list)
# cast=[]
# movie_cast_list=[]
# for i in top_movie_list:
#     url=i['Url']
#     def movie_detail_cast(url,movie_list):
#         # file_name="movie_details_cast_13.json"
#         page=requests.get(url)
#         soup=BeautifulSoup(page.text,"html.parser")
#         tag=soup.find("div",class_="castSection")
#         alltags=tag.find_all('div',class_="cast-item media inlineBlock")
#         # print(alltags)
#         # dic={}
#         for cast in alltags:
#             link=cast.find('a',class_='unstyled articleLink')
#             link1=link['href']
#             # print(link1)
#             name=cast.find('span').get_text().strip()
#             # print(name)
#             dic={}
#             dic['link']=link1
#             dic['name']=name
#             # print(dic)
#             movie_cast_list.append(dic)
#         for i in movie_list:
#             i['Cast']=movie_cast_list
#         # print(movie_list)
#         with open("movie_details_cast_13.json","w") as f:
#             data=json.dump(movie_list, f,indent=6)
#         # pprint.pprint(data)
#         return data
#     movie_detail_cast(url,movie_list)
    #     file_name="movie_details_cast_13.json"
    #     # file=os.path.exists(file_name)
    #     # if file==True:
    #     #     with open(file_name) as f:
    #     #         data=json.load(f)
    #     #     # print(data)
    #     #     return data
    #     # else:
    #     # cast=[]
    #     # a=scrape_movie_cast
    #     # a=cast_list
    #     # for j in cast_list:
    #     #     a=j
    #         # print(a)
    #     for i in movie_list:
    #             # print(i)
    #         # for j in cast_list:
    #         i['cast']=scrape_movie_cast(url)
    #         cast.append(movie_list)
    #     pprint.pprint(cast)

    #     with open(file_name,"w") as f:
    #         data=json.dump(cast, f,indent=6)
    #     # pprint.pprint(data)
    #     return data
    # movie_detail_cast(movie_list,cast_list)


# for i in range(5,1,-1):
#     print(i)
# # print(range(0,5,-1))


# a=12E4
# print(a)

for i in range(11):
# i=0
# while i<10:
#     # print(i)
    # i+=1
    if i==5:
        continue
        # break
    # else:
    print(i)
    # i+=1

# i = 0
# while i < 9:
# #   i += 1
#     if i == 3:
#         continue
#     i+=1
#     print(i)
    
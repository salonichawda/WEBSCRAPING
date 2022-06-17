import requests
import json
from bs4 import BeautifulSoup
import pprint
from task5 import movie_list

def analyse_language_and_directors(movie_list):
    # print(movie_list)
    direct_dic={}
    for movie in movie_list:
        director=movie['Director']
        direct_dic[director]={}
        count=0
        for i in range(len(movie_list)):
            if director==movie_list[i]['Director']:
                language=movie_list[i]['Original Language']
                count+=1
                direct_dic[director].update({language:count})
    with open("language_and_directors10.json","w") as f:
        json.dump(direct_dic, f,indent=6)
    print(direct_dic)

analyse_language_and_directors(movie_list)





# f1="saloni"
# with open("data\ file","x") as f:
#     a=f.write(f1)
    
# print(a)



# i=61
# d={}
# while i<71:
#     b=i
#     b-=60
#     d.update({b:b**2})
#     i+=1
# print(d)


# a=[2,3,4,[5,6,7,[8,9,10]]]
# b=[]
# for i in a:
#     if type(i)==list:
#         for j in i:
#             if type(j)==list:
#                 for k in j:
#                     b.append(k)
#             else:
#                 b.append(j)
#     else:
#         b.append(i)
# print(b)



# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])==list:
#                 k=0
#                 while k<len(a[i][j]):
#                     b.append(a[i][j][k])
#                     k+=1
#             else:
#                 b.append(a[i][j])
#             j=j+1
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)


# a=int(input("enter:"))
# b=int(input('enter:'))
# i=1
# while i<=b:
#     print(a,"*",i,"=",a*i)
#     i+=


# a=12
# b=2
# c=a/(1/b)
# print(c)
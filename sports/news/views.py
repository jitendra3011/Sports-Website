# from django.shortcuts import render
# from newsapi import NewsApiClient
  
# # Create your views here. 
# def news(request):
      
#     newsapi = NewsApiClient(api_key ='a2b3ad48257f4a1090d6db0f8040bb86')
#     top = newsapi.get_top_headlines(sources ='sports')
  
#     l = top['articles']
#     desc =[]
#     news =[]
#     img =[]
  
#     for i in range(len(l)):
#         f = l[i]
#         news.append(f['title'])
#         desc.append(f['description'])
#         img.append(f['urlToImage'])
#     mylist = zip(news, desc, img)
  
#     return render(request, 'news.html', context ={"mylist":mylist})


from django.shortcuts import render
from django.http import JsonResponse
import json


def news(request):
    import requests
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=a2b3ad48257f4a1090d6db0f8040bb86")
    api=json.loads(news_api_request.content)
    return render(request,'news.html',{'api':api})
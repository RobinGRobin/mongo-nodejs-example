import requests
from bs4 import BeautifulSoup
import json

search_url = requests.get("https://cnnespanol.cnn.com/tag/red-5g/")
url_html = BeautifulSoup(search_url.content, 'html.parser')

# Search for data in each news
a_media = url_html.find_all("a", class_="news__media-item")
a_title = url_html.find_all("h2", class_="news__title")

cont = 0
for a_media_content in a_media:
    cont = cont+1

a_media_src = []
a_title_nme = []
a_link_news = []

for a in range(cont):
    a_media_src.append(a_media[a].find("img").get("data-lazy-src"))
    a_title_nme.append(a_title[a].find("a").get("title"))
    a_link_news.append(a_title[a].find("a").get("href"))

# Function for getting the content from each article
def getAuthor(type, url):
    art_content = requests.get(url)
    art_content_parsed = BeautifulSoup(art_content.content, 'html.parser')
    if type == 'video':
        a_author = art_content_parsed.find("p", class_="news__byline").find("span").find("span").string
    else:
        a_author = art_content_parsed.find("p", class_="storyfull__authors").find("a").string
    return a_author

# Function for getting the publication date
def getDate(type, url):
    art_date = requests.get(url)
    art_date_parsed = BeautifulSoup(art_date.content, 'html.parser')
    if type == 'video':
        a_date = art_date_parsed.find("time", class_="news__date").string
    else:
        a_date = art_date_parsed.find("time", class_="storyfull__time").string
    return a_date

# Validate if the content of the article is in a video and getting the author
a_author_data = []
a_date_data = []
a_type = []
atk = 0
for c in range(cont):
    validation = a_link_news[c].split(sep='/')
    for validation_char in validation:
        if validation_char == 'video':
           atk = 1
    if atk == 1:
        a_type.append('video')
        a_author_data.append(getAuthor('video', a_link_news[c]))
        a_date_data.append(" ".join(getDate('video',a_link_news[c]).split()))
    else:
        a_type.append('article')
        a_author_data.append(getAuthor('article', a_link_news[c]))
        a_date_data.append(getDate('article',a_link_news[c]).strip())
    atk = 0

# Request to API for creating articles
url = "http://localhost:3000/article"
#jsonData = json.dumps({'title'=a_title_nme[0], 'author'=a_author_data[0], 'date'=a_date_data[0], 'mediaSource'=a_media_src[0], 'source'=a_link_news[0]});
jsonStream = {
    'title':a_title_nme[0],
    'author':a_author_data[0],
    'date':a_date_data[0],
    'mediaSource':a_media_src[0],
    'source':a_link_news[0]
}
r = requests.post(url, json=jsonStream)
r.status_code


for b in range(cont):
     print("Article ", b, " title: ", a_title_nme[b])
     print("Author: ", a_author_data[b])
     print("Date: ", a_date_data[b])
     print("Media source: ", a_media_src[b])
     print("Link: ", a_link_news[b])
     print("")
     jsonStream = {
         'title':a_title_nme[b],
         'author':a_author_data[b],
         'date':a_date_data[b],
         'mediaSource':a_media_src[b],
         'source':a_link_news[b]
     }
     r = requests.post(url, json=jsonStream)
     r.status_code

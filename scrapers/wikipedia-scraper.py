import bs4 as bs
from pymongo import MongoClient
import requests
import wikipedia

url = "https://en.wikipedia.org/wiki/"
pages = []

search = "cricket"
titles = wikipedia.search(search, 1000, False)
print(len(titles))
i = 0
for title in titles:
	print(i)
	i += 1
	new_url = url + title
	r = requests.get(new_url)
	soup = bs.BeautifulSoup(r.content, 'lxml')
	body = soup.body
	paras = body.find_all('p')
	for para in paras:
		pages.append(para.text)

client = MongoClient('localhost', 27017)
db = client.wikipedia

for page in pages:
	doc = {'text': page, 'search': search}
	db.articles.insert_one(doc)

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	from bs4 import BeautifulSoup 
	import requests,csv

	URL = 'https://techcrunch.com/'
	source = requests.get(URL).text
	soup = BeautifulSoup(source,"html.parser")
	tc_data = []
	tc_items = soup.find_all('div',class_='post-block post-block--image post-block--unread')
	for i in tc_items:
		tc_data.append((i.find('a',class_='post-block__title__link').text.strip(),i.find('a',class_='post-block__title__link')['href'],i.find('img')['src'].split('?')[0]))

	URL='https://www.theverge.com/tech/'
	source = requests.get(URL).text
	soup = BeautifulSoup(source,"html.parser")
	tv_data = []
	tv_items = soup.find_all('div',class_='c-entry-box--compact c-entry-box--compact--article')
	for i in tv_items:
		tv_data.append((i.find('h2').text,i.find('h2').a['href'],i.find_all('img')[1]['src']))

	URL = 'https://www.wired.com/most-recent/'
	source = requests.get(URL).text
	soup=BeautifulSoup(source,"html.parser")
	items = soup.find_all('li',class_="archive-item-component")
	w_data = []
	for i in items:
	    w_data.append((i.find('h2').text, URL[:-13] + i.find('a',class_="archive-item-component__link")['href'] , i.find('div',class_="archive-item-component__img").find('img')['src'] ))

	URL='https://in.mashable.com/tech/'
	source = requests.get(URL).text
	soup = BeautifulSoup(source,"html.parser")
	ms_data = []
	ms_items = soup.find_all('div', class_='wrapper is_channel')[0].find_all('a')
	new_items = soup.find(id='new').find_all('li')
	for i in new_items:
	    ms_data.append((i.find_all('a')[1].text, i.find('a')['href'], i.find('img')['data-src'] ))		
	rising_items = soup.find(id='rising').find_all('li')
	for i in rising_items:
	    ms_data.append((i.find_all('a')[1].text,  i.find_all('a')[1]['href'], i.find('img')['data-src'] ))
	for i in ms_items:
	    ms_data.append((i.text[4:], URL[:-5] + i['href'], ''))


	#CNET
	URL='https://www.cnet.com/news/'
	source = requests.get(URL).text
	soup = BeautifulSoup(source,"html.parser")
	cnet_data = []
	# cnet_items = soup.find_all('div',class_='riverPost')
	# for i in cnet_items:
	# 	cnet_data.append((i.find('a', class_="assetHed").text.strip(), i.a['href'], i.img['src']))

	cnet_items = soup.find_all('div',class_='assetWrap')
	for i in cnet_items:
		cnet_data.append((i.find(class_='assetHed').text.strip(),i.find(class_='assetHed')['href'],i.img['src']))


	# gizmodo	
	URL='https://gizmodo.com/latest'
	source = requests.get(URL).text
	soup = BeautifulSoup(source,'html.parser')
	gizmodo_data = []
	gizmodo_items = soup.find_all('article')
	for i in gizmodo_items:
	    title = i.h2.text.strip()
	    try:
	        link = i.figure.a['href']
	    except:
	        link = i.a['href']
	    try:
	        img = i.img['data-srcset'].split(' ')[4]
	    except:
	        img = ""
	    gizmodo_data.append((title,link,img))

	context = {'tc_data':tc_data, 'tv_data':tv_data,'w_data':w_data, 'ms_data':ms_data, 'cnet_data':cnet_data, 'gizmodo_data':gizmodo_data }
	return render(request,'newsag/home3.html', context)

import os
from bs4 import BeautifulSoup
import requests
import telebot
import schedule
import time

API_KEY = '5636091834:AAFP1TLallmgSccD-w1v1aJ8ta8jq9n_x_w'
bot = telebot.TeleBot(API_KEY)
channel = '@BoxOfficeY'

url = requests.get('https://www.imdb.com/chart/boxoffice')
soup = BeautifulSoup(url.content, 'html.parser')
table = soup.find('tbody')
list = table.find_all('tr')
date = soup.find('h4')

def random():
	
    urll = requests.get('https://ssnvalidator.net/test/get-movie.php')

    sup = urll.json()
    t= "#Title :   "+sup["title"]
    y="#Year :   "+sup["year"]
    p ="#Plot :   "+sup["description"]
    g = t+'\n'+y+'\n'+p +'\n @BoxOfficeY'
    bot.send_photo(channel, sup["image"], caption=g) 
   
    

def link():
	bot.send_message(channel,' \U0001f31a For Updated Information || @BoxOfficeY ||')



									 
def datefun():
   bot.send_message(channel,'__________________________________________\n||  Box Office Top 10 (US)\n||  '+date.text+'\n||  Join @BoxOfficeY ')


def post():
    
    for top in list:
        
			  
        h = top.find('td', class_='titleColumn')
        m = top.find('td', class_='ratingColumn')
        k = top.find(class_='secondaryInfo')
        w = top.find(class_='weeksColumn')
       
     
        bot.send_message(channel, '______________________________________\n\U0001f3ac Title :   '+ h.a.text + '\n______________________\n\U0001f4b8 This Week : ' + m.text.strip() + '\n\U0001f4b0 Total Gross : ' + k.text.strip() + '\n\U0001f501 Week : ' + w.text.strip())
	

schedule.every().tuesday.at("15:30:30").do(link)
schedule.every().tuesday.at("15:30:00").do(datefun)
schedule.every().tuesday.at("15:30:05").do(post)
schedule.every(120).minutes.do(random)
while True:
 
    schedule.run_pending()
    time.sleep(1)

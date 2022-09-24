import os
from bs4 import BeautifulSoup
import requests
import telebot

API_KEY = '5636091834:AAFP1TLallmgSccD-w1v1aJ8ta8jq9n_x_w'
bot = telebot.TeleBot(API_KEY)
channel = '@BoxOfficeY'
n = 1 
url = requests.get('https://www.imdb.com/chart/boxoffice')
soup = BeautifulSoup(url.content, 'html.parser')
table = soup.find('tbody')
list = table.find_all('tr')
date = soup.find('h4')
bot.send_message(channel,date)
@bot.message_handler(commands=['boxo'])

def boxo(message):
    	
    for top in list:
       
			  
        h = top.find('td', class_='titleColumn')
        m = top.find('td', class_='ratingColumn')
        k = top.find(class_='secondaryInfo')
        w = top.find(class_='weeksColumn')
       
     
        bot.send_message(
            channel, "___________________________\n"+n+"."+ h.a.text + "  << \n________________\n This Week : " +
            m.text.strip() + "\n Total Gross : " + k.text.strip() +
            "\n Weeks : " + w.text.strip())
	n+=1

bot.polling()

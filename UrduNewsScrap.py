import time

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen , Request
filename = "EXP_try-News_sports_urdu.csv"
f= open(filename,"w",encoding='utf-16')
headers = "news, date, Category\n"
#f = open(filename , "w" , encoding='utf-32')
f.write(headers)

import requests
n=1
while n <= 11:

   m = str(n)
   url = "https://www.express.pk/sports/archives/?page="+m
   #uclien = uReq(ul)  # main page link request
   page = requests.get(url).text  # page Reading

   psoup = soup(page, "html.parser")
   page= psoup.select(".meta")[0]

   print(page.get_text)
   #page = psoup.select(".meta")
   #print(coniner)
   for con in coniner:   #Now explore each title in the page
     ref = con.get('href')    #get href of each title

     uclen = uReq(ref)
     pag = uclen.read()
     uclen.close()
     psou = soup(pag, "html.parser")

     if (psou.find("a", {"class": "span-16 story-content last mobile-story-content fix-l-r"})):  # find para class from page which contain abstracts
         coer = psou.find("a", {"class": "Para"})
         coer = coer.getText()
         coer = coer.replace(",", " ")
         print(coer)

         try:
             f.write(coer + "\n")
         except:
             print("Exception")
     print(n)

   #
f.close()
# time.sleep(.25)
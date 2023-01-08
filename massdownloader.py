import os
import requests
import datetime
from datetime import date
from datetime import timedelta
import time
import schedule
from bs4 import BeautifulSoup

def downloader(date):

    #This is probably unnecessary but its cool so i keep it
    months = ['January', 'February', 'March',
              'April', 'May', 'June',
              'July', 'August', 'September',
              'October', 'November', 'December']

    
    save_path = os.getcwd()
    year = str(date.year)
    month = str(int(date.month)) + " " + str(months[int(date.month) - 1])
    
    #find todays comic
    todays_comic = date.strftime("https://www.gocomics.com/garfield/%Y/%m/%d")
    todays_filename = "Garfield " + str(date) + ".png"
    
    completeName = os.path.join(save_path, year, month, todays_filename)
    #checks if directory is there, if it isnt, creates it
    os.makedirs(os.path.dirname(completeName), exist_ok=True)
    
    #get comic
    response = requests.get(todays_comic)
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.select('div img')
    #5th element is the comic
    images_url = images[4]['src']
    img_data = requests.get(images_url).content
    
    #download comic
    with open(completeName, 'wb') as handler: 
        handler.write(img_data)
    print("Downloaded " + str(date))

if __name__ == '__main__':
    newMonth = False
    lastMonth = -1
    start_date = date(2021, 2, 1)
    end_date = date(2022, 12, 26)
    delta = timedelta(days=1)
    while start_date <= end_date:
        downloader(start_date)
        if start_date.month is not lastMonth:
            #this line is to see the downloads passing by in cmd window
            print("NEW DIRECTORY HAS BEEN CREATED FOR THE NEW MONTH AND OR YEAR FOR COMICS")
            lastMonth = start_date.month
        start_date += delta
    print("--------------------------DONE--------------------------")

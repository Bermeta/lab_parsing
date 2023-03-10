import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from time import sleep
import os

from selenium.webdriver.common.by import By

apartments_url = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273"
os.environ['PATH'] += "/home/bermet/Desktop/lab_parsing/chromedriver"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(apartments_url)


def write_to_csv(data):
    with open('Apart.file', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow((data['price'],
                         data['date'],
                         data['image']))


def prepare_csv():
    with open('Apart.file', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(('price', 'date', 'image'))


sleep(30)
for i in range(1, 101):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    data = soup.find_all('div', class_='clearfix')
    for d in data:
        try:
            price = d.find('div', class_='price') \
                .text.strip() \
                .replace('Please Contact', 'NO PRICE!') \
                .replace('\n', '').replace(' ', '-')
        except:
            price = 'NO PRICE!'
        try:
            date = d.find('span', class_='date-posted').text.replace('<', '')
        except:
            date = 'NO DATE!'
        try:
            image = d.find('div', class_='image').find('img').get('src')
        except:
            image = 'NO IMAGE!'
        data_ = {'price': price, 'date': date, 'image': image}
        write_to_csv(data_)

    next_button_link = driver.find_element(By.CSS_SELECTOR, "a[title=Next]")
    next_button_link.click()
    sleep(20)


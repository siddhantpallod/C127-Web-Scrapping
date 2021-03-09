from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time, csv

startUrl = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome(r'C:/Users/siddh/Downloads/chromedriver/chromedriver.exe')
browser.get(startUrl)
time.sleep(10)


def scrapper():
    headers = ['Name', 'Light_Years_From_Earth', 'Planet_Mass', 'Stellar_Magnitude', 'Discovery_Date']
    planetData = []
    for i in range(0, 437):
        soup = bs(browser.page_source, 'html.parser')

        for ul_tag in soup.find_all('ul', attrs = {'class', 'exoplanet'}):

            li_tags = ul_tag.find_all('li')
            tempList = []

            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    tempList.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        tempList.append(li_tag.contents[0])
                    except:
                        tempList.append('')

            planetData.append(tempList)        

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

    with open('scrapper.csv', 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetData)

scrapper()
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions


from selenium.webdriver.chrome.options import Options
#Table Tennis MEN's RANKINGS
#url to scrape from table tennis website

driver = webdriver.Chrome()
driver.get('http://results.ittf.link/index.php?option=com_fabrik&view=list&listid=70&Itemid=207')

#If you want to find a more specific attr for a tag, use attrs= to either find class name
output_rows = []
#SCRAPING all the table data
def scraping(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.findAll('table')[1].find('tbody', attrs={'class': 'fabrik_groupdata'})
    x = table.findAll('tr')[1:]
    num = 0
    for table_row in x:
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            updated_column = [column.text.strip('\n').strip('\t').strip('Click here').strip('')]
            if (len(output_row) == 7):
                break
            if (updated_column == ['']):
                if len(column.contents) == 0:
                    output_row.append('')
                else:
                    if column.contents.__len__() == 1:
                        if column.contents[0] == '\n':
                            if "title" in column.contents[1].attrs.keys():
                                updated_column_geo = column.contents[1].attrs["title"]
                                output_row.append(updated_column_geo)

                        else:
                            if "title" in column.contents[0].attrs.keys():
                                updated_column_geo = column.contents[0].attrs["title"]
                                output_row.append(updated_column_geo)
                    elif(len(column.contents) > 1):
                        if "title" in column.contents[1].attrs.keys():
                            updated_column_geo = column.contents[1].attrs["title"]
                            output_row.append(updated_column_geo)

            else:
                output_row.append(updated_column[0])

        output_rows.append(output_row)
        num = num + 1






#python_button = driver.find_element_by_css_selector('#list_69_com_fabrik_69 > tfoot > tr > td > div > div > div.pagination > ul > li.pagination-next > a')
#This is to search for the "next" button of the ittf webpage, so that it can scrape another 50 or so players
#a = soup.findAll('table')[1].find('tfoot').find('tr', attrs={'class': 'fabrik___heading'})
#a_href = a.find('ul', attrs={'class':'pagination-list'}).find('li', attrs={'class': 'pagination-next'}).find('a').attrs['href']
#a_href_url = 'https://results.ittf.link' + a_href
#a_new = a_href_url
count = 0
str_num = 50

wait = ui.WebDriverWait(driver,10)
def exceptioncatch():
    counter = 0
    attempts = 0
    while attempts < 2:
        try:
            python_button = driver.find_element_by_xpath(
                '//*[@id="list_70_com_fabrik_70"]/tfoot/tr/td/div/div/div[2]/ul/li[13]/a')
            if counter == 0:
                html_source = driver.page_source
                scraping(html_source)
            else:
                driver.execute_script("arguments[0].click();", python_button)
                time.sleep(10)
                html = driver.page_source
                scraping(html)

            print('Successful: ' + str(counter))
            counter = counter + 1
            #Adjust this counter
            if counter == 19:
                break
        except StaleElementReferenceException as Exception:
            print('Exception')
            attempts = attempts + 1

exceptioncatch()



    #Adjust this based on how many table pages there are

#Using Pandas Dataframes
dataset = pd.DataFrame(output_rows)
headers = ['Country','Player (ITTF ID)', 'Position', 'Previous Position', 'Points', 'Month', 'Year']
dataset.columns = headers
dataset.to_csv("ProfessionalTableTennisWomenWorldRankingsExperiment.csv", index = False)
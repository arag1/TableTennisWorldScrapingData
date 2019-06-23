import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd

#Table Tennis Women's RANKINGS
#url to scrape from table tennis website
url =  'http://results.ittf.link/index.php?option=com_fabrik&view=list&listid=70&Itemid=207'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#If you want to find a more specific attr for a tag, use attrs= to either find class name
table = soup.findAll('table')[1].find('tbody', attrs={'class': 'fabrik_groupdata'})
output_rows = []
x = table.findAll('tr')[1:]
#SCRAPING all the table data
def scraping():
    num = 0
    for table_row in x:
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            updated_column = [column.text.strip('\n').strip('\t').strip('Click here').strip('')]
            if(updated_column == ['']):
                if column.contents[0] == '\n':
                    if len(column.contents) == 1:
                        output_row.append('')
                        return
                    if "title" in column.contents[1].attrs.keys():
                        updated_column_geo = column.contents[1].attrs["title"]
                        output_row.append(updated_column_geo)

            else:
                output_row.append(updated_column[0])

        output_rows.append(output_row)
        num = num+1
scraping()
#This is to search for the "next" button of the ittf webpage, so that it can scrape another 50 or so players
a = soup.findAll('table')[1].find('tfoot').find('tr', attrs={'class': 'fabrik___heading'})
a_href = a.find('ul', attrs={'class':'pagination-list'}).find('li', attrs={'class': 'pagination-next'}).find('a').attrs['href']
a_href_url = 'https://results.ittf.link' + a_href
a_new = a_href_url
count = 0
str_num = 50
counter = 0
while a_new is not None:
    response = requests.get(a_new)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.findAll('table')[1].find('tbody', attrs={'class': 'fabrik_groupdata'})
    x = table.findAll('tr')[1:]
    scraping()
    str_num_new = str_num + 50
    str_num_concat = str(str_num_new)
    counter = counter + 1
    print('Successful: ' + str(counter))
    a_new = a_new.replace(str(str_num), str_num_concat)
    str_num += 50
    count = count + 1
    #Adjust this based on how many table pages there are
    if(count == 19):
       break

#Using Pandas Dataframes
dataset = pd.DataFrame(output_rows)
headers = ['Country','Player (ITTF ID)', 'Position', 'Previous Position', 'Points', 'Month', 'Year']
dataset.columns = headers
dataset.to_csv("ProfessionalTableTennisWomenWorldRankings.csv", index = False)


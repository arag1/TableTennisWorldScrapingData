import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd

#url to scrape from table tennis website
url =  'http://results.ittf.link/index.php?option=com_fabrik&view=list&listid=69&Itemid=206'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#If you want to find a more specific attr for a tag, use attrs= to either find class name
table = soup.findAll('table')[1].find('tbody', attrs={'class': 'fabrik_groupdata'})
output_rows = []
x = table.findAll('tr')[1:]
#SCRAPING all the table data
for table_row in x:
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        updated_column = [column.text.strip('\n').strip('\t').strip('Click here').strip('')]
        #Removing empty list from a list conditional statement
        if (updated_column != ['']):
            output_row.append(updated_column[0])
    output_rows.append(output_row)
#Using Pandas Dataframes
dataset = pd.DataFrame(output_rows)
headers = ['Player (ITTF ID)', 'Position', 'Previous Position', 'Points', 'Month', 'Year']
dataset.columns = headers
dataset.to_csv("Top50ProfessionalTableTennisWorldRankings.csv", index = False)


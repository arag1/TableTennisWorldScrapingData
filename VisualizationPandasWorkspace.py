import pandas as pd
from geopy import geocoders
import pycountry_convert as pc
#importing csv file generated from TableTennisMenRANKINGSREV.py

mens_rankings = pd.read_csv("ProfessionalTableTennisMenWorldRankingsExperiment.csv")
#print(mens_rankings)

#Printing column for country of men's rankings in Dataframe
#print(mens_rankings[["Country"]])

#iloc experiment: prints out all the values in a particular row, in this case iloc[2] prints out all the entries in the 3rd row
#print(mens_rankings.iloc[2][0])

#shows the first 5 rows
#print(mens_rankings.head())

country = mens_rankings[["Country"]]
country_two = country['Country'].value_counts()
df = pd.DataFrame({'Country':country_two.index, 'Count':country_two.values})
#print(df)

country_list = df['Country'].tolist()
new_list = []
for x in country_list:
    if x.title() == 'Republic Of Korea':
        x = 'South Korea'
        country_code = pc.country_name_to_country_alpha2(x.title(), cn_name_format="default")
    elif x.title() == 'Chinese Taipei':
        x = 'Taiwan'
        country_code = pc.country_name_to_country_alpha2(x.title(), cn_name_format="default")
    elif x.title() == 'United States Of America':
        x = 'USA'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == "Democratic People'S Republic Of Korea":
        x = 'North Korea'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == "Congo Democratic":
        x = 'Congo'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == "England":
        x = 'United Kingdom'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == "Scotland":
        x = 'United Kingdom'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == "Cote D'Ivoire":
        x = "South Africa"
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == "Congo Brazzaville":
        x = 'Congo'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == "Tahiti":
        x = 'French Polynesia'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == 'Trinidad And Tobago':
        x = 'Venezuela'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == 'North Macedonia':
        x = 'Bulgaria'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == 'Wales':
        x = 'United Kingdom'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == 'Kosovo':
        x = 'Montenegro'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == 'Fiji Islands':
        x = 'Fiji'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == 'Bosnia & Herzegovina':
        x = 'Bosnia and Herzegovina'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    elif x.title() == 'Phillipines':
        x = 'Philippines'
        country_code = pc.country_name_to_country_alpha2(x, cn_name_format="default")
    else:
        country_code = pc.country_name_to_country_alpha2(x.title(), cn_name_format="default")
    continent_name = pc.country_alpha2_to_continent_code(country_code)
    new_list.append(continent_name)
    words = [w.replace('AS', 'Asia').replace('AF', 'Africa').replace('EU', 'Europe').replace('OC', 'Oceania').replace('SA', 'South America').replace('NA', 'North America') for w in new_list]

df['Continents'] = words
df.to_csv("NumberofPlayersinTableTennis.csv", index = False)

print(df)
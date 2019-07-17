library(ggplot2)
worldtabletenniscounts <- read.csv("/Users/anurag/PycharmProjects/WEBSCRAPINGSIDEPROJECT/NumberofPlayersinTableTennis.csv")
worldtabletenniscounts
firstfiverows <- worldtabletenniscounts[1:5, 1:3]
firstfiverows
row<- firstfiverows[c(2)] / sum(firstfiverows[c(2)])
firstfiverows[c(4)] <- row
firstfiverows
#Stacked bar plot for the most number of players representing their country in Asia[DESCENDING ORDER] for first three countries
firstthreerows <- worldtabletenniscounts[1:3, 1:3]
row<- firstthreerows[c(2)] / sum(firstthreerows[c(2)])
firstthreerows[c(4)] <- row
ggplot(firstthreerows, aes(Continents, weight = Count.1)) + geom_bar(aes(fill=Country), position = "fill") + ggtitle("The Most players Representing Each Table Tennis Country") + geom_text(aes(label = Count, y = Count.1, group=Country), position = position_fill(vjust = .5))
#Stacked bar plot for the most number of players representing their country in Asia, Africa and Europe for first five countries
ggplot(firstfiverows, aes(Continents, weight = Count.1)) + geom_bar(aes(fill=Country), position = "fill") + ggtitle("The Most players Representing Each Table Tennis Country") + geom_text(aes(label = Count, y = Count.1, group=Country), position = position_fill(vjust = .5))
#Creating heatmap of most players in Asia
library(dplyr)
worldtabletenniscounts <- worldtabletenniscounts[-c(1)]
#Grouping column by aggregrating data to sum up total column
worldtabletennis <- aggregate(Count ~ Continents, worldtabletenniscounts, sum)
library(rworldmap)
data(gridExData)
library(rworldmap)
sPDF <- getMap()  
mapCountryData(sPDF, nameColumnToPlot='continent')
worldtabletennis['index'] <- c(1,2,3,4,5,6)
worldtabletennis

library(rgeos)
library(rgdal)
library(ggplot2)
library(httr)
library(maptools)

install.packages("gpclib", type = "source")
gpclibPermit()

url <- "https://gist.githubusercontent.com/hrbrmstr/91ea5cc9474286c72838/raw/f3fde312c9b816dff3994f39f2bcda03209eff8f/continents.json"
stop_for_status(GET(url, write_disk("continents.json")))
continents <- readOGR("continents.json", "OGRGeoJSON")
continents_map <- fortify(continents, region="CONTINENT")
gg <- ggplot()
gg <- gg + geom_map(data=continents_map,
                    map=continents_map,
                    aes(x=long, y=lat, map_id=id),
                    color="black")
gg <- gg + geom_map(data=worldtabletennis,
                    map=continents_map,
                    aes(map_id=Continents, fill=Count),
                    color="black")
gg <- gg + scale_fill_distiller("# of Players") # needs latest ggplot2
gg <- gg + coord_equal()
gg <- gg + theme_bw()
gg <- gg + labs(x=NULL, y=NULL)
gg <- gg + theme(panel.border=element_blank())
gg <- gg + theme(panel.grid=element_blank())
gg <- gg + ggtitle("Table Tennis Players Representing Each Continent")
gg

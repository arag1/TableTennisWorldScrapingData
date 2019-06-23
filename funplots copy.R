#MAKING GRAPHS WITH Table Tennis Men's Data
library(ggplot2)
tabletennis <- read.csv("/Users/anurag/PycharmProjects/WEBSCRAPINGSIDEPROJECT/ProfessionalTableTennisMenWorldRankingsExperiment.csv")
a <- data.frame(tabletennis)
a
lapply(a, count)
#Dropping columns by index: Specifically dropping columns 2 thru 7
#Only keeping countries
df <- a[-c(2:7)]
df
colnames(df)
myfreq<-count(df, vars="Country") 
#Making Country occurences into a table
country<-table(df$"Country")
#Creating it back to dataframe
new_country_set <- as.data.frame(country)
#Renaming column by index
names(new_country_set)[1] <- "Country" 

#ONE PLOT
first_five_countries <- new_country_set[c(1:5), c(1:2)]
#ggplot example for five countries bar graph, number of players occurences
#geom_text fills text inside or outside bars with numbers or frequencies for the numbers of players in Table
ggplot(first_five_countries, aes(Country, Freq)) + geom_col(fill="blue4") + geom_text(aes(label=Freq), vjust=1.6, color="white", size=3.5) + theme_minimal()

#SECOND PLOT
second_five_countries <- new_country_set[c(6:10), c(1:2)]
#size for geom_text tampers or plays with font size
ggplot(second_five_countries, aes(Country, Freq)) + geom_col(fill="salmon1") + geom_text(aes(label=Freq), vjust=1.6, color="white", size=4) + theme_minimal()

third_five_countries <- new_country_set[c(11:15), c(1:2)]
ggplot(third_five_countries, aes(Country, Freq)) + geom_col(fill="goldenrod3") + geom_text(aes(label=Freq), vjust=1.6, color="white", size=3.5) + theme_minimal()

#THIRD PLOT
fourth_five_countries <- new_country_set[c(16:20), c(1:2)]
ggplot(fourth_five_countries, aes(Country, Freq)) + geom_col(fill="aquamarine4") + geom_text(aes(label=Freq), vjust=1.6, color="white", size=3.5) + theme_minimal()


# fifth_five_countries <- new_country_set[c(21:25), c(1:2)]
# ggplot(fifth_five_countries, aes(Country, Freq)) + geom_col(fill="chocolate1") + geom_text(aes(label=Freq), vjust=1.6, color="white", size=3.5) + theme_minimal()
# 
# sixth_five_countries <- new_country_set[c(26:30), c(1:2)]
# ggplot(sixth_five_countries, aes(Country, Freq)) + geom_col(fill="blue4") + geom_text(aes(label=Freq), vjust=1.6, color="white", size=3.5) + theme_minimal()
# 
# seventh_five_countries <- new_country_set[c(31:35), c(1:2)]
# ggplot(seventh_five_countries, aes(Country, Freq)) + geom_col(fill="blue4") + geom_text(aes(label=Freq), vjust=1.6, color="white", size=3.5) + theme_minimal()
# 
# eighth_five_countries <- new_country_set[c(36:40), c(1:2)]
# ggplot(eighth_five_countries, aes(Country, Freq)) + geom_col(fill="blue4") + geom_text(aes(label=Freq), vjust=1.6, color="white", size=3.5) + theme_minimal()
# 
# ninth_five_countries <- new_country_set[c(41:45), c(1:2)]
# ggplot(ninth_five_countries, aes(Country, Freq)) + geom_col(fill="blue4") + geom_text(aes(label=Freq), vjust=1.6, color="white", size=3.5) + theme_minimal()
# 
# tenth_five_countries <- new_country_set[c(46:50), c(1:2)]
# ggplot(tenth_five_countries, aes(Country, Freq)) + geom_col(fill="blue4") + geom_text(aes(label=Freq), vjust=1.6, color="white", size=3.5) + theme_minimal()








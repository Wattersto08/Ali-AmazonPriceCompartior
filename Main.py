from AliScraper import Scrape_Ali
from Utils import ALI_Convertcost

a,b = Scrape_Ali(input('What would you like to search for?  '), int(input('How many pages would you like to search?  ')))

print(len(a))
for i in range(len(a)):

    print(a[i] + ' - ' + str(ALI_Convertcost(b[i])))
               


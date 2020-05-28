from AliScraper import Scrape_Ali
from Utils import ALI_Convertcost, Output_CSV


_search = input('What would you like to search for?  ')
_pages = int(input('How many pages would you like to search?  '))



a,b = Scrape_Ali(_search,_pages)

print('%d products found!' %len(a))

#for i in range(len(a)):

   # print(a[i] + ' - ' + str(ALI_Convertcost(b[i])))

Output_CSV(a,b,_search)               


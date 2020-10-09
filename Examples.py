'''
John Curran

This program uses the election scraper to pull data from Dave Leip's Atlas of US Presidential Elections.
Below are several examples of what the web scraper can accomplish. Feel free to edit this program 
and perform any data pulls you wish.


Bibliography
Dave Leip's Atlas of U.S. Presidential Elections. http://uselectionatlas.org (17 September 2020)


required modules: requests, numpy, pandas, openpyxl, colored, BeautifulSoup
If the program does not compile, try "pip install" on these modules
'''

import ElectionScraper as es

all_states = ["Alabama", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "DC", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",\
"Iowa", "Kansas", "Kentucky", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", \
"New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", \
"South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

if __name__ == "__main__":
	es.create_simple_excel("California", 2008)
	es.create_swing_excel("Michigan", 1984, 1996)
	es.create_simple_mapchart(all_states, 2008)
	es.create_swing_mapchart(["Michigan", "Wisconsin", "Minnesota", "Ohio", "Indiana", "Illinois", "Iowa"], 2008, 2016)
	es.create_margin_mapchart(all_states, 1964)
	es.create_margin_mapchart(["Tennessee", "North Carolina", "South Carolina", "Georgia", "Florida", "Alabama", "Mississippi", "Arkansas", "Texas"], 1968)
	
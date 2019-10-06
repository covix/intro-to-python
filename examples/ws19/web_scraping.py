import requests
from bs4 import BeautifulSoup

url = "https://www.eventi.garr.it/it/ws19/programma/workshop"

r = requests.get(url)  # get the search url using requests
soup = BeautifulSoup(r.content)  # create a BeautifulSoup object 'soup' of the content

# extract all the events in the workshop
#'find_all' method is used to find the  matching criteria as mentioned in parenthesis
events = soup.find_all("tr", {"class": "uk-alert uk-alert-table"})

for event in events:
    time = event.find("h4").text.strip()
    desc = event.find("p").text.strip()

    print(f"{time}\t{desc}")

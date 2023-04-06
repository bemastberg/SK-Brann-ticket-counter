import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True
driver = selenium.webdriver.Chrome(r'C:\Users\bemas\Downloads\chromedriver_win32 (2)\chromedriver.exe', options=options)
html = urlopen("https://ticketco.events/no/nb/events/254926/seating_arrangement/?item_type_id=13643680&_ga=2.240639427.171245730.1680800463-862292630.1665493683")
soup = BeautifulSoup(html.read(), 'html.parser')

sections = soup.find('g', {'id':'text'}).find_all('a')
sections = [section for section in sections if len(section.text) == 3]
ticketsAvailable = 0
ticketsSold = 0
for section in sections:
    if len(section.text) == 3:
        #print("https://ticketco.events/no/nb/events/254926/seating_arrangement/" + section['xlink:href'])
        html = "https://ticketco.events/no/nb/events/254926/seating_arrangement/" + section['xlink:href']
        driver.get(html)
        #time.sleep(3)
        seats = driver.find_elements(By.CLASS_NAME,'tc-section--seat')
        sold = []
        available = []
        for i in seats:
            if i.get_attribute('data-status') == 'sold':
                sold.append(i)
            elif i.get_attribute('data-status') == 'available':
                available.append(i)
        ticketsAvailable += len(available)
        ticketsSold += len(sold)
        print(f"Ledige seter på felt {section.text}: {len(available)}")
        print(f"Solgte seter på felt {section.text}: {len(sold)}")
print(f"Totalt ledige seter: {ticketsAvailable}")
print(f"Totalt solgte seter: {ticketsSold}")







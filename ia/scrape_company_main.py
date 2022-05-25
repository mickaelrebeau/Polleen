import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs
from time import time, sleep
import pandas as pd

# For use Chrome
from webdriver_manager.chrome import ChromeDriverManager

s = Service('chromedriver_win32/chromedriver.exe')
options = webdriver.ChromeOptions()
# options.add_argument('--headless')

browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.maximize_window()

df = pd.read_csv("profile_scrape.csv")
companys = df["Company"]

for company in companys:

    # Go to societe.com
    browser.get('https://www.societe.com/cgi-bin/search?champs=+' + company)

    src = browser.page_source
    soup = bs(src, 'lxml')

    ents = soup.select('.ResultSearch__result .ResultBloc__link')

    for ent in ents:
        if ent["data-href"].startswith("/societe/"):
            url = "https://www.societe.com/" + ent["data-href"]
            browser.get(url)
            sleep(2)

            src = browser.page_source
            soup = bs(src, 'lxml')

            # Scroll to the bottom
            start = time()
            initialScroll = 0
            finalScroll = 200

            while True:
                browser.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
                initialScroll = finalScroll
                finalScroll += 100
                sleep(2)
                end = time()
                if round(end - start) > 20:
                    break

            card = soup.find("div", {'id': 'siren_number'})

            siret_loc = card.select_one(".copyNumber__number")
            siret = None

            if siret_loc:
                siret = siret_loc.get_text().strip()

            benefice_loc = soup.find("tr", {'class': 'numdisplay txt-right'})
            benefice = None

            if benefice_loc:
                benefice = benefice_loc.get_text().strip()

            data = {
                "Siret": siret, "Bénéfice": benefice,
            }

            data = pd.DataFrame.from_dict([data])
            df = df.append(data, ignore_index=True)

df.to_csv(r'test_scrape.csv', encoding='utf-8', index=False, header=True)
browser.quit()

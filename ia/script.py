import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs
from time import time, sleep
import pandas as pd
import environ
from Polleen.settings import BASE

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(BASE, '0.env'))

# For use Chrome
s = Service('chromedriver_win32/chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser = webdriver.Chrome(service=s, options=options)
# browser.maximize_window()

# Open login page
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

username = env('LINKEDIN_USERNAME')
password = env('LINEDIN_PASSWORD')

# Enter login information
elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

# Go to webpage
browser.get('https://www.linkedin.com/mynetwork/')

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

src = browser.page_source
soup = bs(src, 'lxml')
prospects = soup.select('a.discover-entity-type-card__link')
# if the csv file doesn't exist, create it
if not os.path.exists('../Polleen/ia/profile_scrape.csv'):
    df = pd.DataFrame()
else:
    df = pd.read_csv('../Polleen/ia/profile_scrape.csv')

for prospect in prospects:
    if prospect["href"].startswith("/in"):
        # Go to a process profile
        profile_url = "https://www.linkedin.com" + prospect["href"]
        browser.get(profile_url)
        sleep(2)

        src = browser.page_source
        soup = bs(src, 'lxml')
        intro = soup.find('div', {'class': 'mt2 relative'})

        # Extracting the Name
        name_loc = intro.select_one(".text-heading-xlarge")
        name = None

        if name_loc:
            name = name_loc.get_text().strip()

        # Extracting the Description
        description_loc = intro.find("div", {'class': 'text-body-medium'})
        description = None

        if description_loc:
            description = description_loc.get_text().strip()

        # Extracting the Post
        post_loc = soup.select_one("#experience-section ul li:first-child h3")
        post = None

        if post_loc:
            post = post_loc.get_text().strip()

        # Extracting the Company Name
        company_loc = soup.select_one("[aria-label='Entreprise actuelle']")
        company = None

        if company_loc:
            company = company_loc.get_text().strip()

        # Extracting the location
        location_loc = intro.select_one(".pb2.pv-text-details__left-panel span")
        location = None

        if location_loc:
            location = location_loc.get_text().strip()

        # Go to the coordinate
        coordinate_url = profile_url + "detail/contact-info/"
        browser.get(coordinate_url)

        # Extracting the e-mail
        src = browser.page_source
        soup = bs(src, 'lxml')

        email_loc = soup.select_one("section.ci-email a")
        email = None

        if email_loc:
            email = email_loc.get_text().strip()

        # Save data
        data = {
            "Name": name, "Description": description, "Location": location, "Post": post, "Company": company,
            "Email": email, "Url profile": profile_url
        }
        # save data in csv from a dict
        data = pd.DataFrame.from_dict([data])
        df = df.append(data, ignore_index=True)
        '''
        Show the information
        print("Name -->", name,
              "\nTitle -->", title,
              "\nLocation -->", location,
              "\nPost -->", post,
              "\nCompany -->", company,
              "\nMail -->", email,
              "\nProfil URL -->", profil_url,
              )
        '''

df.to_csv(r'profile_scrape.csv', encoding='utf-8', index=False, header=True)

browser.quit()

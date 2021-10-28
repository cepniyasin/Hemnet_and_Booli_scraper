from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time


def hemnet_parser():
    try:
        main = [WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH,
                                        "//li[@class='normal-results__hit js-normal-list-item']")))]
        for articles in main:

            for article in articles:
                global counter
                counter += 1
                # print("\nArticle:", counter)
                link = article.find_element(By.CLASS_NAME, "listing-card").get_attribute('href')
                # print(link)
                # print(article.text)
                apartment = article.find_element(By.CLASS_NAME, "listing-card__address").text.split("\n")
                address = apartment[0]
                location = apartment[1]
                # print(address)
                # print(location)
                attributes = article.find_element(By.CLASS_NAME, "listing-card__attributes-row")
                attribute_list = attributes.text.split("\n")
                price = attribute_list[0]
                area = None
                room = None
                if len(attribute_list) == 3:
                    area = attribute_list[1]
                    room = attribute_list[2]
                if len(attribute_list) == 2:
                    area = attribute_list[1]
                # print(price)
                # print(area)
                # print(room)

                property_type_list = article.find_element(By.CLASS_NAME, 'listing-card__location'
                                                     ).get_attribute("textContent").split("\n")
                property_type = property_type_list[2]

                write_csv(str(counter), link, address, location, price, area, room, property_type)

    except Exception as e:
        print(e)
        driver.close()


def hemnet_sold_parser():
    try:
        main = [WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH,
                                                 "//li[@class='sold-results__normal-hit']")))]
        for articles in main:
            for article in articles:
                global counter
                counter += 1
                link = article.find_element(By.CLASS_NAME, "hcl-card").get_attribute('href')

                apartment = article.find_element(By.CLASS_NAME, "sold-property-listing__location").text.split("\n")
                address = apartment[0]
                location = apartment[2]
                property_type = apartment[1]
                price_list = article.find_elements(By.CLASS_NAME, "clear-children")
                price = price_list[1].text
                date_of_sale = price_list[2].text
                sizes = article.find_element(By.CLASS_NAME, "clear-children").text.split("\n")
                area = sizes[0]
                avgift = None
                if len(sizes) > 1:
                    avgift = sizes[1]

                write_csv_sold(str(counter), link, address, location, price, area, avgift, property_type, date_of_sale)

    except Exception as e:
        print(e)
        driver.close()


def start_csv():
    date = str(datetime.datetime.today()).split()[0]
    global csv_file
    csv_file = open(f'{date +"-"+ location}.csv', 'w')
    csv_file.write(f'{date}' + "\n")
    csv_file.write('Count'
                   + ';' + 'Website Link'
                   + ';' + 'Subject'
                   + ';' + 'Location'
                   + ';' + 'Price'
                   + ';' + 'Area'
                   + ';' + 'Number of rooms'
                   + ';' + 'Property Type'
                   + ';' + 'Status'
                   + "\n")


def write_csv(id, link, address, location, price, area, room, property_type, date_of_sale="For Sale"):
    global csv_file
    csv_file.write(f'{id}'
                   + ';' + f'{link}'
                   + ';' + f'{address}'
                   + ';' + f'{location}'
                   + ';' + f'{price}'
                   + ';' + f'{area}'
                   + ';' + f'{room}'
                   + ';' + f'{property_type}'
                   + ';' + f'{date_of_sale}'
                   + "\n")


def start_csv_sold():
    date = str(datetime.datetime.today()).split()[0]
    global csv_file
    csv_file = open(f'{date +"-"+ location +"-"+"slutpris"}.csv', 'w')
    csv_file.write(f'{date}' + "\n")
    csv_file.write('Count'
                   + ';' + 'Website Link'
                   + ';' + 'Subject'
                   + ';' + 'Location'
                   + ';' + 'Price'
                   + ';' + 'Area and number of rooms'
                   + ';' + 'Avgift'
                   + ';' + 'Property Type'
                   + ';' + 'Status'
                   + "\n")


def write_csv_sold(id, link, address, location, price, area, avgift, property_type, date_of_sale="For Sale"):
    global csv_file
    csv_file.write(f'{id}'
                   + ';' + f'{link}'
                   + ';' + f'{address}'
                   + ';' + f'{location}'
                   + ';' + f'{price}'
                   + ';' + f'{area}'
                   + ';' + f'{avgift}'
                   + ';' + f'{property_type}'
                   + ';' + f'{date_of_sale}'
                   + "\n")

def ask_slutpris():
    slutpris = input("Do you want to make the search for sold properties? [y/n]: ")
    if slutpris == "y":
        return True
    if slutpris == "n":
        return False
    else:
        ask_slutpris()

location = input("Give a location to search: ")

sold = ask_slutpris()

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://www.hemnet.se/')
# print(driver.title)
driver.implicitly_wait(5)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='hcl-button hcl-button--primary']")))
element.click()
driver.implicitly_wait(5)

if sold:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//label[@class='search-tabs__tab-link']")))
    element[-1].click()

search = driver.find_element(By.ID, "area-search-input-box")
search.clear()
search.send_keys(location)
time.sleep(2)
search.send_keys(Keys.RETURN)

element = driver.find_elements(By.CLASS_NAME, "icon-checkbox__label")
element[1].click()
element[2].click()
element[3].click()
element[4].click()


element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//div[@class='start-search-form__sticky-submit js-sticky-submit-control']")))
element.click()
counter = 0

if not sold:
    start_csv()
    hemnet_parser()
if sold:
    start_csv_sold()
    hemnet_sold_parser()

next_page = True

while next_page:
    try:
        if not sold:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//div[@class='pagination__item pagination__item--responsive']")))
            element.click()
            hemnet_parser()
        if sold:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//a[@class='next_page hcl-button hcl-button--primary hcl-button--full-width']")))
            element.click()
            hemnet_sold_parser()

    except Exception as e:
        print("\nALL FINISHED - You can find the results csv file in the same directory.")
        next_page = False
        # time.sleep(2)
        driver.quit()


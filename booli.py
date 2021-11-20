from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time


# def hemnet_parser():
#     try:
#         main = [WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.XPATH,
#                                         "//li[@class='normal-results__hit js-normal-list-item']")))]
#         for articles in main:
#
#             for article in articles:
#                 global counter
#                 counter += 1
#                 link = article.find_element(By.CLASS_NAME, "listing-card").get_attribute('href')
#                 apartment = article.find_element(By.CLASS_NAME, "listing-card__address").text.split("\n")
#                 address = apartment[0]
#                 location = apartment[1]
#                 attributes = article.find_element(By.CLASS_NAME, "listing-card__attributes-row")
#                 attribute_list = attributes.text.split("\n")
#                 price = attribute_list[0]
#                 area = None
#                 room = None
#                 if len(attribute_list) == 2:
#                     area = attribute_list[1]
#                 elif len(attribute_list) == 3:
#                     area = attribute_list[1]
#                     room = attribute_list[2]
#
#                 property_type_list = article.find_element(By.CLASS_NAME, 'listing-card__location'
#                                                      ).get_attribute("textContent").split("\n")
#                 property_type = property_type_list[2]
#                 write_csv(str(counter), link, address, location, price, area, room, property_type)
#
#     except Exception as e:
#         print(e)
#         driver.close()


def hemnet_sold_parser():
    main = [WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH,
                                                 "//div[@class='_2m6km uC2y2 _3oDFL']")))]
    # print(main[0][0].text)

    all_articles = main[0][0].text

    all_articles = all_articles.split("%\n")

    # print(all_articles)

    all_articles_cleaned = []

    for i in all_articles:
        x = i.split("\n")
        if len(x) > 13:
            y = ""
            for n in x:
                y += n + '\n'
            y = y.split('—')
            for v in y:
                v = v.split("\n")
                z = []
                for q in v:
                    if len(q) > 0:
                        z.append(q)
                print(z)
                print(len(z))
                all_articles_cleaned.append(z)

        elif len(x) > 2:
            all_articles_cleaned.append(x)
            print(x)
            print(len(x))
    # print(all_articles_cleaned)

    # # try:
    #     main = [WebDriverWait(driver, 10).until(
    #         EC.presence_of_all_elements_located((By.XPATH,
    #                                                      "//li[@class='sold-results__normal-hit']")))]
    #
    #     print(main)
    #     for articles in main:
    #         for article in articles:
    #             # print(article.text)
    #             global counter
    #             counter += 1
    #             link = article.find_element(By.XPATH,
    #                                              "//a[@class='sold-property-link']").get_attribute('href')
    #             apartment = article.find_element(By.CLASS_NAME, "sold-property-listing__location").text.split("\n")
    #             address = apartment[0]
    #             print (address)
    #             location = apartment[2]
    #             property_type = apartment[1]
    #             price_list = article.find_elements(By.CLASS_NAME, "sold-property-listing__price-info")
    #             x = price_list[0].text.split("\n")
    #             avgift = None
    #             land_area = None
    #             price = x[0]
    #             date_of_sale = x[1]
    #             # print(price, date_of_sale)
    #
    #
    #
    #             sizes = article.find_elements(By.CLASS_NAME, "sold-property-listing__size")
    #             # print (sizes[0])
    #                 # article.find_element(By.CLASS_NAME, "clear-children").text.split("\n")
    #             a = sizes[0].text.split("\n")
    #             # print(a)
    #             area = a[0]
    #             # print(area)
    #             if len(a) > 1:
    #                 if "m²" in a[1]:
    #                     land_area = a[1]
    #                 if "kr/mån" in a[1]:
    #                     avgift = a[1]
    #
    #                 # print(avgift)
    #                 # print(land_area)
    #             write_csv_sold(str(counter), link, address, location, price, area,land_area, avgift, property_type, date_of_sale)
    # #
    # # except Exception as e:
    # #     print(e)
    # #     driver.close()

#
# def start_csv():
#     date = str(datetime.datetime.today()).split()[0]
#     global csv_file
#     csv_file = open(f'{date +"-"+ location}.csv', 'w')
#     csv_file.write(f'{date}' + "\n")
#     csv_file.write('Count'
#                    + ';' + 'Subject'
#                    + ';' + 'Location'
#                    + ';' + 'Price'
#                    + ';' + 'Area'
#                    + ';' + 'Number of rooms'
#                    + ';' + 'Property Type'
#                    + ';' + 'Status'
#                    + ';' + 'Website Link'
#                    + "\n")
#
#
# def write_csv(id, link, address, location, price, area, room, property_type, date_of_sale="For Sale"):
#     global csv_file
#     csv_file.write(f'{id}'
#                    + ';' + f'{address}'
#                    + ';' + f'{location}'
#                    + ';' + f'{price}'
#                    + ';' + f'{area}'
#                    + ';' + f'{room}'
#                    + ';' + f'{property_type}'
#                    + ';' + f'{date_of_sale}'
#                    + ';' + f'{link}'
#                    + "\n")


def start_csv_sold():
    date = str(datetime.datetime.today()).split()[0]
    global csv_file
    csv_file = open(f'{date +"-"+ location +"-"+"slutpris"}.csv', 'w')
    csv_file.write(f'{date}' + "\n")
    csv_file.write('Count'
                   + ';' + 'Subject'
                   + ';' + 'Location'
                   + ';' + 'Price'
                   + ';' + 'Area and number of rooms'
                   + ';' + 'Land Size'
                   + ';' + 'Avgift'
                   + ';' + 'Property Type'
                   + ';' + 'Status'
                   + ';' + 'Website Link'
                   + "\n")


def write_csv_sold(id, link, address, location, price, area,land_area, avgift, property_type, date_of_sale="For Sale"):
    global csv_file
    csv_file.write(f'{id}'
                   + ';' + f'{address}'
                   + ';' + f'{location}'
                   + ';' + f'{price}'
                   + ';' + f'{area}'
                   + ';' + f'{land_area}'
                   + ';' + f'{avgift}'
                   + ';' + f'{property_type}'
                   + ';' + f'{date_of_sale}'
                   + ';' + f'{link}'
                   + "\n")

# def ask_slutpris():
#     slutpris = input("Do you want to make the search for sold properties? [y/n]: ")
#     if slutpris == "y":
#         return True
#     if slutpris == "n":
#         return False
#     else:
#         ask_slutpris()


location = input("Give a location to search: ")

# sold = ask_slutpris()

start = time.time()

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://www.booli.se/slutpriser/sverige/77104?objectType=Fritidshus')
driver.implicitly_wait(5)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
element.click()
driver.implicitly_wait(5)

counter = 0

start_csv_sold()
hemnet_sold_parser()

next_page = True

while next_page:
    try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[contains(text(),'Nästa sida')]")))
            element.click()
            time.sleep(1)
            driver.implicitly_wait(5)
            hemnet_sold_parser()

    except Exception as e:
        print(e)
        csv_file.close()
        print("\nALL FINISHED - You can find the results csv file in the same directory.")
        next_page = False
        driver.quit()

end = time.time()
print('\nElapsed time:', int(end - start), 'seconds')
print("Article found:", counter)
input("\nPress return to quit.\n\n\ncepniyasin.com")
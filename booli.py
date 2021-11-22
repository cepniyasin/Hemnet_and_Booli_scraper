from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time


def start_csv_sold():
    date = str(datetime.datetime.today()).split()[0]
    global csv_file
    csv_file = open(f'{date +"-"+ location +"-"+"slutpris"}.csv', 'w')
    csv_file.write(f'{date}' + "\n")
    csv_file.write('Count'
                   + ';' + 'Subject'
                   + ';' + 'Area and number of rooms'
                   + ';' + 'Price'
                   + ';' + 'Location'
                   + ';' + 'Property Type'
                   + ';' + 'Sold Date'
                   + "\n")


def write_csv_sold(id, address, location, area, property_type, price, date_of_sale="For Sale"):
    global csv_file
    csv_file.write(f'{id}'
                   + ';' + f'{address}'
                   + ';' + f'{location}'
                   + ';' + f'{price}'
                   + ';' + f'{area}'
                   + ';' + f'{property_type}'
                   + ';' + f'{date_of_sale}'
                   + "\n")


def hemnet_sold_parser():
    time.sleep(7)

    article_list = []

    main = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH,
                                             "//div[@class='_1EcEF iF9uQ']")))
    for i in main:
        address = None
        area = None
        location = None
        property_type = None
        if i:
            article = i.text.split('\n')
            address = article[0]
            global counter

            if len(article) == 3:
                area = article[1]
                location = article[2].split(", ")[1]
                property_type = article[2].split(", ")[0]

            if len(article) == 2:
                location = article[1].split(", ")[1]
                property_type = article[1].split(", ")[0]

            article_list.append([address, area, location, property_type])

    main = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH,
                                            "//div[@class='_1EcEF MJ2C2']")))
    index_count = 0
    for i in main:
        price = None
        date_of_sale = None
        if i:
            article2 = i.text.split('\n')
            price = article2[0]
            date_of_sale = article2[-1]
            article_list[index_count].append(price)
            article_list[index_count].append(date_of_sale)
        index_count += 1

    for item in article_list:
        counter += 1
        write_csv_sold(str(counter), item[0], item[1], item[2], item[3], item[4], item[5])


location = input("Give a name to output CSV file: ")
search_page = input("\nThe link to the starting page of the search: ")

start = time.time()

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get(f'{search_page}')
time.sleep(2)
driver.implicitly_wait(5)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
element.click()
driver.implicitly_wait(5)

counter = 0
count_error = 0

start_csv_sold()

hemnet_sold_parser()

next_page = True
page = 0
while next_page:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Nästa sida')]")))
        element.click()
        page += 1
        print("Counter:", counter)
        print('PAGE: ',page)
        driver.implicitly_wait(5)
        hemnet_sold_parser()

    except Exception as e:
        # print(e)
        csv_file.write("\nUntil page: " + f'{page}' + "\n" + "Error: "+f'{count_error}')
        csv_file.close()
        print("\nALL FINISHED - You can find the results' csv file in the same directory.")
        next_page = False
        driver.quit()

end = time.time()

print('\nElapsed time:', int(end - start), 'seconds')
print("Article found:", counter)
print("Number of error:", count_error)

input("\nPress return to quit.\n\n\ncepniyasin.com")
print('Finished on page: ', page)

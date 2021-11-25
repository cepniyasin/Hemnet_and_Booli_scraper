import datetime

def start_csv_sold(run_counter):
    if run_counter == 0:
        run_counter += 1
        global new_file
        new_file = open(f'{date + "-" + property_title + "-" + "slutpris"}.csv', 'w')
        new_file.write(f'{date}' + "\n")
        new_file.write('Count'
                       + ';' + 'Subject'
                       + ';' + 'Area and number of rooms'
                       + ';' + 'Price'
                       + ';' + 'Location'
                       + ';' + 'Property Type'
                       + ';' + 'Sold Date'
                       + "\n")
        new_file.close()


def write_csv_sold(id, address, location, area, property_type, price, date_of_sale):
    new_file = open(f'{date + "-" + property_title + "-" + "slutpris"}.csv', 'a')
    new_file.write(f'{id}'
                   + ';' + f'{address}'
                   + ';' + f'{location}'
                   + ';' + f'{price}'
                   + ';' + f'{area}'
                   + ';' + f'{property_type}'
                   + ';' + f'{date_of_sale}'
                   + "\n")


def get_data_from_csv():
    file = input("CSV file to add: ") # "2021-11-22-Blekinge-slutpris"
    infile = open(f'{file}.csv', 'r')
    # print(infile.read())
    temp = infile.read()
    temp = temp.split("\n")
    # print(temp)
    temp2 = []
    for n in range(len(temp)):
        temp2.append(temp[n].split(";"))
    # print(len(temp2))
    for n in range(len(temp2)):
        if n != 0 and n != 1 and n != len(temp2) - 1 and n != len(temp2) - 2 and n != len(temp2) - 3:
            data_line = temp2[n]
            if not check_exists(data_line):
                write_csv_sold(data_line[0], data_line[1], data_line[2], data_line[3], data_line[4], data_line[5], data_line[6])
                # print(data_line)

# Detects Duplicates
def check_exists(data_line):
    date = str(datetime.datetime.today()).split()[0]
    open_new_file = open(f'{date + "-" + property_title + "-" + "slutpris"}.csv', 'r')
    temp = open_new_file.read()
    temp = temp.split("\n")
    # print(temp)
    temp2 = []
    for n in range(len(temp)):
        temp2.append(temp[n].split(";"))
    # print(len(temp2))
    for n in range(len(temp2)):
        if n != 0 and n != 1 and n != len(temp2) - 1:  # and n != len(temp2) - 2 and n != len(temp2) - 3:
            existing_data_line = temp2[n]
            if existing_data_line[1] == data_line[1] and existing_data_line[6] == data_line[6]:
                # print(existing_data_line)
                return True







date = str(datetime.datetime.today()).split()[0]

run_counter = 1 # CHANGE THIS TO ZERO DURING THE FIRST RUN.

property_title = "Fritidhus"

start_csv_sold(run_counter)

get_data_from_csv()
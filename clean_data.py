
def start_csv():
        global new_file
        new_file = open(f'{title}.csv', 'w')
        new_file.write('Count'
                       + ';' + 'Subject'
                       + ';' + 'Price in SEK'
                       + ';' + 'Number of Rooms'
                       + ';' + 'Area in m²'
                       + ';' + 'Property Type'
                       + ';' + 'Location'
                       + ';' + 'Sold Date'
                       + '\n'
                       )
        new_file.close()

def write_csv_sold(id, address, room, area, price, location, property_type, date_of_sale):
    new_file = open(f'{title}.csv', 'a')
    new_file.write(f'{id}'
                   + ';' + f'{address}'
                   + ';' + f'{location}'
                   + ';' + f'{room}'
                   + ';' + f'{area}'
                   + ';' + f'{price}'
                   + ';' + f'{property_type}'
                   + ';' + f'{date_of_sale}'
                   + "\n")

counter = 0
def get_data_from_csv():
    file = input("CSV file to add: ")
    infile = open(f'{file}.csv', 'r')
    temp = infile.read()
    temp = temp.split("\n")
    temp2 = []
    for n in range(len(temp)):
        temp2.append(temp[n].split(";"))
    for n in range(len(temp2)):
        if n not in (0, 1, len(temp2)-1, len(temp2)-2, len(temp2)-3, len(temp2)-4):
            global counter
            counter += 1
            if n == len(temp2) - 5:
                print(counter)
            data_line = temp2[n]
            data_line = separate_area(data_line)
            data_line[2] = clean_text(data_line[2])
            data_line[3] = clean_text(data_line[3])
            data_line[5] = clean_text(data_line[5])

            write_csv_sold(id=data_line[0], address=data_line[1], room=data_line[2],
                           area=data_line[3], price=data_line[4], location=data_line[5],
                               property_type=data_line[6], date_of_sale=data_line[7])


def clean_text(text):
    temp = ""
    if text:
        for i in text:
            if 47 < ord(i) < 58:
                temp+=i
    if text is None:
        temp = "Missing"
    return temp


def separate_area(data_line):
        temp = data_line
        area_room = temp[2]
        # print(area_room)
        if area_room != None:
            if "," in area_room:
                area_room = area_room.split(",")
            elif "m²" in area_room:
                area_room = [None, area_room]
            elif "rum" in area_room:
                area_room = [area_room, None]
            elif area_room == "":
                pass
            else:
                area_room = [None, None]
        else:
            area_room = [None, None]

        temp[2] = area_room
        data_line = [temp[0], temp[1],temp[2][0],temp[2][1],temp[3],temp[4],temp[5],temp[6]]
        # print(data_line)
        return data_line

title = input("Name the file: ")
start_csv()
get_data_from_csv()




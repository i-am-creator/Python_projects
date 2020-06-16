# import
import random
import time
from tkinter import *
from PIL import Image, ImageTk
import glob
# constant

INCOME_TAX = 100
SIZE_OF_DICEimg = 70
AMMOUNT_IN_STARTING = 25000
MINIMUM_BANK_BALLANCE = -1000
BANK = - MINIMUM_BANK_BALLANCE * 12
FINE_FOR_JAIL = 500
player_colours = ['#808080', '#ff0000', '#ffff00', '#00ff00', '#ff00ff', '#8080ff', '#00ffff', '#008000']
random.shuffle(player_colours)
coordinate_of_box = []
# game constant
SALARY = 1500
JAIL_FINE = 500
addrs = glob.glob("New folder (2)/*.jpeg")  # background imz

places1 = {
    'Mumbai': {'rent': 1000, "price": 10000},
    'Delhi': {'rent': 700, "price": 7000},
    'Bangalore': {'rent': 1200, "price": 12000},
    'Hyderabad': {'rent': 500, "price": 5000},
    'Ahmedabad': {'rent': 400, "price": 4000},
    'Chennai': {'rent': 800, "price": 8000},
    'Kolkata': {'rent': 250, "price": 2500},
    'Pune': {'rent': 750, "price": 7500},
    'Jaipur': {'rent': 150, "price": 1500},
    'Kanpur': {'rent': 450, "price": 4500},
    'Nagpur': {'rent': 250, "price": 2500},
    'Lucknow': {'rent': 500, "price": 5000},
    'New_Delhi': {'rent': 1500, "price": 15000},
    'Bhopal': {'rent': 450, "price": 4500},
    'Indore': {'rent': 550, "price": 5500},
    'Patna': {'rent': 250, "price": 250},
    'Ghaziabad': {'rent': 150, "price": 2000},
    'Agra': {'rent': 300, "price": 2500},
    'Varanasi': {'rent': 1500, "price": 10000},
    'Guwahati': {'rent': 250, "price": 2000},
    'Kota': {'rent': 800, "price": 5000},
    'Gorakhpur': {'rent': 650, "price": 6500},
    'Noida': {'rent': 1000, "price": 8500},
    'Dehradun': {'rent': 450, "price": 4500},
    'Jammu': {'rent': 250, "price": 2500}
}
places2 = {
    'water_park': {'rent': 2500, "price": 15000, "Tax": 500},
    'Electric_company': {'rent': 3500, "price": 25000, "Tax": 700},
    'Railway': {'rent': 5000, "price": 35000, "Tax": 1000},
    'AirLines': {'rent': 5500, "price": 40000, "Tax": 1100},
    'Motor_boat': {'rent': 3500, "price": 20000, "Tax": 700},
    'Resort': {'rent': 2500, "price": 15000, "Tax": 500}

}
# randomness for map
N = 10000

totalBox = 36
no_of_places1 = 23
no_of_places2 = 4
no_of_chance = 2
no_of_communityChest = 2
no_of_incomeTax = 2
unfilledBox = totalBox - 4
box = []
list_Of_Players = []
chance_of_player = 0
txt = None

# initilization
root = Tk()
root.attributes("-fullscreen", True)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
canvas = Canvas(root, width=w, height=h, bg='#020205')
canvas.pack()
canvas.images = list()
imgIndexD1 = None
imgIndexD2 = None
d1 = None
d2 = None
DICE_IMZ_POS = (w / 2, h / 2)
BigBox = None
alpha = .3
images = []
chance_pic = None
chance_pic_object = None

def create_rectangle(x1, y1, x2, y2, **kwargs):
    # global images
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2-x1, y2-y1), fill)
        images.append(ImageTk.PhotoImage(image))
        return canvas.create_image(x1, y1, image=images[-1], anchor='nw')
        # image = ImageTk.PhotoImage(image)
        # return canvas.create_image(x1, y1, image=image, anchor='nw')
    # canvas.create_rectangle(x1, y1, x2, y2, **kwargs)


def roleTheDice():
    # possible_outcome = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    # return 2 number B/N 1-6
    d1, d2 = random.randint(0, 5) + 1, random.randint(0, 5) + 1
    animateDice(d1, d2)
    return d1, d2




def animateDice(diceNo1, diceNo2):
    # animate the rolling dice and ends with diceNo

    global imgIndexD1, imgIndexD2, d1, d2
    x, y = DICE_IMZ_POS

    if imgIndexD1 != None or imgIndexD2 != None:
        canvas.delete(d1)
        canvas.delete(d2)

    for i in range(16):
        imagefile = 'Dice/animation' + str(i) + ".png"
        pic = Image.open(imagefile)
        pic = ImageTk.PhotoImage(pic)
        # pic = pic.resize(DICE_IMZ_SHAPE)
        d1 = canvas.create_image(x + SIZE_OF_DICEimg / 2, y, anchor=NW, image=pic)
        d2 = canvas.create_image(x - SIZE_OF_DICEimg / 2, y, anchor=NW, image=pic)
        canvas.update()
        time.sleep(.1)
        canvas.delete(d1)
        canvas.delete(d2)
    if imgIndexD1 == None:
        imagefile = 'Dice/' + str(diceNo1) + ".png"
        pic = Image.open(imagefile)
        pic = ImageTk.PhotoImage(pic)
        d1 = canvas.create_image(x + SIZE_OF_DICEimg / 2, y, anchor=NW, image=pic)
        canvas.images.append(pic)
        canvas.update()
        imgIndexD1 = len(canvas.images) - 1
    else:
        imagefile = 'Dice/' + str(diceNo1) + ".png"
        pic = Image.open(imagefile)
        pic = ImageTk.PhotoImage(pic)
        # pic = pic.resize(DICE_IMZ_SHAPE)
        d1 = canvas.create_image(x + SIZE_OF_DICEimg / 2, y, anchor=NW, image=pic)
        canvas.images[imgIndexD1] = pic
        canvas.update()

    if imgIndexD2 == None:
        imagefile = 'Dice/' + str(diceNo2) + ".png"
        pic = Image.open(imagefile)
        pic = ImageTk.PhotoImage(pic)
        # pic = pic.resize(DICE_IMZ_SHAPE)
        d2 = canvas.create_image(x - SIZE_OF_DICEimg / 2, y, anchor=NW, image=pic)
        canvas.images.append(pic)
        canvas.update()
        imgIndexD1 = len(canvas.images) - 1
    else:

        imagefile = 'Dice/' + str(diceNo2) + ".png"
        pic = Image.open(imagefile)
        pic = ImageTk.PhotoImage(pic)
        # pic = pic.resize(DICE_IMZ_SHAPE)
        d2 = canvas.create_image(x - SIZE_OF_DICEimg / 2, y, anchor=NW, image=pic)
        canvas.images[imgIndexD2] = pic
        canvas.update()


class PLAYER:
    def __init__(self, ID):
        self.name = None
        self.total_prop = AMMOUNT_IN_STARTING
        self.bank_balance = AMMOUNT_IN_STARTING
        self.NoOfProperties = 0
        self.ListOfPropertied = []
        self.cash = 0
        self.colour = player_colours[ID]
        self.id = ID
        self.chanceToBeMissed = 0
        self.houseNo = 0
        self.object = None
        self.name = None
        self.bankkrupt = False
        self.tax_C = 0
        self.player_imz = None

    def update_valriabe(self):
        self.NoOfProperties = len(self.ListOfPropertied)
        self.total_prop = self.bank_balance + self.cash
        self.tax_C = 0
        for prop in self.ListOfPropertied:
            if prop.type == 'C':
                self.tax_C += prop.tax
            self.total_prop += prop.cost


def players():
    # NoOfPlayer = int(input("no of players"))
    NoOfPlayer = 6
    if NoOfPlayer <= 0 or NoOfPlayer > 6:
        print("invalid choice \n enter no b/n 1 and 6")
        NoOfPlayer = int(input("no of players"))
    for i in range(NoOfPlayer):
        p = PLAYER(i)
        list_Of_Players.append(p)
        # name = input("name of player" + str(i))
        p.name = 'player' + str(i)


class BLOCK:
    def __init__(self):
        self.rectangle = None
        self.cost = 0
        self.win = 0
        self.rent = 0
        self.fine = 0
        self.tax = 0
        self.name = None
        self.type = "A"
        self.oner = None
        self.oner_rectangle = None
        self.box_no = None
        self.coordinates = None

    def update(self, player, diceNo):
        # a : start, JAIL, GO TO JAIL, REST HOUSE
        # B: PLACE 1
        # c: PLACE 2
        # D: communityChest
        # F: incomeTax

        # if self.oner:
        #     print(self.type, player.name, self.oner.name)
        Action = None
        if self.oner == player:
            Action = 'No Action'
            return Action
        else:
            if self.type == 'A':
                if self.name == 'jail':
                    # pay fine or miss chance
                    if player.bank_balance > self.fine:
                        # paying fine
                        player.bank_balance -= self.fine
                        Action = player.name + ' is paying fine $'  + str(self.fine)
                    else:
                        # missing chance
                        player.chanceToBeMissed = 3
                        Action = player.name + " is missing 3 chance"
                elif self.name == 'go_to_jail':
                    Action = 'Go To Jail'
                    player.houseNo = 9
                    Action = Action + " and" \
                                      "\n"
                    if player.bank_balance > self.fine:
                        # paying fine
                        player.bank_balance -= self.fine
                        Action += player.name + ' is paying fine $' + str(self.fine)
                    else:
                        # missing chance
                        player.chanceToBeMissed = 3
                        Action += player.name + " is missing 3 chance"
                    draw_players()
                    return Action
                elif self.name == 'rest_house':
                    Action = player.name + ' rest for 1 chance'
                    player.chanceToBeMissed = 1
            elif self.type == 'F':
                # tax = INCOME_TAX * player.NoOfProperties
                tax = int(player.total_prop * .05) # 5%
                player.bank_balance -= tax if tax > 0 else 100
                Action = player.name + ' is paying tax of $' + str(tax if tax > 0 else 100)
            elif self.type == 'B' or self.type == 'C':
                if self.oner == None:
                    if player.bank_balance - self.cost > MINIMUM_BANK_BALLANCE:
                        # buy property
                        player.bank_balance -= self.cost
                        Action = player.name + ' Buy ' + self.name + ' of cost $' + str(self.cost)
                        # add this amount to bankers account
                        self.oner = player
                        player.total_prop += 1
                        player.ListOfPropertied.append(self)
                    else:
                        Action = player.name + " can't buy this " + self.name + " BankBalance = $" + str(player.bank_balance) + ' & cost of property $' + str(self.cost)
                else:
                    if player.bank_balance - MINIMUM_BANK_BALLANCE > self.rent:
                        Action = player.name + ' is paying $' + str(self.rent) + ' to ' + self.oner.name
                        player.bank_balance -= self.rent
                        self.oner.bank_balance += self.rent
                    else:
                        if len(player.ListOfPropertied) == 0:
                            # player is bankkrupt
                            player.bankkrupt = True
                            Action = player.name + 'is bankkrupt'
                            return Action
                        else:
                            Action =  player.name +'sell a property to pay rent of' + str(self.rent) + '\n' + player.name + ' is paying $' + str(self.rent) + ' to ' + self.oner.name
                            # index = input('index of property to be sell from' + str([p.name for p in player.ListOfPropertied]))
                            # index = int(index)
                            prop = random.choice(player.ListOfPropertied)
                            # prop = player.ListOfPropertied[index]
                            player.bank_balance += prop.cost
                            player.ListOfPropertied.remove(prop)
                            prop.oner = None
                            player.bank_balance -= self.rent
                            self.oner.bank_balance += self.rent
                            # print(player.ListOfPropertied)

            elif self.type == 'D' or self.type == 'E':
                if diceNo % 2 == 0:
                    player.bank_balance += 500
                    Action = player.name + ' is geting $500 from ' + self.name
                else:
                    player.bank_balance -= 500
                    Action = player.name + ' is paying $500 to ' + self.name


            else:
                pass
                # if self.name == "jail":
                #     if player.bank_balance > FINE_FOR_JAIL:
                #         player.bank_balance -= FINE_FOR_JAIL
                #     else:
                #         pass
                # elif self.name == "go_to_jail":
                #     player.houseNo = 10
                #     if player.bank_balance > FINE_FOR_JAIL:
                #         player.bank_balance -= FINE_FOR_JAIL
                #     else:
                #         pass
                # elif self.name == "rest_house":
                #     pass
        return Action


def give_place(no, coordinates):
    global no_of_places1, no_of_places2, no_of_chance, no_of_communityChest, no_of_incomeTax, unfilledBox, SALARY
    place = BLOCK()
    place.box_no = no
    place.coordinates = coordinates
    # print(unfilledBox, no, '\n\n')

    # house
    if no == 0:
        # start
        place.name = "start"
        place.win = SALARY
    elif no == 9:
        # jail
        place.name = "jail"
        place.fine = JAIL_FINE
        # pay fine or miss 3 chance
    elif no == 18:
        # rest house
        place.name = "rest_house"
        # miss a chance
    elif no == 27:
        # go to jail
        place.name = "go_to_jail"
        place.fine = JAIL_FINE

    else:
        # no of places1 is 37-4-4-4-2 = 23
        # no of places2 is 4
        # 2 chance 2 community chest
        # 2 income tax
        a = random.randint(0, N)
        if a < N * no_of_places1 // unfilledBox:
            key = random.choice(list(places1))
            listOfPara = places1[key]
            del places1[key]
            # print(key, no_of_places1)
            place.name = key
            place.rent = listOfPara['rent']
            place.cost = listOfPara['price']
            place.type = 'B'
            no_of_places1 -= 1
            unfilledBox -= 1
        elif a < N * (no_of_places2 + no_of_places1) // unfilledBox:
            key = random.choice(list(places2))
            listOfPara = places2[key]
            del places2[key]
            # print(key, no_of_places2)
            place.name = key
            place.rent = listOfPara['rent']
            place.cost = listOfPara['price']
            place.type = 'C'
            place.tax = listOfPara['Tax']
            no_of_places2 -= 1
            unfilledBox -= 1
        elif a < N * (no_of_places2 + no_of_places1 + no_of_chance) // unfilledBox:
            # print('chance', no_of_chance)
            place.name = 'chance'
            place.type = 'D'
            no_of_chance -= 1
            unfilledBox -= 1
        elif a < N * (no_of_places2 + no_of_places1 + no_of_chance + no_of_communityChest) // unfilledBox:
            # print('communityChest', no_of_communityChest)
            place.name = 'communityChest'
            place.type = 'E'
            no_of_communityChest -= 1
            unfilledBox -= 1
        elif a < N * (
                no_of_places2 + no_of_places1 + no_of_chance + no_of_communityChest + no_of_incomeTax) // unfilledBox:
            # print('incomeTax', no_of_incomeTax - 1)
            place.name = 'incomeTax'
            place.type = 'F'
            no_of_incomeTax -= 1
            unfilledBox -= 1
        else:
            place = give_place(no, coordinates)
            # print('12345678', no)

    return place


def create_map():
    global k1, k2, box
    k1 = w // 10
    k2 = h // 10
    co = 0

    for i in range(10):
        j = 9 * k2
        # b = c.create_rectangle(i * k1, j, i * k1 + k1, j + k2, fill="#555555")
        coordinate = i * k1, j, i * k1 + k1, j + k2
        place = give_place(co, coordinate)
        box.append(place)
        # c.create_text(i * k1 + k1 / 2, j + k2 / 2, fill="darkblue", font="Times 15 italic bold", text=place.name)
        # text=str(co))
        co += 1
    for j in range(8, 0, -1):
        i = 9 * k1
        # b = c.create_rectangle(i, j * k2, i + k1, j * k2 + k2, fill="#555555")
        coordinate = i, j * k2, i + k1, j * k2 + k2
        place = give_place(co, coordinate)
        box.append(place)
        # c.create_text(i + k1 / 2, j * k2 + k2 / 2, fill="darkblue", font="Times 15 italic bold", text=place.name)
        # text=str(co))
        co += 1
    for i in range(9, -1, -1):
        j = 0
        # b = c.create_rectangle(i * k1, j, i * k1 + k1, j + k2, fill="#555555")
        coordinate = i * k1, j, i * k1 + k1, j + k2
        place = give_place(co, coordinate)
        # place = give_place(co, b, c)
        # place = give_place(co, b)
        box.append(place)
        # canvas.create_text(i * k1 + k1 / 2, j + k2 / 2, fill="darkblue", font="Times 15 italic bold",
        #               text=place.name)
        # text=str(co))
        co += 1
    for j in range(1, 9):
        i = 0 * k1
        # b = c.create_rectangle(i, j * k2, i + k1, j * k2 + k2, fill="#555555")
        coordinate = i, j * k2, i + k1, j * k2 + k2
        place = give_place(co, coordinate)
        # place = give_place(co, b, c)
        # place = give_place(co, b)
        box.append(place)
        # canvas.create_text(i + k1 / 2, j * k2 + k2 / 2, fill="darkblue", font="Times 15 italic bold",
        #               text=place.name)
        co += 1


def draw_map():
    canvas.delete("all")
    imagefile = addrs[1]
    pic = Image.open(imagefile)
    pic = ImageTk.PhotoImage(pic)
    canvas.create_image(0, 0, anchor=NW, image=pic)
    canvas.images.append(pic)
    canvas.update()
    for b in box:
        x1, y1, x2, y2 = b.coordinates
        k1 = w // 10
        k2 = h // 10
        if b.rectangle:
            canvas.delete(b.rectangle)
        rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill="#000000")
        canvas.create_text(x1 + k1 / 2, y1 + k2 / 2, fill="gray", font="Times 15 italic bold", text=b.name)
        b.rectangle = rectangle
        if b.oner:
            b.oner_rectangle =canvas.create_rectangle(x1, y1, x1 + 25, y1 + 10, fill=b.oner.colour)
    draw_players()
    draw_player_bio()

    canvas.update()

def mouse_pointer(event):
    index = None
    global BigBox, images
    for coordinate in coordinate_of_box:
        x1, y1, x2, y2 = coordinate
        if event.x > x1 and event.x < x2 and event.y > y1 and event.y < y2:
            index = coordinate_of_box.index((x1, y1, x2, y2))
            break
    if index!= None:
        x1 -= k1//2
        x2 += k1//2
        y1 -= k2//2
        y2 += k2//2
        if index <= 9:
            y1 -= k2//2
            y2 -= k2//2
        if index <= 18 and index >= 9:
            x1 -= k1//2
            x2 -= k1//2
        if index <= 27 and index >= 18:
            y1 += k2//2
            y2 += k2 // 2
        if index < 40 and index >= 27 or index == 0:
            x1 += k1//2
            x2 += k1//2
        if BigBox != None:
            canvas.delete(BigBox)
        if box[index].oner != None:
            colour = box[index].oner.colour
        else:
            colour = '#050505'
        BigBox = create_rectangle(x1, y1, x2, y2, fill = colour, alpha=alpha)
    else:
        canvas.delete(BigBox)
        # print(len(images))
        images = []
    pass

player_bio_Object = []
def draw_player_bio():
    # player 1
    global chance_pic_object, chance_pic
    for ob in player_bio_Object:
        canvas.delete(ob)
    k1 = w // 10
    k2 = h // 10
    const = 30
    x1 = k1 + k1 / 4
    y1 = k2 + k2 / 4
    x2 = x1 + k1 * 2 + k1 / 3
    y2 = y1 + k2 * 3
    for i in range(0, 3):
        player = list_Of_Players[i]
        player.update_valriabe()
        if player.bankkrupt:
            continue

        if chance_of_player == player.id:
            imagefile = 'player/100x150/player' + player.colour[1:] + ".png"
            pic = Image.open(imagefile)
            pic = ImageTk.PhotoImage(pic)
            chance_pic = pic
            chnace_pic_object = canvas.create_image(x1 - 10, y1 + 25, anchor=NW, image=pic)
        else:
            if chance_pic_object != None:
                canvas.delete(chance_pic_object)
                chance_pic_object = None

        player_bio_Object.append(canvas.create_text((x1 + x2) / 2, y1 + const, fill=player.colour, font="Times 25 bold", text=player.name))
        player_bio_Object.append(canvas.create_text((x1 + x2) / 2, y1 + const * 2, fill="#ffffff", font="Times 15",
                           text='Bank_Balance:' + str(player.bank_balance)))
        player_bio_Object.append(canvas.create_text((x1 + x2) / 2, y1 + const * 3, fill="#ffffff", font="Times 15",
                           text='total_prop:' + str(player.total_prop)))
        # canvas.create_text((x1 + x2 )/ 2, y2 + const*3, fill="#ffffff", font="Times 15", text= 'Cash:' + player.cash)
        string = ""
        line = y1 + const * 4
        for i in range(len(player.ListOfPropertied)):

            if i % 2 != 1 and i != len(player.ListOfPropertied) - 1:
                string = string + player.ListOfPropertied[i].name + '  '
                continue
            string = string + player.ListOfPropertied[i].name + '  '
            player_bio_Object.append(canvas.create_text((x1 + x2) / 2, line, fill="#ffffff", font="Times 15",
                               text=string))
            line = line + const
            string = ''

        x1 = x2 + k1 / 4
        x2 = x1 + k1 * 2 + k1 / 3
    x1 = k1 + k1 / 4
    y1 = h - k2 - k2 / 4
    x2 = x1 + k1 * 2 + k1 / 3
    y2 = y1 - k2 * 3
    for i in range(3, 6):
        player = list_Of_Players[i]
        player.update_valriabe()
        if player.bankkrupt:
            continue


        if chance_of_player == player.id:
            imagefile = 'player/100x150/player' + player.colour[1:] + ".png"
            pic = Image.open(imagefile)
            pic = ImageTk.PhotoImage(pic)
            chance_pic = pic
            chnace_pic_object = canvas.create_image(x1 + 0, y2 + 25, anchor=NW, image=pic)
        else:
            if chance_pic_object != None:
                canvas.delete(chance_pic_object)
                chance_pic_object = None
        # canvas.create_rectangle(x1, y1, x2, y2, fill='#222222')
        player_bio_Object.append(canvas.create_text((x1 + x2) / 2, y2 + const, fill=player.colour, font="Times 25 bold", text=player.name))
        player_bio_Object.append(canvas.create_text((x1 + x2) / 2, y2 + const * 2, fill="#ffffff", font="Times 15",
                           text='Bank_Balance:' + str(player.bank_balance)))
        player_bio_Object.append(canvas.create_text((x1 + x2) / 2, y2 + const * 3, fill="#ffffff", font="Times 15",
                           text='total_prop:' + str(player.total_prop)))
        # canvas.create_text((x1 + x2 )/ 2, y2 + const*3, fill="#ffffff", font="Times 15", text= 'Cash:' + player.cash)
        string = ""
        line = y2 + const * 4
        for i in range(len(player.ListOfPropertied)):

            if i % 2 != 1 and i != len(player.ListOfPropertied) - 1:
                string = string + player.ListOfPropertied[i].name + '  '
                continue
            string = string + player.ListOfPropertied[i].name + '  '
            player_bio_Object.append(canvas.create_text((x1 + x2) / 2, line, fill="#ffffff", font="Times 15",
                               text=string))
            line = line + const
            string = ''
        x1 = x2 + k1 / 4
        x2 = x1 + k1 * 2 + k1 / 3
    pass


def draw_players():
    list_Of_Players.reverse()
    List = list_Of_Players
    list_Of_Players.reverse()
    for p in List:
        if p.bankkrupt:
            continue
        box_no = p.houseNo
        h = p.id
        # print(h)
        colour = p.colour


        x1, y1, x2, y2 = box[box_no].coordinates

        x1 += k1 // 10 + k1 * h // 10
        x2 = x1 + k1 // 10

        y2 -= k1 // 10
        y1 = y2 - k1 // 10

        imagefile = 'player/small/player' + colour[1:] + ".png"
        pic = Image.open(imagefile)
        pic = ImageTk.PhotoImage(pic)
        # canvas.create_image(x1, y1, anchor=NW, image=pic)
        p.player_imz = pic
        if p.object == None:
            canvas.create_image(x1, y1 - 30, anchor=NW, image=pic)
            # p.object = canvas.create_oval(x1, y1, x2, y2, fill=colour)
            # print(p.object, '**')
        else:
            # canvas.delete(p.object)
            # canvas.create_image(x1, y1 - 30, anchor=NW, image=pic)
            # p.object = canvas.create_oval(x1, y1, x2, y2, fill=colour)
            # p.object.move
            p.object.config(x=x1, y=y1)
    canvas.update()


def update_map():
    for b in box:
        x1, y1, x2, y2 = b.coordinates
        if b.oner_rectangle:
            canvas.delete(b.oner_rectangle)
            b.oner_rectangle = None
        if b.oner:
            b.oner_rectangle = canvas.create_rectangle(x1, y1, x1 + 25, y1 + 10, fill=b.oner.colour)


    draw_players()

    draw_player_bio()

    canvas.update()

def mainloop(event):
    global chance_of_player, txt
    p = list_Of_Players[chance_of_player]
    chance_of_player += 1
    chance_of_player = chance_of_player%6
    if p.chanceToBeMissed > 0:
        p.chanceToBeMissed -= 1
        return
    if p.bankkrupt:
        return
    dice_no1, dice_no2 = roleTheDice()
    dice_no = dice_no1 + dice_no2
    newBox = p.houseNo + dice_no
    if newBox >= totalBox:
        p.bank_balance += SALARY
        p.bank_balance -= p.tax_C
        newBox = newBox % totalBox
        while p.houseNo != newBox:
            p.houseNo += 1
            p.houseNo = p.houseNo % totalBox
            draw_players()
            canvas.update()
            time.sleep(.1)
    else:
        while p.houseNo < newBox:
            p.houseNo += 1
            draw_players()
            canvas.update()
            time.sleep(.1)

    p.houseNo = newBox
    Action = box[newBox].update(p, dice_no)
    print(Action)
    if txt:
        canvas.delete(txt)
        txt = None
    txt = canvas.create_text(w / 2, h/2 - SIZE_OF_DICEimg / 2
                             , fill="#f0f0f0", font="Times 15",
                       text=Action)
    time.sleep(.5)
    update_map()


def satup():
    create_map()
    for b in box:
        coordinate_of_box.append(b.coordinates)
    root.bind('<Motion>', mouse_pointer)
    root.bind('<Button-1>', mainloop)
    players()
    draw_map()


if __name__ == '__main__':
    # draw(root)
    satup()
    # while True:
    #     mainloop(None)
    #     time.sleep(1)
    # for i in range(25):
    #     roleTheDice()
    #     time.sleep(1)
    root.mainloop()
# draw_dice()

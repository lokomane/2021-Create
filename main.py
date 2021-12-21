#import Turtles
import turtle as trtl
import random as rand
wn = trtl.Screen()
#setup
wn.setup(width=1.0, height=1.0)
wn.bgpic("Continent.gif")
font_setup = ("Arial", 15, "bold")
title_font = ("Arial"), 40, "normal"
shape = "square"
size = .5
color = "goldenrod"
button_color = "slateblue"
done_color = "green"
africa_click = 0
na_click = 0
sa_click = 0
asia_click = 0
ant_click = 0
aus_click = 0
eu_click = 0
#List of turtles/continents
#Create continents functions
sg = trtl.Turtle()
africa = trtl.Turtle()
na = trtl.Turtle()
sa = trtl.Turtle()
asia = trtl.Turtle()
eu = trtl.Turtle()
aus = trtl.Turtle()
ant = trtl.Turtle()
#go back turtles
gb = trtl.Turtle()
#set speed for other turtles
africa.speed(0)
na.speed(0)
sa.speed(0)
asia.speed(0)
eu.speed(0)
aus.speed(0)
ant.speed(0)
gb.speed(0)
#hide Turtles
africa.hideturtle()
na.hideturtle()
sa.hideturtle()
asia.hideturtle()
eu.hideturtle()
aus.hideturtle()
ant.hideturtle()
gb.hideturtle()
# Pen up for ease and future use
africa.penup()
na.penup()
sa.penup()
asia.penup()
eu.penup()
aus.penup()
ant.penup()
#set shape for turtles
africa.shape(shape)
na.shape(shape)
sa.shape(shape)
asia.shape(shape)
eu.shape(shape)
aus.shape(shape)
ant.shape(shape)
gb.shape(shape)
sg.shape("turtle")
#Set size for turtles
africa.shapesize(size)
na.shapesize(size)
sa.shapesize(size)
asia.shapesize(size)
eu.shapesize(size)
aus.shapesize(size)
ant.shapesize(size)
gb.shapesize(size)
#Set color for turtle
africa.fillcolor(color)
na.fillcolor(color)
sa.fillcolor(color)
asia.fillcolor(color)
eu.fillcolor(color)
aus.fillcolor(color)
ant.fillcolor(color)
location_list = [35,75,150,150,15,175,275,10,355,150,0,175,250,60]
def create_con():
#Thes statements represet the color of object
    global location_list
    delete = location_list.pop(0)
    africa.goto(-location_list[0], location_list[1])
    africa.write("Africa", font=font_setup)
    location_list.append(delete)
    location_list.append(delete)
    asia.goto(location_list[0], location_list[1])
    asia.write("Asia", font=font_setup)
    eu.goto(-location_list[0], location_list[1])
    eu.write("Europe", font=font_setup)
    sa.goto(-location_list[0], location_list[1])
    sa.write("South America", font=font_setup)
    na.goto(-location_list[0], location_list[1])
    na.write("North America", font=font_setup)
    ant.goto(location_list[0], -location_list[1])
    ant.write("Antarctica", font=font_setup)
    aus.goto(location_list[0], -location_list[1])
    aus.write("Australia", font=font_setup)
    if africa_click > 0:
        africa.fillcolor(done_color)
        africa.showturtle()
    else:
        africa.fillcolor(color)
        africa.showturtle()
    if na_click > 0:
        na.fillcolor(done_color)
        na.showturtle()
    else:
        na.fillcolor(color)
        na.showturtle()
    if sa_click > 0:
        sa.fillcolor(done_color)
        sa.showturtle()
    else:
        sa.fillcolor(color)
        sa.showturtle()
    if eu_click > 0:
        eu.fillcolor(done_color)
        eu.showturtle()
    else:
        eu.showturtle()
        eu.fillcolor(color)
    if ant_click > 0:
        ant.fillcolor(done_color)
        ant.showturtle()
    else:
        ant.fillcolor(color)
        ant.showturtle()
    if asia_click > 0:
        asia.fillcolor(done_color)
        asia.showturtle()
    else:
        asia.fillcolor(color)
        asia.showturtle()
    if aus_click > 0:
        aus.fillcolor(done_color)
        aus.showturtle()
    else:
        aus.fillcolor(color)
        aus.showturtle()
def hide_con():
    africa.hideturtle()
    na.hideturtle()
    sa.hideturtle()
    asia.hideturtle()
    eu.hideturtle()
    aus.hideturtle()
    ant.hideturtle()
    #clear turtles
    africa.clear()
    na.clear()
    sa.clear()
    asia.clear()
    eu.clear()
    aus.clear()
    ant.clear()

def go_back(x,y):
    gb.clear()
    gb.hideturtle()
    hide_con()

    create_con()


#Create lists of random facts
AfricaFacts = ["Africa is the second largest continent on earth!",
               "Between 1500 and 2000 languages are spoken!",
               "Africa has the longest the largest river, The Nile!",
               "Africa has the worlds largest desert, the Sahara!",
               "Africa has the oldest relics of human Civilization!"]
NAFacts = ["North America is third largest Continent!","North America was named after the explorer, Americo Vespucci!","North America is the only Continent that has every type of climate!","Lake Superior is the largest body of freshwater in the world!","The island of Greenland is the largest island in the world!"]
SAFacts = ["South America is the fourth Largest country in the world!", "The country Brazil takes up half of the continents land mass!", "South America hold 40% of the world plants in less then 15% of earth's land space!","The Andes mountain range is the longest mountain range in the world!", "The Atacama Desert is the world driest non polar desert!"]
AUSFACTS = ["Australia is the smallest Continent!","Tasmania has the cleanest air in the world!","The Great Barrier Reef is the largest eco-system in the world!","Australia is known as a island Continent!","The sheep population in Australia is higher then the Human population!"]
EUFacts = ["Europe is the sixth Largest Continent!","There are no deserts in europe!","Europe is a large peninsula made up of small peninsulas!","Every country is no more than 300 miles away from sea!","The Vatican City is the smallest country in the world!"]
ASIAFacts = ["Asia is the largest continent on earth!","Asia has 30% of the worlds land and 60% of worlds population!","Asia is home to the 10 highest mountains in the world!","Asia is home tot he largest country, Russia!","Asia also has the lowest point on earth, the Dead Sea!"]
ANTFacts = ["Antarctica holds most of the world's fresh water!","Antarctica is a polar desert!","There’s a subglacial lake that flows blood red!","Antarctica is fifth largest Continent!","More than 10 countries have research stations in Antarctica!"]
#Box points
#(350,275),(-450,275),(-450,-250),(350,275)
#Set location of continent turtles and print names

#start Game function
sg.speed(0)
sg.fillcolor("aquamarine")
sg.begin_fill()
sg.penup()
sg.goto(350,275)
sg.pendown()
sg.goto(-450,275)
sg.goto(-450,-250)
sg.goto(350,-250)
sg.goto(350,275)
sg.end_fill()
sg.penup()
#start game text
sg.goto(-250,200)
sg.write("Continent Learner",font= title_font)
sg.goto(-375,150)
sg.write("Welcome to the Continent Guesser!",font= font_setup)
sg.goto(-375,100)
sg.write("In this Program you will learn about the different continents", font=font_setup)
sg.goto(-375,50)
sg.write("Instructions: Click on square beneath each continent to learn facts about it",font = font_setup)
sg.goto(-375,0)
sg.write("Then click the go back button in the left corner to go back to the map!", font = font_setup)
sg.goto(-375,-50)
#creating the fact screen
def africa_box(x,y):
    global AfricaFacts, africa_click
    fact = rand.choice(AfricaFacts)
    hide_con()
    #go back turtle
    africa.showturtle()
    africa.fillcolor(color)
    africa.begin_fill()
    africa.goto(350, 275)
    africa.pendown()
    africa.goto(-450, 275)
    africa.goto(-450, -250)
    africa.goto(350, -250)
    africa.goto(350, 275)
    africa.end_fill()
    africa.fillcolor(button_color)
    africa.penup()
    africa.goto(-100,200)
    africa.write("Africa", font = title_font)
    africa.goto(-200,150)
    africa.write("Population:1,385,809,393", font = font_setup)
    africa.goto(-200,100)
    africa.write("Size:11.73 million mi²", font = font_setup)
    africa.goto(-275,50)
    africa.write(fact, font = font_setup)
    africa.goto(100,-235)
    africa.write("Click me for a new fact!", font = font_setup)
    gb.fillcolor(button_color)
    gb.showturtle()
    gb.penup()
    gb.goto(-435,-235)
    gb.write("Click me to go Back!", font = font_setup)
    africa_click += 1
def na_box(x,y):
    global NAFacts, na_click
    fact = rand.choice(NAFacts)
    hide_con()
    na.showturtle()
    na.fillcolor(color)
    na.begin_fill()
    na.goto(350, 275)
    na.pendown()
    na.goto(-450, 275)
    na.goto(-450, -250)
    na.goto(350, -250)
    na.goto(350, 275)
    na.end_fill()
    na.fillcolor(button_color)
    na.penup()
    na.goto(-200, 200)
    na.write("North America", font=title_font)
    na.goto(-200,150)
    na.write("Population:596,591,172", font=font_setup)
    na.goto(-200,100)
    na.write("Size:9.54 million mi²", font=font_setup)
    na.goto(-275,50)
    na.write(fact, font=font_setup)
    na.goto(100,-235)
    na.write("Click me for a new fact!", font = font_setup)
    gb.fillcolor(button_color)
    gb.showturtle()
    gb.penup()
    gb.goto(-435,-235)
    gb.write("Click me to go Back!", font = font_setup)
    na_click  += 1
def ant_box(x,y):
    global ANTFacts, ant_click
    fact = rand.choice(ANTFacts)
    hide_con()
    ant.showturtle()
    ant.fillcolor(color)
    ant.begin_fill()
    ant.goto(350, 275)
    ant.pendown()
    ant.goto(-450, 275)
    ant.goto(-450, -250)
    ant.goto(350, -250)
    ant.goto(350, 275)
    ant.end_fill()
    ant.fillcolor(button_color)
    ant.penup()
    ant.goto(-150, 200)
    ant.write("Antarctica", font=title_font)
    ant.goto(-200,150)
    ant.write("Population:1,000-5,000", font=font_setup)
    ant.goto(-200,100)
    ant.write("Size:5.483 million mi²", font=font_setup)
    ant.goto(-275,50)
    ant.write(fact, font=font_setup)
    ant.goto(100,-235)
    ant.write("Click me for a new fact!", font = font_setup)
    gb.fillcolor(button_color)
    gb.showturtle()
    gb.penup()
    gb.goto(-435,-235)
    gb.write("Click me to go Back!", font = font_setup)
    ant_click += 1
def aus_box(x, y):
    global AUSFACTS, aus_click
    fact = rand.choice(AUSFACTS)
    hide_con()
    aus.showturtle()
    aus.fillcolor(color)
    aus.begin_fill()
    aus.goto(350, 275)
    aus.pendown()
    aus.goto(-450, 275)
    aus.goto(-450, -250)
    aus.goto(350, -250)
    aus.goto(350, 275)
    aus.end_fill()
    aus.fillcolor(button_color)
    aus.penup()
    aus.goto(-140, 200)
    aus.write("Australia", font=title_font)
    aus.goto(-200,150)
    aus.write("Population:25,704,340", font=font_setup)
    aus.goto(-200,100)
    aus.write("Size:2.97 million mi²", font=font_setup)
    aus.goto(-325,50)
    aus.write(fact, font=font_setup)
    aus.goto(100,-235)
    aus.write("Click me for a new fact!", font=font_setup)
    gb.fillcolor(button_color)
    gb.showturtle()
    gb.penup()
    gb.goto(-435,-235)
    gb.write("Click me to go Back!", font = font_setup)
    aus_click += 1
def eu_box(x, y):
    global EUFacts, eu_click
    fact = rand.choice(EUFacts)
    hide_con()
    eu.showturtle()
    eu.fillcolor(color)
    eu.begin_fill()
    eu.goto(350, 275)
    eu.pendown()
    eu.goto(-450, 275)
    eu.goto(-450, -250)
    eu.goto(350, -250)
    eu.goto(350, 275)
    eu.end_fill()
    eu.fillcolor(button_color)
    eu.penup()
    eu.goto(-125, 200)
    eu.write("Europe", font=title_font)
    eu.goto(-200,150)
    eu.write("Population:748,285,180", font=font_setup)
    eu.goto(-200,100)
    eu.write("Size:3.93 million mi²", font=font_setup)
    eu.goto(-275,50)
    eu.write(fact, font=font_setup)
    eu.goto(100,-235)
    eu.write("Click me for a new fact!", font = font_setup)
    gb.fillcolor(button_color)
    gb.showturtle()
    gb.penup()
    gb.goto(-435,-235)
    gb.write("Click me to go Back!", font = font_setup)
    eu_click += 1
def asia_box(x, y):
    global ASIAFacts, asia_click
    fact = rand.choice(ASIAFacts)
    hide_con()
    asia.showturtle()
    asia.fillcolor(color)
    asia.begin_fill()
    asia.goto(350, 275)
    asia.pendown()
    asia.goto(-450, 275)
    asia.goto(-450, -250)
    asia.goto(350, -250)
    asia.goto(350, 275)
    asia.end_fill()
    asia.fillcolor(button_color)
    asia.penup()
    asia.goto(-125, 200)
    asia.write("Asia", font=title_font)
    asia.goto(-200,150)
    asia.write("Population:4,697,395,383", font=font_setup)
    asia.goto(-200,100)
    asia.write("Size:17.21 million mi²", font=font_setup)
    asia.goto(-275,50)
    asia.write(fact, font=font_setup)
    asia.goto(100,-235)
    asia.write("Click me for a new fact!", font = font_setup)
    gb.fillcolor(button_color)
    gb.showturtle()
    gb.penup()
    gb.goto(-435,-235)
    gb.write("Click me to go Back!", font = font_setup)
    asia_click += 1
def sa_box(x, y):
    global SAFacts, sa_click
    fact = rand.choice(SAFacts)
    hide_con()
    sa.showturtle()
    sa.fillcolor(color)
    sa.begin_fill()
    sa.goto(350, 275)
    sa.pendown()
    sa.goto(-450, 275)
    sa.goto(-450, -250)
    sa.goto(350, -250)
    sa.goto(350, 275)
    sa.end_fill()
    sa.fillcolor(button_color)
    sa.penup()
    sa.goto(-200, 200)
    sa.write("South America", font=title_font)
    sa.goto(-200,150)
    sa.write("Population:430,759,766", font=font_setup)
    sa.goto(-200,100)
    sa.write("Size:6.888 million mi²", font=font_setup)
    sa.goto(-275,50)
    sa.write(fact, font=font_setup)
    sa.goto(100,-235)
    sa.write("Click me for a new fact!", font=font_setup)
    gb.fillcolor(button_color)
    gb.showturtle()
    gb.penup()
    gb.goto(-435,-235)
    gb.write("Click me to go Back!", font = font_setup)
    sa_click += 1
#Hiding game start
def start_game(x,y):
    sg.clear()
    sg.hideturtle()
    create_con()


sg.goto(-200,-175)
sg.write("Click me to Begin!",font = font_setup)
sg.turtlesize(10)
sg.fillcolor(button_color)
sg.goto(-350,-125)
sg.onclick(start_game)

africa.onclick(africa_box)
na.onclick(na_box)
sa.onclick(sa_box)
eu.onclick(eu_box)
asia.onclick(asia_box)
aus.onclick(aus_box)
ant.onclick(ant_box)
gb.onclick(go_back)


wn.mainloop()
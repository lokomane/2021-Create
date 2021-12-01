#import Turtles
import turtle as trtl
wn = trtl.Screen()
#setup
wn.setup(width=1.0, height=1.0)
wn.bgpic("Continent.gif")
font_setup = ("Arial", 15, "bold")
title_font = ("Arial"), 40, "normal"
shape = "square"
size = .5
color =  "goldenrod"
#List of turtles/continents
#Create continents functions
africa = trtl.Turtle()
na = trtl.Turtle()
sa = trtl.Turtle()
asia = trtl.Turtle()
eu = trtl.Turtle()
aus = trtl.Turtle()
ant = trtl.Turtle()
#set speed for other turtles
africa.speed(0)
na.speed(0)
sa.speed(0)
asia.speed(0)
eu.speed(0)
aus.speed(0)
ant.speed(0)
#hide Turtles
africa.hideturtle()
na.hideturtle()
sa.hideturtle()
asia.hideturtle()
eu.hideturtle()
aus.hideturtle()
ant.hideturtle()
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
#Set size for turtles
africa.shapesize(size)
na.shapesize(size)
sa.shapesize(size)
asia.shapesize(size)
eu.shapesize(size)
aus.shapesize(size)
ant.shapesize(size)
#Set color for turtle
africa.fillcolor(color)
na.fillcolor(color)
sa.fillcolor(color)
asia.fillcolor(color)
eu.fillcolor(color)
aus.fillcolor(color)
ant.fillcolor(color)
def create_con():
    africa.showturtle()
    na.showturtle()
    sa.showturtle()
    asia.showturtle()
    eu.showturtle()
    aus.showturtle()
    ant.showturtle()
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
sg = trtl.Turtle()
#Create lists of random facts
AfricaFacts = ["Africa is the second largest continent on earth!", "Between 1500 and 2000 languages are spoken!", "Africa has the longest the largest river, The Nile!", "Africa has the worlds largest desert, the Sahara!", "Africa has the oldest relics of human Civilization!"]
NAFacts = ["North America is third largest Continent!","North America was named after the explorer, Americo Vespucci!","North America is the only Continent that has every type of climate!","Lake Superior is the largest body of freshwater in the world!","The island of Greenland is the largest island in the world!"]
SAFacts = ["South America is the fourth Largest country in the world!", "The country Brazil takes up half of the continents land mass!", "South America hold 40% of the world plants in less then 15% of earth's land space!","The Andes moutnain range is the longest mountain range in the world!", "The Atacama Desert is the world driest non polar desert!"]
#Box points
#(350,275),(-450,275),(-450,-250),(350,275)
#Set location of continent turtles and print names
def name_con():
    africa.goto(-35,75)
    africa.write("Africa",font= font_setup)
    asia.goto(150,150)
    asia.write("Asia",font= font_setup)
    eu.goto(-15,175)
    eu.write("Europe",font= font_setup)
    sa.goto(-275,10)
    sa.write("South America",font= font_setup)
    na.goto(-355,150)
    na.write("North America",font= font_setup)
    ant.goto(0,-175)
    ant.write("Antarctica",font= font_setup)
    aus.goto(250,-60)
    aus.write("Australia",font= font_setup)
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
sg.goto(-350,200)
sg.write("Continent Learner",font= title_font)
sg.goto(-350,150)
sg.write("Welcome to the Continent Guesser!",font= font_setup)
sg.goto(-350,100)
sg.write("In this Program you will learn about the different continents", font=font_setup)
sg.goto(-350,50)
sg.write("Instructions: Click on triangle beneath each continent to learn facts about it",font = font_setup)
sg.goto(-350,0)
sg.write("Then click go back in the left corner to go back to the map!", font = font_setup)
sg.goto(-350,-50)
#creating the fact screen
def africa_box(x,y):
    hide_con()
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
    africa.penup()
    africa.goto(-125,200)
    africa.write("Africa", font = title_font)
    africa.goto(-100,175)
    africa.write("Population:1,385,809,393", font = font_setup)
    africa.goto(-50,150)
    africa.write("Size:11.73 million mi²", font = font_setup)
def na_box(x,y):
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
    na.penup()

def ant_box(x,y):
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
    ant.penup()
def aus_box(x, y):
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
    aus.penup()
def eu_box(x, y):
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
    eu.penup()
def asia_box(x, y):
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
    asia.penup()
def sa_box(x, y):
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
    sa.penup()
#Hiding game start
def start_game(x,y):
    sg.clear()
    sg.hideturtle()
    create_con()
    name_con()
sg.turtlesize(10)
sg.fillcolor("red")
sg.goto(-300,-300)
sg.onclick(start_game)

africa.onclick(africa_box)
na.onclick(na_box)
sa.onclick(sa_box)
eu.onclick(eu_box)
asia.onclick(asia_box)
aus.onclick(aus_box)
ant.onclick(ant_box)

















wn.mainloop()
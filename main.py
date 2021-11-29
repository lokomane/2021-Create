#import Turtles
import turtle as trtl
wn = trtl.Screen()
#setup
wn.setup(width=1.0, height=1.0)
wn.bgpic("Continent.gif")
font_setup = ("Arial", 15, "bold")
title_font = ("Arial"), 40, "normal"
#List of turtles/continents
#Create continents functions
africa = trtl.Turtle()
na = trtl.Turtle()
sa = trtl.Turtle()
asia = trtl.Turtle()
eu = trtl.Turtle()
aus = trtl.Turtle()
ant = trtl.Turtle()
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


def create_con():
    africa.showturtle()
    na.showturtle()
    sa.showturtle()
    asia.showturtle()
    eu.showturtle()
    aus.showturtle()
    ant.showturtle()

sg = trtl.Turtle()
#Box points
#(350,275),(-450,275),(-450,-250),(350,275)
#Set location of continent turtles and print names
africa.goto(-50,100)
africa.write("Africa",font= title_font)
asia.goto(150,150)
asia.write("Asia",font= title_font)
eu.goto(-15,175)
eu.write("Europe",font= title_font)
sa.goto(-275,20)
sa.write("South America",font= title_font)
na.goto(-325,150)
na.write("North America",font= title_font)
ant.goto(0,-125)
ant.write("",font= title_font)
aus.goto(250,-60)
aus.write("",font= title_font)
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

#Hiding game start
def start_game(x,y):
    sg.clear()
    sg.hideturtle()
    create_con()
sg.turtlesize(10)
sg.fillcolor("red")
sg.goto(-300,-300)
sg.onclick(start_game)


















wn.mainloop()
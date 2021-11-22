#import Turtles
import turtle as trtl
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("Continent.gif")
#List of turtles/continents
africa =  trtl.Turtle()
'''
NA =  trtl.Turtle()
SA =  trtl.Turtle()
asia =  trtl.Turtle()
EU =  trtl.Turtle()
AUS =  trtl.Turtle()
Antartica =  trtl.Turtle()
'''
#Box points
#(350,275),(-450,275),(-450,-250)
#start Game function
sg = trtl.Turtle()
africa.goto(350,275)
africa.penup()
africa.goto(-450,275)
africa.goto(-450,-250)
africa.goto(350,-250)
africa.goto(350,275)















wn.mainloop()
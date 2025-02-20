import turtle as t
import math
import datetime

#aken
aken=t.Screen()
aken.setup(500,500)
aken.title("Kell")

#ring
kell=t.Turtle()
kell.width(4)
#väike ring keskel
kell.circle(4)
#suurem ring
kell.penup()
kell.goto(0,-200)
kell.pendown()
kell.circle(200)

# numbrid
kell.penup()
kell.hideturtle()  # peidame kilpkonna, et see ei segaks numbreid

# Tsükli abil lisame iga numbri õigesse asukohta
for i in range(1, 13):
    angle = math.radians(30 * i)  # iga number on 30 kraadi kaugusel eelmisest (360 kraadi / 12 numbrit)
    x = 150 * math.sin(angle)     # x-positsioon 150 ühiku kaugusel keskpunktist
    y = 150 * math.cos(angle) - 10  # y-positsioon ja kohandatud -10, et asetus oleks parem
    
    kell.goto(x, y)
    kell.write(str(i), align="center", font=("Verdana", 12, "normal")) 


# Osutite loomine
tund = t.Turtle()
minut = t.Turtle()

# Osutite omadused
for osuti in (tund, minut):
    osuti.shape("arrow")
    osuti.shapesize(stretch_wid=0.15, stretch_len=9) # Osuti kitsaks ja pikaks
    osuti.speed(0)
    osuti.penup()
    
# Osutite värvid
tund.color("black")
minut.color("blue")

# Funktsioon osutite uuendamiseks
def uuenda_kell():
    # Saame praeguse aja
    aeg = datetime.datetime.now()
    tund1 = aeg.hour % 12
    minut1 = aeg.minute
    
    # Arvutame iga osuti nurga vastavalt ajale
    tund_nurk = 30 * (tund1 + minut1 / 60)
    minut_nurk = 6 * minut1
    
    # Asetame osutid õigesse asendisse
    tund.setheading(90 - tund_nurk)
    minut.setheading(90 - minut_nurk)
    
    # Uuendame kella iga 30 sekundi järel
    aken.ontimer(uuenda_kell, 30000)


# Käivitame kella uuendamise
uuenda_kell()

aken.exitonclick()

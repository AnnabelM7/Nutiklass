import turtle
from turtle import  *
import time
from random import *

#Loome rohelise akna
aken=turtle.Screen()
aken.setup(800,500)
aken.bgcolor("green")
aken.title("Turtle race")

#Loome pealkirja
penup() # Tõstame pliiatsi üles, et joonistada ilma jälgi jätmata
goto(-100, 205)
color("White")
write("TURTLE RACE", font=("Arial", 20, "bold"))

#Pruun ala (võistlusala)
goto(-350,190)
pendown() # Langetame pliiatsi, et alustada joonistamist
color("#b07634") #Hex caode
begin_fill() #Täidame värviga
for i in range(2): #Pruun ristkülik
    forward(700)
    right(90)
    forward(350)
    right(90)
end_fill() # Täidame joonistatud ala

#Finiš must joon
goto(290,190) # Liigume finišijoone asukohta
pendown()
color("black") 
begin_fill() #Täidame värviga
for i in range(2):
    right(90)
    forward(350)
    right(90)
    forward(40)
end_fill()

#Finiš 
gap_size = 22.2
shape("square") # Määrame kujundi kuju (ruut)
penup() # Et ei jääks pliiatsi joont
color("white")
#Esimene rida
for i in range(8):
    goto(260, (180 - (i * gap_size * 2)))
    stamp() # Joonistame märgi
#Teine rida
for i in range(8):
    goto(280, (160 - (i * gap_size * 2)))
    stamp()


# Kilpkonnade loomine tsükliga
kilpkonnad = [] # Loome tühja loendi kilpkonnade jaoks
varvid = ["cyan", "yellow", "blue", "red", "purple"]  # Kilpkonnade värvid
algpositsioon = 120  # Esimese kilpkonna Y-koordinaat

# Loome kilpkonnad ja paigutame need üksteise alla
for i in range(len(varvid)):
    kilpkonn = Turtle() # Loome uue kilpkonna
    kilpkonn.color(varvid[i])
    kilpkonn.shape("turtle")
    kilpkonn.shapesize(1.5)
    kilpkonn.penup() # Tõstame pliiatsi üles, et mitte jälgi jätta
    kilpkonn.goto(-300, algpositsioon - (i * 50))  # Paigutame kilpkonnad üksteise alla
    kilpkonn.pendown()
    kilpkonnad.append(kilpkonn)  # Lisame kilpkonna loendisse
    
    
# Loome uue kilpkonna loenduse jaoks
loendur = Turtle()
loendur.penup()
loendur.goto(0, -220)
loendur.color("white")
loendur.hideturtle() # Et ei oleks valget noolt

# 3...2...1... Läks!
for i in range(3, 0, -1):
    loendur.write(i, align="center", font=("Arial", 40, "bold"))
    time.sleep(1)  # 1-sekundiline paus
    loendur.clear()  # Kustutame ainult loenduse, mitte tausta

# Kuvame "Läks!"
loendur.write("START!", align="center", font=("Arial", 40, "bold"))
time.sleep(1)  # 1-sekundiline paus enne kilpkonnade liikumist
loendur.clear()  # Kustutame "START!"

#Finiš
finišijoon = 280 # Finišijoone asukoht

voitja_leitud = False  # Lisasime bool-muutuja

while not voitja_leitud:  # Jätkame seni, kuni võitja on leitud
    for kilp in kilpkonnad:  # Itereerime läbi kilpkonnade
        edasi=randint(1, 15)
        if kilp.xcor() < finišijoon:  # Kontrollime, kas kilpkonn on finišijoone lähedal
            kilp.forward(randint(1, 15))  # Liigutame kilpkonna edasi juhusliku sammuga
        else:
            voitja = kilp.pencolor()  # Salvestame võitja värvi
            voitja_leitud = True  # Määrame, et võitja on leitud
            break  # Katkestame sisemise tsükli
        
# Kuvame võitja
loendur.goto(0, -220)
loendur.write(str(voitja) + " võitis!", align="center", font=("Arial", 30, "bold"))


turtle.exitonclick()# Ootame hiireklõpsu enne akna sulgemist
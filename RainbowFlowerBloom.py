import turtle as tur
tur.bgcolor("black")
tur.speed(0)
tur.hideturtle()

colors = ['yellow','red','yellow','red']

for i in range(120):
    for c in colors:
        tur.color(c)
        tur.circle(200-i, 100)
        tur.lt(90)
        tur.circle(200-i, 100)
        tur.rt(60)
        tur.end_fill()

tur.mainloop()
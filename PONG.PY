import turtle
import playsound

#Ventana
wn = turtle.Screen()
wn.title("STALINGRADO PONG By Fatima")
#wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.bgpic("bg2.gif")
wn.update()
wn.tracer(0)
wn.register_shape('stalin2.gif')
wn.register_shape('hitler2.gif')
wn.register_shape('skull3.gif')

#Marcador
marcadorA = 0
marcadorB = 0

#JugadorA
jugadorA = turtle.Turtle()
jugadorA.speed(0)
#jugadorA.shape("square")
jugadorA.shape('stalin2.gif')
#jugadorA.color("pink")
jugadorA.penup()
jugadorA.goto(-350, 0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1)

#Jugadorb
jugadorB = turtle.Turtle()
jugadorB.speed(0)
#jugadorB.shape("square")
jugadorB.shape('hitler2.gif')
#jugadorB.color("pink")
jugadorB.penup()
jugadorB.goto(350, 0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1)


#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
#pelota.shape("square")
#pelota.color("black")
pelota.shape('skull3.gif')
pelota.penup()
pelota.goto(0,0)
pelota.dx = 3
pelota.dy = 3

division=turtle.Turtle()
division.color("black")
division.goto(0,400)
division.goto(0,-400)

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(": 0              0 : " ,align= "center", font =("Courier",15, "bold" )  )


#funciones
def jugadorA_up():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)    


#Teclado
wn.listen()
wn.onkeypress(jugadorA_up , "w" )
wn.onkeypress(jugadorA_down , "s")
wn.onkeypress(jugadorB_up , "Up" )
wn.onkeypress(jugadorB_down , "Down")


while True:
    wn.update()
    
    pelota.setx(pelota.xcor() + pelota.dx / 10)
    pelota.sety(pelota.ycor() + pelota.dy / 10)


    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1    

    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA +=1
        pen.clear()
        pen.write(": {}             {}  : ".format(marcadorA,marcadorB) ,align= "center", font =("Courier",15, "bold") )
        playsound.playsound('CALAS.mp3',True)
        

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write(": {}              {} : ".format(marcadorA,marcadorB) ,align= "center", font =("Courier",15, "bold") )
        playsound.playsound('nameadolf.mp3',True)

    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and (pelota.ycor() < jugadorB.ycor() + 50
            and pelota.ycor() > jugadorB.ycor() -50)):
            pelota.dx *= -1
            

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and (pelota.ycor() < jugadorA.ycor() + 50
            and pelota.ycor() > jugadorA.ycor() -50)):
            pelota.dx *= -1
            
             
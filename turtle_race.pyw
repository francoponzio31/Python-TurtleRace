import turtle
from random import randint
from time import sleep

# ------------------- Configuracion de la ventana:

pantalla = turtle.Screen()
pantalla.title("__TURTLE RACE__")
pantalla.bgcolor("#066409")
pantalla.setup(width = 700, height = 550)
pantalla.tracer(0)

# ------------------- Dibujo del campo y tablero:

campo_y_tablero = turtle.Turtle(visible=False)
campo_y_tablero.color("white")
campo_y_tablero.pensize(4)
campo_y_tablero.penup()
campo_y_tablero.goto(-370,190); campo_y_tablero.pendown(); campo_y_tablero.goto(370,190); campo_y_tablero.penup()
campo_y_tablero.goto(-370,-250); campo_y_tablero.pendown(); campo_y_tablero.goto(370,-250); campo_y_tablero.penup()
campo_y_tablero.goto(260,-250); campo_y_tablero.pendown(); campo_y_tablero.goto(260,190); campo_y_tablero.penup()
campo_y_tablero.goto(-250,-250); campo_y_tablero.pendown(); campo_y_tablero.goto(-250,190); campo_y_tablero.penup()
campo_y_tablero.goto(293,-120); campo_y_tablero.write("G\nO\nA\nL", font = ("Courier",32,"normal"))
campo_y_tablero.goto(-310,-110); campo_y_tablero.write("S\nT\nA\nR\nT", font = ("Courier",22,"normal"))
campo_y_tablero.goto(-340,243); campo_y_tablero.write("WIN COUNTER:", font = ("Arial",16,"normal"))

circulo_azul = turtle.Turtle(shape="circle")
circulo_azul.color("blue")
circulo_azul.penup()
circulo_azul.goto(-270,220)
circulo_rojo = turtle.Turtle(shape="circle")
circulo_rojo.color("red")
circulo_rojo.penup()
circulo_rojo.goto(-90,220)
circulo_naranja = turtle.Turtle(shape="circle")
circulo_naranja.color("#f39700")
circulo_naranja.penup()
circulo_naranja.goto(87,220)
circulo_violeta = turtle.Turtle(shape="circle")
circulo_violeta.color("purple")
circulo_violeta.penup()
circulo_violeta.goto(264,220)

victorias_azul, victorias_rojo, victorias_naranja, victorias_violeta = 0, 0, 0, 0

texto_counter = turtle.Turtle(visible=False)
texto_counter.color("white")
texto_counter.penup()
texto_counter.goto(-340,208)
texto_counter.write(f"\t: {victorias_azul}\t\t : {victorias_rojo}\t\t : {victorias_naranja}\t\t : {victorias_violeta}", font = ("Arial",14,"normal"))


# --------------------------------- Tortugas:

tortuga_azul = turtle.Turtle(shape="turtle")
tortuga_azul.color("blue")
tortuga_azul.color_string = "BLUE"
tortuga_azul.penup()
tortuga_azul.shapesize(2,2,2)

tortuga_roja = turtle.Turtle(shape="turtle")
tortuga_roja.color("red")
tortuga_roja.color_string = "RED"
tortuga_roja.penup()
tortuga_roja.shapesize(2,2,2)

tortuga_naranja = turtle.Turtle(shape="turtle",)
tortuga_naranja.color("#f39700")
tortuga_naranja.color_string = "ORANGE"
tortuga_naranja.penup()
tortuga_naranja.shapesize(2,2,2)

tortuga_violeta = turtle.Turtle(shape="turtle")
tortuga_violeta.color("purple")
tortuga_violeta.color_string = "PURPLE"
tortuga_violeta.penup()
tortuga_violeta.shapesize(2,2,2)

# ---------------------------------- mainloop:

# Bucle de juego:
while True:

    # Seteo las coordenadas de partida de las tortugas:
    tortuga_azul.goto(-250,130)
    tortuga_roja.goto(-250,25)
    tortuga_naranja.goto(-250,-83)
    tortuga_violeta.goto(-250,-190)


    # Bucle de partida:
    while True:
        
        # Desplazamiento tortugas:
        tortuga_naranja.forward(randint(1,8))
        tortuga_violeta.forward(randint(1,8)) 
        tortuga_azul.forward(randint(1,8))
        tortuga_roja.forward(randint(1,8)) 
        pantalla.update()
        sleep(0.1)
        
        # Victoria de alguna de las tortugas:
        if tortuga_naranja.xcor()>280 or tortuga_violeta.xcor()>280 or tortuga_azul.xcor()>280 or tortuga_roja.xcor()>280:

            # Determinacion del ganador:
            coordenada_x_mayor = 0
            empate = False
            for tortuga in (tortuga_azul, tortuga_naranja, tortuga_roja, tortuga_violeta):

                if tortuga.xcor() == coordenada_x_mayor:
                    empate = True

                elif tortuga.xcor() > coordenada_x_mayor:
                    coordenada_x_mayor = tortuga.xcor()
                    ganador = tortuga.color_string
                    empate = False

            if empate:                    
                # Mensaje empate:            
                texto_empate = turtle.Turtle(visible=False)
                texto_empate.color("black")
                texto_empate.penup()
                texto_empate.write("DRAW !!!", align = "center", font = ("Arial",24,"normal")) 
                pantalla.update()
                sleep(4)
                texto_empate.clear()
                break               
               
            else:
                # Mensaje ganador:
                texto_ganador = turtle.Turtle(visible=False)
                texto_ganador.color(ganador)
                texto_ganador.penup()
                texto_ganador.write(f"{ganador} WINS !!!", align = "center", font = ("Arial",24,"normal"))
                pantalla.update()
                sleep(4)
                texto_ganador.clear()
                
                # Suma contador victorias:
                if ganador == "BLUE":
                    victorias_azul += 1
                elif ganador == "RED":
                    victorias_rojo += 1
                elif ganador == "ORANGE":
                    victorias_naranja += 1
                elif ganador == "PURPLE":
                    victorias_violeta += 1         

                texto_counter.clear()
                texto_counter.write(f"\t: {victorias_azul}\t\t : {victorias_rojo}\t\t : {victorias_naranja}\t\t : {victorias_violeta}", font = ("Arial",14,"normal"))       

                break
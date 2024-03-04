import turtle
import tkinter

def get_category(wind_speed):
    if wind_speed >= 157:
        return 5, "red"
    elif wind_speed >= 130:
        return 4, "orange"
    elif wind_speed >= 111:
        return 3, "yellow"
    elif wind_speed >= 96:
        return 2, "green"
    elif wind_speed >= 74:
        return 1, "blue"
    else:
        return 0, "white"

def draw_hurricane_path(file_path):
    turtle.speed(0)  
    turtle.penup()

    with open(file_path, 'r', encoding='utf-8') as file:
        next(file) 

        for line in file:
            values = line.strip().split(',')

            lat = float(values[2])  
            lon = float(values[3])  
            wind_speed = float(values[4])  
            category, color = get_category(wind_speed)

            turtle.pencolor(color)  
            turtle.pensize(category * 2) 
            turtle.goto(lon, lat)
            turtle.pendown()

            turtle.update()  
            turtle.delay(10)  

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    turtle.setup(965, 600) 

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45) 

    map_bg_img = tkinter.PhotoImage(file="hurricanetracker/StarterFiles/images/atlantic-basin.png")


    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("hurricanetracker/StarterFiles/images/hurricane.gif")
    t.shape("hurricanetracker/StarterFiles/images/hurricane.gif")

    return (t, wn, map_bg_img)

def irma():
    """Animates the path of hurricane Irma"""
    (t, wn, map_bg_img) = irma_setup()
    draw_hurricane_path("hurricanetracker/StarterFiles/data/irma.csv")
    turtle.done()

if __name__ == "__main__":
    irma()

import turtle

# Функция для рисования круга с заданными цветом и радиусом
def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Настройка окна turtle
turtle.bgcolor("white")
turtle.speed(25)

# Голова Деда Мороза
draw_circle("red", 100, 0, -100)

# Лицо
draw_circle("peachpuff", 70, 0, -70)

# Глаза
draw_circle("white", 15, -25, 0)
draw_circle("white", 15, 25, 0)
draw_circle("black", 7, -25, 5)
draw_circle("black", 7, 25, 5)

#шеки
draw_circle("darksalmon", 10, -30, -30)
draw_circle("darksalmon", 10, 30, -30)

#тело
draw_circle("red", 115, 0, -300)
draw_circle("black", 7, 0, -150)
draw_circle("black", 7, 0, -175)
draw_circle("black", 7, 0, -200)

# Нос
draw_circle("red", 10, 0, -30)

# Борода
draw_circle("white", 25, 0, -85)


#пояс
turtle.pensize(20)           # Установка толщины линии
turtle.color("saddlebrown")    # Установка цвета линии
turtle.penup()           # Подъем пера
turtle.goto(-100,-225 )     # Переход к начальной точке
turtle.pendown()         # Опускание пера
turtle.forward(200)     # Рисование линии
turtle.penup()


turtle.hideturtle()
turtle.done()
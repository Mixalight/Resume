'''
Программа рисует правильные многоугольники разных цветов и размеров по нажатию
ЛКМ на холст. Количество граней - n. Радиус многоугольника - r. Необходимо
создать холст, указать все нужные числа и после этого можно "рисовать"
'''
from tkinter import*
import random
from tkinter.messagebox import*
from math import sin, cos, pi

root = Tk()
canva = Tk()
root.geometry("+745+0")
canva.geometry("+0+0")
n = 0
m = 0
cvs = Canvas(root, width = 0, height = 0, bg = "white")

root.title("Полигоны")
canva.title("Холст")

lab1 = Label(root, text = "Введите размеры холста", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
lab2 = Label(root, text = "Введите R", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
lab3 = Label(root, text = "Введите N", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
txt1 = Entry(root, font = "Ubuntu, 20")
txt2 = Entry(root, font = "Ubuntu, 20")
tn = Entry(root, font = "Ubuntu, 20")
tm = Entry(root, font = "Ubuntu, 20")
tn.insert(END, 600)
tm.insert(END, 600)
txt1.insert(END, 40)
txt2.insert(END, 6)

def f1():                                               #Создание холста                                                 
    global m, n, cvs, canva
    m = tm.get()
    n = tn.get()
    try:
        n = int(n)
        m = int(m)
        cvs.grid_forget()
        canva.config(height = m, width = n)
        cvs = Canvas(canva, width = n, height = m, bg = "white")
        cvs.grid(row = 6, column = 0, columnspan = 2)
        cvs.bind("<Button-1>", f3)
    except: showwarning("Error", "Введите натуральные числа") 

    
def f2():                                               #Очистка холста
    cvs.delete("all")
    

def f3(event):                                          #Отрисовка многоугольников
    global cvs, canva
    points = []
    x0 = event.x
    y0 = event.y
    r = random.randint(0, 255)      
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    cl = "#{:02x}{:02x}{:02x}".format(r, g, b) 
    R = int(txt1.get())
    N = int(txt2.get())
    #print(R + N)
    a = 2 * pi / N
    for i in range(N):
        x = x0 + R * cos(a * i)
        y = y0 - R * sin(a * i)
        points.append([x, y])
        #print(x, y)
    spoke = cvs.create_polygon(points, fill = cl, outline = cl)
 
B1 = Button(root, text = "Создать холст", width = "25", command = f1)
B2 = Button(root, text = "Очистить холст",  width = "25", command = f2)
lab1.grid(row = 0, column = 0, columnspan = 2)
tn.grid(row = 1, column = 0)
tm.grid(row = 1, column = 1)
B1.grid(row = 2, columnspan = 2)
lab2.grid(row = 3, column = 0)
lab3.grid(row = 3, column = 1)
txt1.grid(row = 4, column = 0)
txt2.grid(row = 4, column = 1)
B2.grid(row = 5, column = 0, columnspan = 2)

#cvs.bind("<Button-1>", f3)

root.mainloop()
'''
Программа строит график введённой функции. Необходимо ввести диапозоны
координат по осям х и y в соответсвующие поля. Затем ввести функцию, создать
холст и можно строить график.
'''
from tkinter import*
from math import sin, cos, pi
from tkinter.messagebox import*

root = Tk()
canva = Tk()
root.geometry("+0+0")
canva.geometry("-0+0")
n = m = 0
f = ""
cvs = Canvas(canva, width = 0, height = 0)

root.title("Меню")
canva.title("Холст")
lab1 = Label(root, text = "Введите размеры холста", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
lab2 = Label(root, text = "Введите xmin", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
lab3 = Label(root, text = "Введите xmax", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
lab4 = Label(root, text = "Введите ymin", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
lab5 = Label(root, text = "Введите ymax", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
txt2 = Entry(root, font = "Ubunty, 20")
txt3 = Entry(root, font = "Ubunty, 20")
txt4 = Entry(root, font = "Ubunty, 20")
txt5 = Entry(root, font = "Ubunty, 20")
tn = Entry(root, font = "Ubuntu, 20")
tm = Entry(root, font = "Ubuntu, 20")
txty = Entry(root, font = "Ubunty, 20")
tn.insert(END, 600)
tm.insert(END, 600)
txt2.insert(END, -10)
txt3.insert(END, 10)
txt4.insert(END, -10)
txt5.insert(END, 10)

def f1():                                           #Создание холста
    global m, n, cvs, canva
    m = tm.get()
    n = tn.get()
    try:
        n = int(n)
        m = int(m)
        cvs.grid_forget()
        canva.config(height = m, width = n)
        cvs = Canvas(canva, width = n, height = m, bg = "white")
        cvs.grid(row = 0, column = 0, columnspan = 2, rowspan = 2)
    except: showwarning("Error", "Введите натуральные числа")
    
def f2():                                           #Очистка холста
    cvs.delete("all")
    
def f3():                                           #Функция отрисовки
    global mx, my, y0, x0, x, y, f
    f = txty.get()
    xmin, xmax, ymin, ymax =  txt2.get(), txt3.get(), txt4.get(), txt5.get()
    try:
        xmin, xmax, ymin, ymax = int(xmin), int(xmax), int(ymin), int(ymax)
        h = int(cvs["height"])      
        w = int(cvs["width"])

        mx = w / (xmax - xmin) 
        my = h / (ymax - ymin)

        x0, y0 = -xmin * mx, ymax * my
        #x0, y0 = F(x0, y0)
        cvs.create_line(0, y0, w, y0, fill = "green")
        for x in range(xmin + 1, xmax):
            i = x0 + x * mx
            cvs.create_line(i, y0 - 2, i, y0 + 2, fill = "green")
            cvs.create_text(i + 2, y0 + 10, text = str(x), font = "Verdana 12", anchor = "w", fill = "black")
            
        cvs.create_line(x0, 0, x0, h, fill = "green")
        for y in range(ymin + 1, ymax):
            i = y0 - y * my
            cvs.create_line(x0 - 2, i, x0 + 2, i, fill = "green")
            if str(y) != '0':
                cvs.create_text(x0 + 10, i + 2, text = y, font = "Verdana 12", anchor = "w", fill = "black")

        x = xmin
        dx = 0.01
        while x < xmax:
            y = eval(f)
            x1 = x0 + x * mx
            y1 = y0 - y * my
            cvs.create_oval(x1, y1, x1, y1, fill = "red")
            x += dx
    except: showwarning("Error", "Введите целые числа и функцию")

def f4():                                               #Завершение программы
    root.destroy()
    canva.destroy()

B1 = Button(root, text = "Создать холст", width = "25", command = f1)
B2 = Button(root, text = "Очистить холст", width = "25", command = f2)
B3 = Button(root, text = "Нарисовать график", width = "25", command = f3)
B4 = Button(root, text = "Выход", width = "25", command = f4)


lab1.grid(row = 0, column = 0, columnspan = 2)
tn.grid(row = 1, column = 0)
tm.grid(row = 1, column = 1)
lab2.grid(row = 2, column = 0)
txt2.grid(row = 2, column = 1)
lab3.grid(row = 3, column = 0)
txt3.grid(row = 3, column = 1)
lab4.grid(row = 4, column = 0)
txt4.grid(row = 4, column = 1)
lab5.grid(row = 5, column = 0)
txt5.grid(row = 5, column = 1)
txty.grid(row = 6, column = 0, columnspan = 2)
B1.grid(row = 7, column = 0, columnspan = 2)
B2.grid(row = 8, column = 0, columnspan = 2)
B3.grid(row = 9, column = 0, columnspan = 2)
B4.grid(row = 10, column = 0, columnspan = 2)
root.mainloop()
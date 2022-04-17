'''
Программа имтирует работу спирографа. Для её работы необходимо ввести
радиус круга, в котором(или вне которого, в случае внешнего спирогарфа) будет 
двигаться окружность, которая будет рисовать. Этот параметр - R
Также нужно ввести параметр r - радиус окружности, которая будет рисовать.
Затем необходимо ввести параметр d - расстояние от центра рисующей окружности
до точки, которая будет оставлять след. После этого нужно ввести скорость, выбрать
тип спирографа(нажав одну из кнопок) и создать сам холст. При необходимости 
процесс можно остановить и снова запустить. 
'''
from tkinter import*
from math import sin, cos, pi
from tkinter.messagebox import*

root = Tk()
canva = Tk()
root.geometry("+745+0")
canva.geometry("+0+0")
n = 0
m = 0
g = 0
a = 0
flag = 0
time = ""
cvs = Canvas(canva, width = 0, height = 0)

root.title("Меню")
canva.title("Холст")

lab1 = Label(root, text = "Введите размеры холста", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
lab2 = Label(root, text = "Введите R", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
lab3 = Label(root, text = "Введите r", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
lab4 = Label(root, text = "Введите скорость", font = "Ubunty, 20",
             bg = "black", fg = "yellow")
lab5 = Label(root, text = "Введите d", font ="Ubunty, 20",
             bg = "black", fg = "yellow")
labi = Label(root, text = "Тип", font = "Ubunty, 20",
             bg = "black", fg = "yellow")
txt1 = Entry(root, font = "Ubuntu, 20")
txt2 = Entry(root, font = "Ubuntu, 20")
txt3 = Entry(root, font = "Ubuntu, 20")
v = Entry(root, font = "Ubuntu, 20")
tn = Entry(root, font = "Ubuntu, 20")
tm = Entry(root, font = "Ubuntu, 20")
tn.insert(END, 600)
tm.insert(END, 600)
txt1.insert(END, 250)
def f1():                                   #Функция создания холста
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

def f2():                                   #Функция очистки холста
    root.after_cancel(time)
    cvs.delete("all")

def vs():                                   #Основная функция, рисование
    global a, time, spoke, da, x0, y0, g, flag
    x0 = int(cvs["width"]) // 2 
    y0 = int(cvs["height"]) // 2
    if flag == 1:
        xc = x0 + (R - r) * cos(a)
        yc = y0 - (R - r) * sin(a)

        xt1 = xc + d * cos(a - g)
        yt1 = yc - d * sin(a - g)

        a += da
        g = a * R/r

        xc = x0 + (R - r) * cos(a)
        yc = y0 - (R - r) * sin(a)

        xt2 = xc + d * cos(a - g)
        yt2 = yc - d * sin(a - g)

        spoke = cvs.create_line(xt1, yt1, xt2, yt2)
        time = root.after(10, vs)           #Повторный вызов функции
    if flag == -1:
        xc = x0 + (R + r) * cos(a)
        yc = y0 - (R + r) * sin(a)

        xt1 = xc + d * cos(a + g)
        yt1 = yc - d * sin(a + g)

        a += da
        g = a * R / r

        xc = x0 + (R + r) * cos(a)
        yc = y0 - (R + r) * sin(a)

        xt2 = xc + d * cos(a + g)
        yt2 = yc - d * sin(a + g)

        spoke = cvs.create_line(xt1, yt1, xt2, yt2)
        time = root.after(10, vs)           #Повторный вызов функции


def f3():                                   #Функция считывающая все значения с полей ввода
    global a, da, d, R, crcl, r, scrcl, x0, y0, g
    cvs.delete("all")
    #root.after_cancel(time)
    R = txt1.get()
    da = v.get()
    d = txt2.get()
    r = txt3.get()
    try:
        x0 = int(cvs["width"]) // 2
        y0 = int(cvs["height"]) // 2
        R = int(R)
        da = int(da)
        da = da * pi / 180
        d = int(d)
        r = int(r)
        crcl = cvs.create_oval(x0 - R, y0 - R, x0 + R, y0 + R)
        a = 0
        vs()
    except: showwarning("Ошибка", "Введите натуральные числа")
    
def f4():                                   #Остановка рисования
    root.after_cancel(time)
    
def f5():                                   #Продолжение рисования
    root.after_cancel(time)
    vs()
    
def f6():                                   #Завершение программы
    root.destroy()
    canva.destroy()

def f7():                                   #Эта и следующая функция - установка флага
    global flag                             #для разных режимов работы
    flag = -1
    labi["text"] = "Внешний"

def f8():
    global flag
    flag = 1
    labi["text"] = "Внутренний"


B1 = Button(root, text = "Создать холст", width = "25", command = f1)
B2 = Button(root, text = "Очистить холст",  width = "25", command = f2)
B3 = Button(root, text = "Старт", width = "25", command = f3)
B4 = Button(root, text = "Стоп", width = "25", command = f4)
B5 = Button(root, text = "Продолжить", width = "25", command = f5)
B6 = Button(root, text = "Выход", width = "25", command = f6)
B7 = Button(root, text = "Внешний", width = "25", command = f7)
B8 = Button(root, text = "Внутренний", width = "25", command = f8)

lab1.grid(row = 0, column = 0, columnspan = 2)
tn.grid(row = 1, column = 0)
tm.grid(row = 1, column = 1)
lab2.grid(row = 2, column = 0)
txt1.grid(row = 2, column = 1)
lab3.grid(row = 3, column = 0)
txt3.grid(row = 3, column = 1)
lab5.grid(row = 4, column = 0)
txt2.grid(row = 4, column = 1)
B1.grid(row = 10, column = 0, columnspan = 2)
B2.grid(row = 11, column = 0, columnspan = 2)
B3.grid(row = 7, column = 0)
B4.grid(row = 7, column = 1)
B5.grid(row = 8, column = 1)
B6.grid(row = 8, column = 0)
B7.grid(row = 6, column = 0)
B8.grid(row = 6, column = 1)
lab4.grid(row = 5, column = 0)
v.grid(row = 5, column = 1)
labi.grid(row = 9, column = 0, columnspan = 2)
root.mainloop()
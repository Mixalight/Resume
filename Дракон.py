'''
Программа рисует фрактал кривая дракона. Для её работы необходимо ввести размеры холста,
ввести длину одной линии фрактала(d) и его размерность(сколько раз повторять рисование, n)
Затем необходимо нажать ЛКМ по холсту, и программа построит кривую дракона.
'''
from tkinter import*
from math import sin, cos, pi
from tkinter.messagebox import*
root = Tk()
canva = Tk()
root.geometry("+745+0")
canva.geometry("+0+0")
x = y = m = n = a = i = t = x1 = y1 = 0
a = 0
s = "1"
l = r = ""
cvs = Canvas(canva, width = 0, height = 0)
root.title("Меню")
canva.title("Холст")

lab1 = Label(root, text = "Введите размеры холста", font = "Ubuntu, 20",
             bg = "black",
             fg = "yellow")
lab2 = Label(root, text = "Введите d", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
lab3 = Label(root, text = "Введите n", font = "Ubuntu, 20",
             bg = "black", fg = "yellow")
txt2 = Entry(root, font = "Ubuntu, 20")
txt3 = Entry(root, font = "Ubuntu, 20")
tn = Entry(root, font = "Ubuntu, 20")
tm = Entry(root, font = "Ubuntu, 20")
tn.insert(END, 700)
tm.insert(END, 700)

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
        cvs.grid(row = 0, column = 0)
        cvs.bind("<Button-1>", f4)
    except: showwarning("Error", "Введите натуральные числа")

def f2():                                               #Очистка холста
    cvs.delete("all")

def f3():                                               #Завершение программы
    root.destroy()
    canva.destroy()

def f4(event):                                          #Отрисовка фрактала
    global x, y, s, d, n, i, l, t, r, a, x1, y1, cvs
    x, y = event.x, event.y
    d = txt2.get()
    n = txt3.get()
    try:
        d, n = int(d), int(n)
        cvs.create_line(x, y, x + d, y, fill = "red")
        x = x + d
        s = "1"
        a = 0
        for i in range(2, n + 1):
            l = s
            t = len(s) // 2
            r = s[:t] + '0' + s[t+1:]
            s = l + '1' + r
        for i in s:
            if i == '1':
                a += pi/2
            else:
                a -= pi/2
            cvs.create_line(x, y, x + d * cos(a), y - d * sin(a), fill = "red")
            x = x + d * cos(a)
            y = y - d * sin(a)
    except: showwarning("Error", "Введите натуральные числа")

B1 = Button(root, text = "Создать холст", width = "25", command = f1)
B2 = Button(root, text = "Очистить холст",  width = "25", command = f2)
B3 = Button(root, text = "Выход", width = "25", command = f3)

lab1.grid(row = 0, column = 0, columnspan = 2)
tn.grid(row = 1, column = 0)
tm.grid(row = 1, column = 1)
lab2.grid(row = 2, column = 0)
lab3.grid(row = 2, column = 1)
txt2.grid(row = 3, column = 0)
txt3.grid(row = 3, column = 1)
B1.grid(row = 4, column = 0, columnspan = 2)
B2.grid(row = 5, column = 0, columnspan = 2)
B3.grid(row = 6, column = 0, columnspan = 2)

root.mainloop()
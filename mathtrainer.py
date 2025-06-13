from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
from random import *
from datetime import datetime

root = Tk()
root.withdraw()

name = askstring('Привіт! :)', 'Хто ти?')

root.deiconify()

a = b = 0
cw = ch = 450
imgs = ['cat.png', 'cat1.png', 'cat2.png']
img = 0

testing_time = 300 # секунд

n = str(datetime.now().isoformat(timespec='minutes')) + name + ".txt"
n = n.replace(':', '')
print(n)


def my_clock():
    global testing_time
    testing_time -= 1
    if testing_time > 0:
        root.after(1000, my_clock)
    else:
        root.withdraw()
        messagebox.showinfo('Фініш', 'Вітаю! Тестування закінчено')
        root.destroy()
        

def tofile(s):
    f = open(n, "a")
    f.write(s)
    f.close()


def kotiki(a, b):
    global img
    cnv.delete("all")
    
    sz = 45
    dx = (cw-b*sz)//2 if sz * b <= cw else 0
    dy = (ch-a*sz)//2 if sz * a <= ch else 0
    
    img = PhotoImage(file = choice(imgs))
    
    for r in range(a):
        for c in range(b):
            cnv.create_image(dx+c*(sz if sz * b <= cw else (cw // (b + 1))),
                             dy+r*(sz if sz * a <= ch else (ch // (a + 1))),
                             anchor = NW, image = img)


def show():
    global a, b
    r1 = reg_1.get()
    a = randint(r1, 9 if r1 <= 5 else r1 + 5)
    r2 = reg_2.get()
    b = randint(r2, 9 if r2 <= 5 else r2 + 5)

    s = str(a) + " · " + str(b) + " ="
    
    kotiki(a, b)
    lbl['text'] = s
    
    ans['fg'] = 'black'
    ans.delete(0, END)
    ans.focus()


def test(ev):
    w = ans.get()
    if w.isdigit():
        tofile('\n' + str(a) + "·" + str(b) + '=' + str(w))
        #print(a, "·", b, '=', w, end = ' ') # для протоколу
        if int(w) == a*b:
            ans['fg'] = 'green'
            tofile('\t:)')
            #print('\t:)') # для протоколу
            #messagebox.showinfo('Результат', 'Правильно :)')
            show()
        else:
            ans['fg'] = 'red'
            tofile('\t:(')
            #print('\t:(') # для протоколу
            messagebox.showinfo('Результат', 'Помилка :(')
            ans.delete(0, END)
            ans['fg'] = 'black'
    else:
        ans.delete(0, END)


lbl = Label(text = "*", font = "Arial, 80")
lbl.grid(row = 0, column = 1, padx = 5, pady = 5)

ans = Entry(font = "Arial, 80", width = 3)
ans.grid(row = 0, column = 2, padx = 5)

ans.bind('<Return>', test)

f = open(n, "w")
f.write(name)
f.close()

reg_1 = Scale(root, from_=1, to=9, length = ch)
reg_1.grid(row = 1, column = 0)

reg_2 = Scale(root, from_=1, to=9, length = ch)
reg_2.grid(row = 1, column = 3)

cnv = Canvas(width = cw, height = ch)
cnv.grid(row = 1, column = 1, columnspan = 2, padx = 5)

my_clock()
show()

root.mainloop()

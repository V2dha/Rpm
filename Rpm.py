
rpm = 1000
from tkinter import*
from tkinter import messagebox
root = Tk()
root.title('CAR')
root.geometry('400x300')
root.config(bg='white')

l1 = Label(root, text=rpm, font=30)
l1.pack()
l2 = Label(root, text='Speed', font=30)
l2.place(x=170, y=40)


def f():
    global rpm
    rpm = 1000


def accelerate():
    global rpm
    rpm += 100
    l1.config(text=rpm)
    if rpm > 1500:
            import winsound
            winsound.Beep(2000, 1000)
            messagebox.showinfo(title = 'Warning', message = 'warning RPM too high')


def brake():
    global rpm
    rpm -= 100
    l1.config(text=rpm)
    if rpm > 1500:
            import winsound
            winsound.Beep(2000, 1000)
            messagebox.showinfo(title='Warning', message='warning RPM too high')

Button(root, text = 'Accelerate', font = 20, command=accelerate).place(x=250, y=90)
Button(root, text = 'Brake', font =20, command=brake).place(x=50, y=90)
Label(root, text='Maximum speed 1500', font=10).place(x=90, y=140)

root.mainloop()
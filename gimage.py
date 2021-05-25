from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("G-Image")

# root.iconbitmap('/home/gaurav/Downloads/launchpad-icon.png')

my_img1= ImageTk.PhotoImage(Image.open("prof.png"))
my_img2= ImageTk.PhotoImage(Image.open("bike.png"))
my_img3= ImageTk.PhotoImage(Image.open("hell.png"))
my_img4= ImageTk.PhotoImage(Image.open("dshn.png"))
my_img5= ImageTk.PhotoImage(Image.open("ku.png"))
my_img6= ImageTk.PhotoImage(Image.open("kmp.png"))
my_img7= ImageTk.PhotoImage(Image.open("kist.png"))
my_img8= ImageTk.PhotoImage(Image.open("kanyam.png"))
my_img9= ImageTk.PhotoImage(Image.open("shr.png"))
my_img10= ImageTk.PhotoImage(Image.open("sano.png"))

image_list =[my_img1, my_img2, my_img3, my_img4, my_img5,
             my_img6, my_img7, my_img8, my_img9, my_img10]


my_label = Label(image= my_img1)
my_label.grid(row=0,column=0, columnspan=2)


def next(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label= Label(image=image_list[image_number-1])
    button_next= Button(root, text =">>", command=lambda: next(image_number+1))
    button_back  = Button(root, text="<<", command=lambda: next(image_number -1))

    if image_number == 10:
        button_next = Button(root, text=">>",state = DISABLED)
    if image_number == 1:
        button_back = Button(root, text="<<",state = DISABLED)

    my_label.grid(row=0, column=0, columnspan=2)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label= Label(image=image_list[image_number-1])
    button_next = Button(root, text =">>", command=lambda: next(image_number+1))
    button_back  = Button(root, text="<<", command=lambda: next(image_number -1))


button_back = Button(root, text="<<", command=back,state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_next = Button(root, text=">>", command=lambda: next(2))


button_back.grid(row=1,column=0)
button_exit.grid(row=1, column=1)
button_next.grid(row=1,column=2)

root.mainloop()
from tkinter import *
from PIL import ImageTk,Image

#Declaring background
root = Tk()
img = Image.open("background.png")
img2 = ImageTk.PhotoImage(img)
canvas = Canvas(root, width = 500, height = 500)
canvas.pack(fill="both", expand=TRUE)
canvas.create_image(0, 0, image = img2, anchor="nw")

#Initializing penguin
penguin = Image.open("idle/0.png")
penguin2 = ImageTk.PhotoImage(penguin)
sprite = canvas.create_image(10, 10, anchor=NW, image=penguin2)

#Arrays to store images for penguin sprites
idle = ["idle/0.png", "idle/1.png", "idle/2.png", "idle/3.png", "idle/4.png", 
        "idle/5.png", "idle/6.png", "idle/7.png", "idle/8.png", "idle/9.png", 
        "idle/10.png", "idle/11.png"]
walkN = ["walk_N/0.png", "walk_N/1.png", "walk_N/2.png", "walk_N/3.png"]
walkE = ["walk_E/0.png", "walk_E/1.png", "walk_E/2.png", "walk_E/3.png"]
walkS = ["walk_S/0.png", "walk_S/1.png", "walk_S/2.png", "walk_S/3.png"]
walkW = ["walk_W/0.png", "walk_W/1.png", "walk_W/2.png", "walk_W/3.png"]


def move():
    print("yay")


# Initializing the background image and the game window
root.geometry('{}x{}'.format(img2.width(), img2.height()))
root.title("Penguin Game")
ico = Image.open("idle/0.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.bind("<Key>", move)
root.mainloop()
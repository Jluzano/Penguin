from tkinter import *
from PIL import ImageTk,Image

#Declaring background
root = Tk()
img = Image.open("background.png")
img2 = ImageTk.PhotoImage(img)
canvas = Canvas(root)
canvas.pack(fill="both", expand=TRUE)
canvas.create_image(0, 0, image = img2, anchor="nw")

#Initializing penguin & position
posx = 0
posy = 0

#Arrays to store images for penguin sprites
idle = ["idle/0.png", "idle/1.png", "idle/2.png", "idle/3.png", "idle/4.png", 
        "idle/5.png", "idle/6.png", "idle/7.png", "idle/8.png", "idle/9.png", 
        "idle/10.png", "idle/11.png"]
walkN = ["walk_N/0.png", "walk_N/1.png", "walk_N/2.png", "walk_N/3.png"]
walkE = ["walk_E/0.png", "walk_E/1.png", "walk_E/2.png", "walk_E/3.png"]
walkS = ["walk_S/0.png", "walk_S/1.png", "walk_S/2.png", "walk_S/3.png"]
walkW = ["walk_W/0.png", "walk_W/1.png", "walk_W/2.png", "walk_W/3.png"]

#Array for idle animation
idle_list = []
#converting the idle array to PhotoImages
for image in idle:
    image_obj = Image.open(image)
    photo_obj = ImageTk.PhotoImage(image_obj)
    idle_list.append(photo_obj)

#Creating the Penguin class
class Penguin:
    def __init__(self, canvas, x, y, sprites):
        self.canvas = canvas
        self.sprites = sprites
        self.sprite_index = 0
        self.sprite = canvas.create_image(x, y, anchor='nw', image=sprites[0])
        self.isIdle = TRUE

    def update_sprite(self):
        if self.isIdle:
            self.sprite_index += 1
            self.sprite_index = self.sprite_index % len(idle)
            self.canvas.itemconfig(self.sprite, image=idle_list[self.sprite_index])
        else:
            self.sprite_index += 1
            self.sprite_index = self.sprite_index % len(self.sprites)
            self.canvas.itemconfig(self.sprite, image=self.sprites[self.sprite_index])

    def move(self, x, y, sprites):
        self.canvas.move(self.sprite, x, y)
        self.sprites = sprites
        self.update_sprite()
        self.isIdle = TRUE

def up(event):
    x = 0
    y = -20
    canvas.move(sprite, x, y)

def down(event):
    x = 0
    y = 20
    canvas.move(sprite, x, y)

def left(event):
    x = -20
    y = 0
    canvas.move(sprite, x, y)

def right(event):
    x = 20
    y = 0
    canvas.move(sprite, x, y)


# Initializing the background image and the game window
root.geometry('{}x{}'.format(img2.width(), img2.height()))
root.title("Penguin Game")
ico = Image.open("idle/0.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.mainloop()
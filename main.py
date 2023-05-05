from tkinter import *
from PIL import ImageTk,Image

#Declaring background image
root = Tk()
img = Image.open("background.png")
img2 = ImageTk.PhotoImage(img)
canvas = Canvas(root)
canvas.pack(fill="both", expand=TRUE)
canvas.create_image(0, 0, image = img2, anchor="nw")
check = FALSE

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
        #Creating penguin and placing it onto the canvas
        self.canvas = canvas
        self.sprites = sprites
        self.sprite_index = 0
        self.sprite = canvas.create_image(x, y, anchor='nw', image=sprites[0])
        self.isIdle = TRUE #Penguin is not moving by default
        #Initializing penguin & position
        self.posx = 0
        self.posy = 0
        self.speed = 20

    #Update the penguin's sprite depending on if it is moving or not
    def update_sprite(self):
        #If the penguin is not moving
        if self.isIdle:
            self.sprite_index += 1
            #This allows the sprite_index to loop back to the start
            self.sprite_index = self.sprite_index % len(idle)
            #This line changes the sprite of the penguin to the next frame
            self.canvas.itemconfig(self.sprite, image=idle_list[self.sprite_index])
        else:
            #If the penguin is moving
            self.sprite_index += 1
            self.sprite_index = self.sprite_index % len(self.sprites)
            self.canvas.itemconfig(self.sprite, image=self.sprites[self.sprite_index])

    #Function for actually moving the sprite across the screen
    #First, moves the sprite
    #Next, sets its own sprite to the sprite depending on the direction
    #Then, it updates the sprite to the next frame
    #Last, it sets isIdle to true
    def move(self, x, y, sprites):
        self.isIdle = FALSE
        self.canvas.move(self.sprite, x, y)
        self.sprites = sprites
        self.update_sprite()
        self.isIdle = TRUE

    #Checking if the penguin is moving or not
    def animate_idle(self):
        if self.isIdle:
            self.update_sprite()
        #Repeat this every half a second
        root.after(500, self.animate_idle)

#Declaring Penguin object at (0, 0)
penguin = Penguin(canvas, 0, 0, [ImageTk.PhotoImage(Image.open(image)) for image in idle])
penguin2 = Penguin(canvas, 1000, 420, [ImageTk.PhotoImage(Image.open(image)) for image in idle])

#Function to convert the arrays of images into PhotoImages
#Also to reduce lines of code since its used in all 4 movement functions
def loop(array, direction):
    for image in direction:
        image_obj = Image.open(image)
        photo_obj = ImageTk.PhotoImage(image_obj)
        array.append(photo_obj)

def up(event):
    #Temporary variable for location checking
    tempx = penguin.posx
    tempy = penguin.posy - penguin.speed
    #Array of new images
    image_list = []
    #Go through array of respective direction and add it to the new array
    loop(image_list, walkN)
    #
    if tempx >= 840 and tempx <= 1160 and tempy >= 320 and tempy <= 540:
        penguin.move(0, 0, image_list)
        print("help!")
    #Checking if the penguin is at the top of the screen
    elif tempy >= 0:
        #Moving the penguin
        penguin.move(0, -penguin.speed, image_list)
        penguin.posy = tempy
        #Displays the penguin's updated position
        print("x: " + str(penguin.posx) + "\ty: " + str(penguin.posy))
    #Idle animation plays
    penguin.isIdle = TRUE

def down(event):
    tempx = penguin.posx
    tempy = penguin.posy + penguin.speed
    image_list = []
    loop(image_list, walkS)
    #
    if tempx >= 840 and tempx <= 1160 and tempy >= 320 and tempy <= 540:
        penguin.move(0, 0, image_list)
        print("help!")
    #760 is the maximum that the penguin can go downwards
    elif tempy <= 760:
        penguin.move(0, penguin.speed, image_list)
        penguin.posy = tempy
        print("x: " + str(penguin.posx) + "\ty: " + str(penguin.posy))
    penguin.isIdle = TRUE

def left(event):
    tempx = penguin.posx - penguin.speed
    tempy = penguin.posy
    image_list = []
    loop(image_list, walkW)
    if tempx >= 840 and tempx <= 1160 and tempy >= 320 and tempy <= 540:
        penguin.move(0, 0, image_list)
        print("help!")
    elif tempx >= 0:
        penguin.move(-penguin.speed, 0, image_list)
        penguin.posx = tempx
        print("x: " + str(penguin.posx) + "\ty: " + str(penguin.posy))
    penguin.isIdle = TRUE

def right(event):
    tempx = penguin.posx + penguin.speed
    tempy = penguin.posy
    image_list = []
    loop(image_list, walkE)
    if tempx >= 880 and tempx <= 1160 and tempy >= 320 and tempy <= 540:
        penguin.move(0, 0, image_list)
        print("help!")
    elif tempx <= 1420:
        penguin.move(penguin.speed, 0, image_list)
        penguin.posx = tempx
        print("x: " + str(penguin.posx) + "\ty: " + str(penguin.posy))
    penguin.isIdle = TRUE

#Penguin starts out in the idle animation
penguin.animate_idle()
penguin2.animate_idle()

#Stretches the background to fit the window height + width
root.geometry('{}x{}'.format(img2.width(), img2.height()))
#Changes the name of the window
root.title("Penguin Game")
#These lines change the icon in the corner of the window
ico = Image.open("idle/0.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
#Binding keys to functions
root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.mainloop()
from tkinter import *
from PIL import ImageTk,Image
import json

# Initializing the background image
root = Tk()
img = Image.open("background.png")
img2 = ImageTk.PhotoImage(img)
canvas = Canvas(root, width = 500, height = 500)
canvas.pack(fill="both", expand=TRUE)
canvas.create_image(0, 0, image = img2, anchor="nw")
root.geometry('{}x{}'.format(img2.width(), img2.height()))
root.mainloop()
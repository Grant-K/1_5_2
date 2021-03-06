""" TkinterDraw.py demonstrates some methods of Tkinter.Canvas
Revision 10/29/2013 Copyright 2013 PLTW
"""
from Tkinter import *          #don't import like this except for Tkinter
root = Tk()                      #create main window

# Make and place a canvas widget for events and drawing
canvas = Canvas(root, height=700, width=600, relief=RAISED, bg='white')
canvas.grid() #Puts the canvas in the main Tk window

# Make four objects on the canvas
checkbox = canvas.create_rectangle(100, 300, 200, 400, dash=[1,4])
x = canvas.create_line(270, 460, 330, 530, 300, 495, 270, 530, 330, 460,fill='red', width=20)
check = canvas.create_line(100, 350, 150, 400, 215, 275, fill='red', width=20)
message = canvas.create_text(380, 350, text='Try this!', font=('Arial', -100))
myName = canvas.create_text(300, 60, text='Grant Klees', font=('Times New Roman', -115))
shadow = canvas.create_oval(100, 550, 500, 650, fill='#00ccff', outline='#888888')
canvas.tag_raise(myName, shadow)

# Make an array of objects on the canvas
circles=[]
for r in range(10, 60, 10):
    circles += [canvas.create_oval(300-r, 500-r, 300+r, 500+r, outline='red')]

# Make one more object on the canvas
canopy = canvas.create_arc(0, 150, 600, 750, start=30, extent=120, width=50, style=ARC, outline = '#00ccff')          
canvas.itemconfig(circles[0], fill = 'black', width = 5)
# Demonstrate changing a property of canvas' item.
canvas.itemconfig(circles[2], outline='black') # Change color
# Get a filename in the same directory as this program
import os.path
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'canopyIcon.jpg')
# Open the image file and convert to an ImageTk object
import PIL.Image, PIL.ImageTk
img = PIL.Image.open(filename) # create a PIL.Image from the jpg fil
tkimg = PIL.ImageTk.PhotoImage(img) # convert the PIL.Image to a PIL
# Add the ImageTk object to the canvas.
icon = canvas.create_image(150, 350, image = tkimg)
canvas.tag_raise(icon, check)
# Enter event loop. This displays the GUI and starts listening for events.
# The program ends when you close the window.
root.mainloop() 
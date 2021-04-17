from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk,ImageOps
from tkinter.filedialog import askopenfile
import time
from cv2 import VideoCapture,imshow
import cv2

# main window configuration
root = Tk()
root.geometry("880x660")
root.resizable(width=False,height=False)
root.configure(bg="ghost white")
 
# progress bar 
progress = ttk.Progressbar(root, orient = HORIZONTAL,length = 250, mode = 'determinate')
 
trigger = 0 # <-- This is a trigger that checks if file loaded or not.
 

img = Image.open("C:/Users/carnage/Desktop/image2.png") # <-- need to be changed
img = img.resize((400,400))

filename = ImageTk.PhotoImage(img)

canvas = Canvas(root,height=400,width=400)
canvas.image = filename  # <--- keep reference of your image
canvas.create_image(0,0,anchor='nw',image=filename)
canvas.place(x=25,y=60)



# <-- Heading goes here
lab = Label(text="",bg="ghost white")
lab.place(x=430,y=470)
labtop = Label(root,text="LS-DETECTOR",font=("Verdana",20),padx=350,pady=5,bg="snow",fg="black")
labtop.place(x=0,y=0)
img = Image.open("C:/Users/carnage/Desktop/download.png")
filename = ''
# function that uploads file and set the image to the canvas
def chljaa():
    global filename
    global trigger
    global lab
    global img
    file = askopenfile(mode='r',filetypes=[('png/jpg/jpeg files','*.*')])
    img = Image.open(file.name)
    img = img.resize((400,400))
    filename = ImageTk.PhotoImage(img)
    print(type(filename))
    lab.config(text="",bg="ghost white")
    canvas = Canvas(root,height=400,width=400)
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(0,0,anchor='nw',image=filename)
    canvas.place(x=25,y=60)
 
    trigger = 1
 
# heart of the code.
def kaamkrapna():
    global filename
    global lab
    global img
    #img = Image.open()
    im2 = ImageOps.grayscale(img)
    filename1 = ImageTk.PhotoImage(im2)
    canvas = Canvas(root,height=400,width=400)
    canvas.image = filename1  # <--- keep reference of your image
    canvas.create_image(0,0,anchor='nw',image=filename1)
 
    global trigger
 
    if trigger == 1:
        
        progress['value'] = 20
        root.update_idletasks()
        time.sleep(1)
 
        progress['value'] = 40
        root.update_idletasks()
        time.sleep(1)
 
        progress['value'] = 50
        root.update_idletasks()
        time.sleep(1)
 
        progress['value'] = 60
        root.update_idletasks()
        time.sleep(1)
 
        progress['value'] = 80
        root.update_idletasks()
        time.sleep(1)
        progress['value'] = 100
 
        root.update_idletasks()
        time.sleep(1)
        progress['value'] = 0
        canvas.place(x=430,y=60)
        
    else:
        lab.config(text="Image not inserted",font=("Verdana",10),fg="red",bg="ghost white")
            
# placing of progress bar
progress.place(x=310,y=530)
 
# Button 1 for uploading the image
btn = Button(root,text='Browse Image/Video',font=("Verdana",14),command=chljaa)
btn.place(x=200,y=580)
 
# Button 2 for analyzing the image 
b = Button(root,text='Analyze',font=("Verdana",14),command=kaamkrapna)
b.place(x=500,y=580)
 
mainloop()

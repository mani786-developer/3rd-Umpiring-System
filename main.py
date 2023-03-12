import tkinter       #  because we make a gui 
import cv2           # it used to capture video using Opencv to use it pip install opencv-python
import threading     # we import this because we not need any blockage in program
from functools import partial # takes both function and its parameter at same time
import imutils       #image library of OpenCV for rotation , resizing , inserting ...
import time          #we wll use time.sleep   ( just like decision pending )
import PIL.Image, PIL.ImageTk # PIL mean python image library  # to install pip install pillow

# imagetk is used to show the image in the kinterwindow 

# This is the width and height of our main screen
SET_WIDTH=580
SET_HEIGHT=400

stream = cv2.VideoCapture("p.mp4")

#For slowing the video
def play(speed):
    print(f"the speed is {speed}")
    
    # for playing the video in reverse
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    
    #for setting the video accordingly
    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width = SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor= tkinter.NW)

# for presenting decision 
def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("decisionpend.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    canvas.create_text(150,30, fill ="black" , font= "times 26 bold", text= "___   3rd Empire Decision Pending " )
    
    # 2. then wait for 1 second
    time.sleep(3)

    # 3. then display sponser image
    frame = cv2.cvtColor(cv2.imread("sponcer.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width = SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame, anchor= tkinter.NW)

    # 4. wait for 1.5 second     
    time.sleep(3)
    
    # 5. display out/notout image
    if decision == 'out':
        decisionI = "out.jpg"
    else:
        decisionI = "notout.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionI), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width = SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame, anchor= tkinter.NW)

# Function for giving OUT
def out():
    #we use thread to render image with different speed
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1 # Daemon is used to not block the main threads and continue
    thread.start()
    print("Player is out")

# Function for giving NOT OUT
def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")
    
    
#*/----This is the Start----/*
ump=tkinter.Tk()

# title of our GUI
ump.title("3rd Umpire Review")
ump.config(background="violet")

# welcome Image 
img_1 = cv2.cvtColor(cv2.imread("welcomee.jpg"),cv2.COLOR_BGR2RGB)

#we use canvas in place of geometry
canvas=tkinter.Canvas(ump,width=SET_WIDTH,height=SET_HEIGHT)

# to insert in GUI (Canvas)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img_1))

# Set image on Canvas
image_on_canvas = canvas.create_image(0,0, anchor = tkinter.NW, image = photo)

#pack canvas to show everythin gon GUI
canvas.pack()

# Buttons to control our Software

# for moving Back (Prev)
pFast = tkinter.Button(ump,text= "<<<<Previous (Fast)", width=82,bg="violet",command=partial(play,-25))
pFast.pack()

# for moving Forward (Next)
pSlow = tkinter.Button(ump,text= "<<Previous (Slow)", width=82,bg="violet",command=partial(play,-2))
pSlow.pack()

# for moving forward (Slow)
nSlow = tkinter.Button(ump, text="Next>> (Slow)", width=82,bg="violet",command=partial(play,+2))
nSlow.pack()

# for moving Forward (fast)
nFast = tkinter.Button(ump,text= "Next>>>> (Fast)", width=82,bg="violet",command=partial(play,+25))
nFast.pack()

#for Giving out
gOut = tkinter.Button(ump , text = "Give out" , width=82,bg="violet", command=partial(out,))
gOut.pack()

#for not out
gNout = tkinter.Button(ump, text  ="Give not out" , width =82,bg="violet", command=partial(not_out,))
gNout.pack()

# For Rating
rate = tkinter.Button(ump, text=">>Rate my coding<<", width = 82,bg="violet")
rate.pack()

# This is the End 
ump.mainloop()

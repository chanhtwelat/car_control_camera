import cv2
import numpy as np
from tkinter import *
from PIL import Image,ImageTk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# define motor pins
IN1 = 11  #GPIO Pin GPIO 7
IN2 = 17 #GPIO Pin GPIO 17
IN3 = 13 #GPIO Pin GPIO 27
IN4 = 15 #GPIO Pin GPIO 22

# Set up output
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)


def move_forward(): # robot move forward
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)
    print('move forward')

def move_back():    # robot move back
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 1)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 1)
    print('move back')
    
def move_right():  # robot move right
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 0)
    print('move right')

def move_left():   # robot move left
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)
    print('move left')

def stop(): # robot stop
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 0)
    print('Stop')

#set up GUI
root = Tk()
root.geometry("700x7")
root.configure(bg = "black")

# set up title
Label(root,text="Camera", font=("times new roman",30,"bold"),bg="black",fg="red").pack()

#camera frame
f1 = LabelFrame(root, bg="red")
f1.pack()
L1 = Label(f1, bg = "green")
L1.pack()


#Capture Video Frames
cap = cv2.VideoCapture(0)

# define button for robot control 

button_1 = Button (root,text="forward",font=("time new roman",10,"bold"),bg="black",fg="green",command=move_forward).pack()
button_2 = Button (root,text="back....",font=("time new roman",10,"bold"),bg="black",fg="green",command=move_back).pack()
button_3 = Button (root,text="right...",font=("time new roman",10,"bold"),bg="black",fg="green",command=move_right).pack()
button_4 = Button (root,text="left.....",font=("time new roman",10,"bold"),bg="black",fg="green",command=move_left).pack()
button_5 = Button (root,text="stop....",font=("time new roman",10, "bold"),bg="black",fg="green",command=stop).pack()


while True:
    frame = cap.read()[1]
    image = cv2.rotate(frame,cv2.cv2.ROTATE_180)
    img   = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(Image.fromarray(img))
    L1['image'] = photo
    root.update()
cap.releate()

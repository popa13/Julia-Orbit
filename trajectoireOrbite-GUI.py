import tkinter as tk
from tkinter import *
import time

import os
import sys

from PIL import Image, ImageDraw  # Module de gestion des images
from PIL import ImageTk
import numpy as np

import datetime as dt

# Donnes constantes
WIDTH, HEIGHT = 1000, 1000
Size_Image_WIDTH, Size_Image_HEIGHT = 450, 450
X_MIN, X_MAX = -2.0, 2.0
Y_MIN, Y_MAX = -2.0, 2.0
LENGTH_X = X_MAX - X_MIN
LENGTH_Y = Y_MAX - Y_MIN

NB_DIVISION = 8
LENGHT_DIVISION_X = (X_MAX - X_MIN)/NB_DIVISION
LENGTH_DIVISION_Y = (Y_MAX - Y_MIN)/NB_DIVISION

RESOL = 0.0001

zRealDep = 0.0
zImDep = 0.0
cx = 0.0
cy = 0.0
numberIter = 30

# Useful functions
def PointToPixel(x,y):
    return (int((WIDTH/LENGTH_X)* (x -X_MIN)), int((HEIGHT/LENGTH_Y)*(y-Y_MIN)))

def leftBottomCornerPixel(x,y):
    return (int((WIDTH/LENGTH_X)* (x -X_MIN)) - 3 , int((HEIGHT/LENGTH_Y)*(y-Y_MIN)) -3)

def rightTopCornerPixel(x,y):
    return (int((WIDTH/LENGTH_X)* (x -X_MIN)) + 3, int((HEIGHT/LENGTH_Y)*(y-Y_MIN)) + 3)

def fctQuatratiqueReal(x, y, cx, cy):
    return x*x - y*y + cx

def fctQuatratiqueIm(x, y, cx, cy):
    return 2*x*y + cy

def drawAxis():
    X = np.linspace(X_MIN, X_MAX, WIDTH)

    draw.line([PointToPixel(X_MIN, 0), PointToPixel(X_MAX, 0)], fill = (0,0, 0), width = 1)
    draw.line([PointToPixel(0, Y_MIN), PointToPixel(0, Y_MAX)], fill=(0,0, 0), width=1)

    for x in range(NB_DIVISION):
        draw.line([PointToPixel(X_MIN + x* LENGHT_DIVISION_X , -0.05), PointToPixel(X_MIN + x*LENGHT_DIVISION_X, 0.05)], fill = (0,0,0), width = 1)
    for x in range(NB_DIVISION*2):
        draw.line([PointToPixel(X_MIN + x* LENGHT_DIVISION_X /2, -0.025), PointToPixel(X_MIN + x*LENGHT_DIVISION_X / 2, 0.025)], fill = (0,0,0), width = 1)
    for x in range(NB_DIVISION*8):
        draw.line([PointToPixel(X_MIN + x* LENGHT_DIVISION_X /8, -0.0125), PointToPixel(X_MIN + x*LENGHT_DIVISION_X / 8, 0.0125)], fill = (0,0,0), width = 1)

    for y in range(NB_DIVISION):
        draw.line([PointToPixel(-0.05, Y_MIN + y* LENGTH_DIVISION_Y), PointToPixel(0.05, Y_MIN + y*LENGTH_DIVISION_Y)], fill = (0,0,0), width = 1)
    for y in range(NB_DIVISION*2):
        draw.line([PointToPixel(-0.025, Y_MIN + y* LENGTH_DIVISION_Y/2), PointToPixel(0.025, Y_MIN + y*LENGTH_DIVISION_Y/2)], fill = (0,0,0), width = 1)
    for y in range(NB_DIVISION*8):
        draw.line([PointToPixel(-0.0125, Y_MIN + y* LENGTH_DIVISION_Y/8), PointToPixel(0.0125, Y_MIN + y*LENGTH_DIVISION_Y/8)], fill = (0,0,0), width = 1)

## Get the real and imaginary parts of Z
def print_selectionReal(val):
    global zRealDep
    sReal_var.set(str(val))
    zRealDep = float(val)

def mod_selectionReal(event):
    try:
        sReal.set(float(sReal_var.get()))
    except:
        sReal.set(float(0))

def print_selectionImag(val):
    global zImDep
    sImag_var.set(str(val))
    zImDep = float(val)

def mod_selectionImag(event):
    try:
        sImag.set(float(sImag_var.get()))
    except:
        sImag.set(float(0))

## Get the real and imaginary parts of C
def print_selectionRealC(val):
    global cx
    sRealC_var.set(str(val))
    cx = float(val)

def mod_selectionRealC(event):
    try:
        sRealC.set(float(sRealC_var.get()))
    except:
        sRealC.set(float(0))

def print_selectionImagC(val):
    global cy
    sImagC_var.set(str(val))
    cy = float(val)

def mod_selectionImagC(event):
    try:
        sImagC.set(float(sImagC_var.get()))
    except:
        sImagC.set(float(0))

### Fonction pour générer l'orbite
def creer_image():
    global orbiteImage
    global orbiteImageCanvas
    global zRealDep, zImDep, cx, cy
    orbiteImage = Image.new('RGB', (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(orbiteImage)
    drawAxis()

    ## Use mod_selection functions to make sure we use the right numbers
    try:
        sRealC.set(float(sRealC_var.get()))
    except:
        sRealC.set(float(0))

    try:
        sImag.set(float(sImag_var.get()))
    except:
        sImag.set(float(0))

    try:
        sRealC.set(float(sRealC_var.get()))
    except:
        sRealC.set(float(0))

    try:
        sImagC.set(float(sImagC_var.get()))
    except:
        sImagC.set(float(0))

    ## Initializing the values for z and c 
    zRealDep = sReal.get()
    zImDep = sImag.get()
    cx = sRealC.get() 
    cy = sImagC.get()

    nbIterationRetrieved = numberIter

    # Créer autant de X et Y que de pixels dans l'image
    X = np.linspace(X_MIN, X_MAX, WIDTH)

    draw.line([PointToPixel(X_MIN, 0), PointToPixel(X_MAX, 0)], fill = (0,0, 0), width = 1)
    draw.line([PointToPixel(0, Y_MIN), PointToPixel(0, Y_MAX)], fill=(0,0, 0), width=1)

    for x in range(NB_DIVISION):
        draw.line([PointToPixel(X_MIN + x* LENGHT_DIVISION_X , -0.05), PointToPixel(X_MIN + x*LENGHT_DIVISION_X, 0.05)], fill = (0,0,0), width = 1)
    for x in range(NB_DIVISION*2):
        draw.line([PointToPixel(X_MIN + x* LENGHT_DIVISION_X /2, -0.025), PointToPixel(X_MIN + x*LENGHT_DIVISION_X / 2, 0.025)], fill = (0,0,0), width = 1)
    for x in range(NB_DIVISION*8):
        draw.line([PointToPixel(X_MIN + x* LENGHT_DIVISION_X /8, -0.0125), PointToPixel(X_MIN + x*LENGHT_DIVISION_X / 8, 0.0125)], fill = (0,0,0), width = 1)

    for y in range(NB_DIVISION):
        draw.line([PointToPixel(-0.05, Y_MIN + y* LENGTH_DIVISION_Y), PointToPixel(0.05, Y_MIN + y*LENGTH_DIVISION_Y)], fill = (0,0,0), width = 1)
    for y in range(NB_DIVISION*2):
        draw.line([PointToPixel(-0.025, Y_MIN + y* LENGTH_DIVISION_Y/2), PointToPixel(0.025, Y_MIN + y*LENGTH_DIVISION_Y/2)], fill = (0,0,0), width = 1)
    for y in range(NB_DIVISION*8):
        draw.line([PointToPixel(-0.0125, Y_MIN + y* LENGTH_DIVISION_Y/8), PointToPixel(0.0125, Y_MIN + y*LENGTH_DIVISION_Y/8)], fill = (0,0,0), width = 1)

    draw.ellipse([leftBottomCornerPixel(zRealDep, zImDep), rightTopCornerPixel(zRealDep, zImDep)],  outline = (0, 127, 0), fill=(0, 127, 0), width = 5)

    iteration = 1
    zReal = zRealDep
    zIm = zImDep
    iteration = 0

    print('Initialization')
    print(str(zReal) + ', ' + str(zIm))

    # Normal orbit
    while(iteration <= numberIter):
        #print("I'm here")
        previousReal = zReal
        previousIm = zIm
        zReal= fctQuatratiqueReal(previousReal, previousIm, cx, cy)
        zIm = fctQuatratiqueIm(previousReal, previousIm, cx, cy)
        print(str(zReal) + ', ' + str(zIm))
        # Draw the points and the lines
        if ((iteration >= numberIter - nbIterationRetrieved) and (zReal > X_MIN or zReal == X_MIN) and (zReal < X_MAX or zReal == X_MAX) and (zIm > Y_MIN or zIm == Y_MIN) and (zIm < Y_MAX or zIm == Y_MAX)):
            draw.ellipse([leftBottomCornerPixel(zReal, zIm), rightTopCornerPixel(zReal, zIm)], outline = (0, 127, 0), fill = (0, 127, 0), width = 5)
            draw.line([PointToPixel(previousReal, previousIm), PointToPixel(zReal, zIm)], fill = (255, 0, 0), width = 3)
            iteration+=1
        elif ((iteration < numberIter - 6) and (zReal > X_MIN or zReal == X_MIN) and (zReal < X_MAX or zReal == X_MAX) and (zIm > Y_MIN or zIm == Y_MIN) and (zIm < Y_MAX or zIm == Y_MAX)):
            iteration+=1
        else:
            break

    print('Normal Orbit')
    print('Number of Iterations : ' + str(iteration))
    print(str(zReal) + ', ' + str(zIm))

    # Cesaro orbit (including z in the means)
    cesaroMeansReal = zRealDep
    cesaroMeansImag = zImDep

    zReal = zRealDep
    zIm = zImDep

    iteration = 2

    previousReal = 0
    previousIm = 0

    while(iteration <= numberIter):
        previousReal = zReal
        previousIm = zIm
        zReal = fctQuatratiqueReal(previousReal, previousIm, cx, cy)
        zIm = fctQuatratiqueIm(previousReal, previousIm, cx, cy)

        ## Storing previous cesaroMeans and compute next Cesaro means
        previousCesaroMeansReal = cesaroMeansReal
        previousCesaroMeansIm = cesaroMeansImag
        cesaroMeansReal = cesaroMeansReal*(iteration - 1)/iteration + zReal/iteration
        cesaroMeansImag = cesaroMeansImag*(iteration - 1)/iteration + zIm/iteration
        # Drawing the points and the lines
        #print(str(cesaroMeansReal) + ", " + str(cesaroMeansImag))
        if ((iteration >= numberIter - nbIterationRetrieved) and (cesaroMeansReal > X_MIN or cesaroMeansReal == X_MIN) and (cesaroMeansReal < X_MAX or cesaroMeansReal == X_MAX)
            and (cesaroMeansImag > Y_MIN or cesaroMeansImag == Y_MIN) and (cesaroMeansImag < Y_MAX or cesaroMeansImag == Y_MAX)):
            draw.ellipse([leftBottomCornerPixel(cesaroMeansReal, cesaroMeansImag), rightTopCornerPixel(cesaroMeansReal, cesaroMeansImag)], outline = (127, 127, 0), fill = (0, 127, 0), width = 5)
            draw.line([PointToPixel(previousCesaroMeansReal, previousCesaroMeansIm), PointToPixel(cesaroMeansReal, cesaroMeansImag)], fill = (0,0, 255), width = 3)
            iteration+=1
        elif ((iteration < numberIter - nbIterationRetrieved) and (cesaroMeansReal > X_MIN or cesaroMeansReal == X_MIN) and (cesaroMeansReal < X_MAX or cesaroMeansReal == X_MAX)
            and (cesaroMeansImag > Y_MIN or cesaroMeansImag == Y_MIN) and (cesaroMeansImag < Y_MAX or cesaroMeansImag == Y_MAX)):
            iteration+=1
        else:
            break

    #print('Cesaro Orbit')
    #print('Number of Iterations : ' + str(iteration))
    #print(str(cesaroMeansReal) + ", " + str(cesaroMeansImag))

    orbiteImage = orbiteImage.rotate(180)
    orbiteImage = orbiteImage.transpose(Image.FLIP_LEFT_RIGHT)

    orbiteImageCanvas = ImageTk.PhotoImage(orbiteImage.resize((Size_Image_WIDTH, Size_Image_HEIGHT)))
    canvas.create_image(300,240, image=orbiteImageCanvas)

def save_Img():
    dateTime = dt.datetime.now()
    orbiteImage.save('TrajectoireOrbiteVSCesaro' + '-zRe' + str(zRealDep) + 'zIm' + str(zImDep) + dateTime.strftime('%Y-%m-%d_%H-%M-%S') + '.png', 'PNG')

def show_Img():
    orbiteImage.show()

## application graphique
window = tk.Tk()
window.title("Julia Orbites")

# Canvas
canvas = tk.Canvas(window, width = 600, height = 650)
canvas.grid(columnspan=3)
canvas.pack()

# Initialize the main image
orbiteImage = Image.new('RGB', (WIDTH, HEIGHT), "white")
draw = ImageDraw.Draw(orbiteImage)
drawAxis()

orbiteImageCanvas = ImageTk.PhotoImage(orbiteImage.resize((Size_Image_WIDTH, Size_Image_HEIGHT)))
canvas.create_image(300,240, image=orbiteImageCanvas)

# Sliders to choose the real and imaginary parts of the initial z complex number
sReal = tk.Scale(window, label='Z real part : ', from_=X_MIN, to=X_MAX, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, resolution=RESOL, command=print_selectionReal)
sReal.place(x = 75, y = Size_Image_HEIGHT + 28)
sReal_var = tk.StringVar()
sRealValLabel = tk.Entry(window, textvariable=sReal_var, width=7)
sRealValLabel.place(x = 216, y = Size_Image_HEIGHT + 27)
sReal_var.set("0.0000")
sRealValLabel.bind("<Return>", mod_selectionReal)

sImag = tk.Scale(window, label='Z imaginary part: ', from_=Y_MIN, to=Y_MAX, orient=tk.HORIZONTAL, length=225, showvalue=0, tickinterval=2, resolution=RESOL, command=print_selectionImag)
sImag.place(x = 300, y = Size_Image_HEIGHT + 28)
sImag_var = tk.StringVar()
sImagValLabel = tk.Entry(window, textvariable=sImag_var, width=7)
sImag_var.set("0.0000")
sImagValLabel.place(x= 466, y= Size_Image_HEIGHT + 27)
sImagValLabel.bind("<Return>", mod_selectionImag)

# Sliders to choose the real and imaginary parts of the initial c complex number
sRealC = tk.Scale(window, label='C real part : ', from_=X_MIN, to=X_MAX, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, resolution=RESOL, command=print_selectionRealC)
sRealC.place(x = 75, y = Size_Image_HEIGHT + 86)
sRealC_var = tk.StringVar()
sRealValLabelC = tk.Entry(window, textvariable = sRealC_var, width=7)
sRealC_var.set("0.0000")
sRealValLabelC.place(x = 216, y = Size_Image_HEIGHT + 85)
sRealValLabelC.bind("<Return>", mod_selectionRealC)

sImagC = tk.Scale(window, label='C imaginary part: ', from_=Y_MIN, to=Y_MAX, orient=tk.HORIZONTAL, length=225, showvalue=0, tickinterval=2, resolution=RESOL, command=print_selectionImagC)
sImagC.place(x = 300, y = Size_Image_HEIGHT + 86)
sImagC_var = tk.StringVar() 
sImagValLabelC = tk.Entry(window, textvariable=sImagC_var, width=7)
sImagC_var.set("0.0000")
sImagValLabelC.place(x= 466, y= Size_Image_HEIGHT + 85)
sImagValLabelC.bind("<Return>", mod_selectionImagC)

# Add button to Generate
generate_Text = tk.StringVar()
generateButton = tk.Button(window, textvariable = generate_Text, width = 20, command = lambda:creer_image())
generate_Text.set("Generate")
generateButton.place(x = 85, y = Size_Image_HEIGHT + 150)

save_Text = tk.StringVar()
saveButton = tk.Button(window, textvariable = save_Text, width = 20, command = lambda:save_Img())
save_Text.set("Save image")
saveButton.place(x= 320, y = Size_Image_HEIGHT + 150)

# Add menus
menu = tk.Menu(window)
window.config(menu = menu)

fileMenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Save image", command = save_Img)
fileMenu.add_command(label = "View image", command = show_Img)

if __name__ == "__main__":
    window.mainloop()

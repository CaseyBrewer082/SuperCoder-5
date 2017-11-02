#Imports
from Tkinter import *
import Tkinter
import tkMessageBox
import time
from random import randint


#colour lists for comparison
gameColours = []
playerColours = []

#global count
count = 1

#colour dictionary
coloursimg = {
	1: 'singlebutton r1.gif',
	2: 'singlebutton b1.gif',
	3: 'singlebutton o1.gif',
	4: 'singlebutton gr1.gif',
        5: 'singlebutton g1.gif',
        6: 'singlebutton p1.gif',
        7: 'singlebutton br1.gif',
	'singlebutton r1.gif': 'singlebutton r1.gif',
	'singlebutton b1.gif': 'singlebutton b1.gif',
	'singlebutton o1.gif': 'singlebutton o1.gif',
	'singlebutton gr1.gif': 'singlebutton gr1.gif',
        'singlebutton g1.gif': 'singlebutton g1.gif',
        'singlebutton p1.gif': 'singlebutton p1.gif',
        'singlebutton br1.gif': 'singlebutton br1.gif'
}

#original colours tied to flashed colours
originalcoloursimgdict = {
	'singlebutton r1.gif': 'singlebutton r2.gif',
	'singlebutton b1.gif': 'singlebutton b2.gif',
	'singlebutton o1.gif': 'singlebutton o2.gif',
	'singlebutton gr1.gif': 'singlebutton gr2.gif',
        'singlebutton g1.gif': 'singlebutton g2.gif',
        'singlebutton p1.gif': 'singlebutton p2.gif',
        'singlebutton br1.gif': 'singlebutton br2.gif'
}

#randomly adds a colour to gameColours
def generateColour():
	colour = randint(1,7)
	gameColours.append(coloursimg[colour])

#flashes the colour - 1 second on, 1 second off
def flashColour(colour):
	buttons[colour].config(image = PhotoImage(file = (coloursimg[colour])))
	master.update()
	time.sleep(1)
	buttons[colour].config(image = PhotoImage(file = (originalcoloursimgdict[colour])))
	master.update()
	time.sleep(1)

#flashes the colours in the gameColours list
def showColours():
	print gameColours
	for colour in gameColours:
		print 'flashing colour'
		flashColour(colour)

#enables all colour buttons
def enableButtons():
	singlebuttonr1.config(state='normal')
	singlebttonb1.config(state='normal')
	singlebuttono1.config(state='normal')
	singlebuttong1.config(state='normal')
	singlebuttongr1.config(state='normal')
	singlebuttonp1.config(state='normal')
	singlebuttonbr1.config(state='normal')

#disables all colour buttons
def disableButtons():
	singlebuttonr1.config(state='disabled')
	singlebttonb1.config(state='disabled')
	singlebuttono1.config(state='disabled')
	singlebuttong1.config(state='disabled')
	singlebuttongr1.config(state='disabled')
	singlebuttonp1.config(state='disabled')
	singlebuttonbr1.config(state='disabled')

#adds colours to the playerColours list
def addColour(colour):
	playerColours.append(colour)
	print playerColours

#compares gameColours to playerColours
def checkColours():
	global gameColours
	global playerColours
	global count
	if gameColours == playerColours:
		count +=1
		tkMessageBox.showinfo("Good Job!", "Good Job! Keep going! Next is level %d" %(count))
		playerColours = []
		return True
	else:
		tkMessageBox.showwarning("You Lose!", "You Lose! You reached level %d" %(count))
		playerColours = []
		gameColours = []
		return False

#prompts player to input pattern
def playerInput():
	tkMessageBox.showinfo("Ready?", "Enter the pattern and click check to see your result")
	enableButtons()

       
#game loop
def game():

	# while True:

	generateColour()
	showColours()
	playerInput()
	
#GUI instance
master = Tk()
w = Canvas(master, width = 500, height = 500)

master.title("Super Coder 5000")

img0 = PhotoImage(file = coloursimg['singlebutton r1.gif'])
img1 = PhotoImage(file = coloursimg['singlebutton b1.gif'])
img2 = PhotoImage(file = coloursimg['singlebutton o1.gif'])
img3 = PhotoImage(file = coloursimg['singlebutton g1.gif'])
img4 = PhotoImage(file = coloursimg['singlebutton gr1.gif'])
img5 = PhotoImage(file = coloursimg['singlebutton p1.gif'])
img6 = PhotoImage(file = coloursimg['singlebutton br1.gif'])


#Buttons
singlebuttonr1 = Button(master, state='disabled', image = img0)
singlebuttonb1 = Button(master, state='disabled', image = img1)
singlebuttono1 = Button(master, state='disabled', image = img2)
singlebuttongr1 = Button(master, state='disabled', image = img3)
singlebuttong1 = Button(master, state='disabled', image = img4)
singlebuttonp1 = Button(master, state='disabled', image = img5)
singlebuttonbr1 = Button(master, state='disabled', image = img6)
start = Button(master, text="start", bg="lightgrey", command=game)

#dictionary of button objects
buttons = {
	'singlebutton r1.gif': red,
	'singlebutton b1.gif': blue,
	'singlebutton o1.gif': yellow,
	'singlebutton g1.gif': green,
        'singlebutton gr1.gif': white,
        'singlebutton p1.gif': purple,
        'singlebutton br1.gif': brown
}

#button placement
red.place(x = 400, y = 55)
blue.place(x = 494, y = 100)
green.place(x = 515, y = 202)
yellow.place(x = 446, y = 286)
white.place(x = 354, y = 286)
purple.place(x = 284, y = 202)
brown.place(x = 306, y = 100)
start.place(x = 430, y = 400)

#main
mainloop()

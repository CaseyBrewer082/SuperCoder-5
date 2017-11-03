from Tkinter import *
from random import randint
master = Tk()
clack0 = True
gameColours = []
playerColours = []

class GUI(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master = master
        master.minsize(width = 800, height = 415)
        
    def createFrames(self):
        #The frames will not be seen. They are there so that if a Label or
        #button is changed or lost we will have a record of the proper
        #placement and dimensions.
        frame1 = Frame(height = 46, width = 200, bg = "white")
        frame1.place(x = 0, y = 0)
        frame2 = Frame(height = 46, width = 200, bg = "white")
        frame2.place(x = 0, y = 46)
        frame3 = Frame(height = 46, width = 200, bg = "white")
        frame3.place(x = 0, y = 92)
        frame4 = Frame(height = 46, width = 200, bg = "white")
        frame4.place(x = 0, y = 138)
        frame5 = Frame(height = 46, width = 200, bg = "white")
        frame5.place(x = 0, y = 184)
        frame6 = Frame(height = 46, width = 100, bg = "white")
        frame6.place(x = 0, y = 230)
        frame7 = Frame(height = 46, width = 100, bg = "white")
        frame7.place(x = 100, y = 230)
        frame8 = Frame(height = 46, width = 100, bg = "white")
        frame8.place(x = 0, y = 276)
        frame9 = Frame(height = 46, width = 100, bg = "white")
        frame9.place(x = 100, y = 276)
        frame10 = Frame(height = 46, width = 100, bg = "white")
        frame10.place(x = 0, y = 322)
        frame11 = Frame(height = 46, width = 100, bg = "white")
        frame11.place(x = 100, y = 322)
        frame12 = Frame(height = 47, width = 100, bg = "white")
        frame12.place(x = 0, y = 368)
        frame13 = Frame(height = 47, width = 100, bg = "white")
        frame13.place(x = 100, y = 368)
        frame14 = Frame(height = 369, width = 400, bg = "white")
        frame14.place(x = 200, y = 0)
        frame15 = Frame(height = 47, width = 400, bg = "white")
        frame15.place(x = 200, y = 368)
        frame16 = Frame(height = 92, width = 200, bg = "blue")
        frame16.place(x = 600, y = 0)
        frame17 = Frame(height = 323, width = 200, bg = "pink")
        frame17.place(x = 600, y = 92)
        
    def StaticLabels(self):
        #places the word REACTION in the window
        Label2 = Label(master, bg = "white", font = 20, text = "REACTION:")
        Label2.place(x = 0, y = 46, height = 46, width = 200)
        
        #places the word POINTS in the window
        Label4 = Label(master, bg = "white", font = 20, text = "POINTS:" )
        Label4.place(x = 0, y = 138, height = 46, width = 200 )
        
        #places the word perfect in the window
        Label6 = Label(master, bg = "white", fg = "green",\
                       font = 20, text = "Perfect")
        Label6.place(x = 0, y = 230, height = 46, width = 100)
        
        #places the word good in the window
        Label8 = Label(master, bg = "white", fg = "blue",\
                       font = 20, text = "Good" )
        Label8.place(x = 0, y = 276, height = 46, width = 100)
        
        #displays the word bad in the window
        Label10 = Label(master, bg = "white", fg = "red",\
                        font = 20, text = "Bad" )
        Label10.place(x = 0, y = 322, height = 46, width = 100)
        
        #displays the word miss in the window
        Label12 = Label(master, bg = "white", fg = "brown",\
                        font = 20, text = "Miss")
        Label12.place(x = 0, y = 368, height = 47, width = 100)
        
    def ChangingLabels(self):
        #sets the players name (default is player 1)
        Label1 = Label(master, bg = "white", font = 20, text = Player1Name)
        Label1.place(x = 0, y = 0, height = 46, width = 200)

        #displays average reaction time based on a global variable
        Label3 = Label(master, bg = "white", font = 20, text = average_react )
        Label3.place(x = 0, y = 92, height = 46, width = 200)
        
        #gives the players points based on a variable
        Label5 = Label(master, bg = "white", font = 20, text = points  )
        Label5.place(x = 0, y = 184, height = 46, width = 200)
        
        
        #displays the number of perfects a player has aquired
        Label7 = Label(master, bg = "white", font = 20, text = perfect )
        Label7.place(x = 100, y = 230, height = 46, width = 100)
        
        
        #displays the number of goods a player has aquired
        Label9 = Label(master, bg = "white", font = 20, text = good )
        Label9.place(x = 100, y = 276, height = 46, width = 100)
        
        #displays the number of bads a person has aquired
        Label11 = Label(master, bg = "white", font = 20, text = bad )
        Label11.place(x = 100, y = 322, height = 46, width = 100)
        
        #displays the number of misses a person has aquired
        Label13 = Label(master, bg = "white",font = 20, text = miss)
        Label13.place(x = 100, y = 368, height = 47, width = 100)
        
        #displays what type of hit a person gets
        Label_14 = Label(master, bg = "white", fg = Hit_color, image = img14)
        Label_14.place(x = 200, y = 368, height = 47, width = 400)
        
        #displays the current level
        Label_15 = Label(master, bg = "white", image = Level_1)
        Label_15.place(x = 600, y = 0, height = 92, width = 200)
        
        #displays the status of the level bar
        Label_16 = Label(master, bg = "white", image = status[0])
        Label_16.place(x = 600, y = 92, height = 323 , width = 200)
        



    def generateColour(colour):
        colour = randint(1,7)
        gameColours.append(colours[colour])
    
        
            
    #def flashButtons(self):
    def flashButtons(colour):
        buttons[colour].config(bg=colours[colour])
        master.update()
        time.sleep(1)
        buttons[colour].config(bg=originalcoloursdict[colour])
        master.update()
        time.sleep(1)

        

    def showColours():
        print gameColours
        for colour in gameColours:
            print 'flashing colour'
            flashColour(colour)

    def enableButtons():
        red.config(state='normal')
        blue.config(state='normal')
        green.config(state='normal')
        yellow.config(state='normal')
        white.config(state='normal')
        purple.config(state='normal')
        brown.config(state='normal')
    
    def disableButtons():
        red.config(state='disabled')
        blue.config(state='disabled')
        green.config(state='disabled')
        yellow.config(state='disabled')
        white.config(state='disabled')
        purple.config(state='disabled')
        brown.config(state='disabled')

    #adds colours to the playerColours list
    def addColour(colour):
        playerColours.append(colour)
        print playerColours

        
    #prompts player to input pattern
    def playerInput():
        tkMessageBox.showinfo("Ready?", "Enter the pattern and click check to see your result")
        enableButtons()
        
        
        
        
        

button_r1 = Button(master, state='disabled', bg="darkred", activebackground="red", height="5", width="5", command= lambda: addColour('red'))
button_r1.place(x = 360, y = 15)
#button 2
button_b1 = Button(master, state='disabled', bg="darkblue", activebackground="blue", height="5", width="5", command= lambda: addColour('blue'))
button_b1.place(x = 454, y = 60)
#button 3
button_o1 = Button(master, state='disabled', bg="darkgreen", activebackground="green", height="5", width="5", command= lambda: addColour('green'))
button_o1.place(x = 476, y = 162)
#button 4
button_gr1 = Button(master, state='disabled', bg="goldenrod", activebackground="yellow", height="5", width="5", command= lambda: addColour('yellow'))
button_gr1.place(x = 406, y = 255)
#button 5
button_g1 = Button(master, state='disabled', bg="grey", activebackground="white", height="5", width="5", command= lambda: addColour('white'))
button_g1.place(x = 314, y = 255)
#button 6
button_p1 = Button(master, state='disabled', bg="violet", activebackground="purple", height="5", width="5", command= lambda: addColour('purple'))
button_p1.place(x = 244, y = 162)
#button 7
button_br1 = Button(master, state='disabled', bg="tan", activebackground="brown", height="5", width="5", command= lambda: addColour('brown'))
button_br1.place(x = 266, y = 60)
#Declare changeable variables for labels
Player1Name = "Player 1"
average_react = 0
points = 0
perfect = 0
good = 0
bad = 0
miss = 0
Hit_color = "green"

#Button image variables
img0 = PhotoImage(file = 'singlebutton r1.gif')
img1 = PhotoImage(file = 'singlebutton b1.gif')
img2 = PhotoImage(file = 'singlebutton o1.gif')
img3 = PhotoImage(file = 'singlebutton g1.gif')
img4 = PhotoImage(file = 'singlebutton gr1.gif')
img5 = PhotoImage(file = 'singlebutton p1.gif')
img6 = PhotoImage(file = 'singlebutton br1.gif')
img7 = PhotoImage(file = 'singlebutton r2.gif')
img8 = PhotoImage(file = 'singlebutton b2.gif')
img9 = PhotoImage(file = 'singlebutton o2.gif')
img10 = PhotoImage(file = 'singlebutton g2.gif')
img11 = PhotoImage(file = 'singlebutton gr2.gif')
img12 = PhotoImage(file = 'singlebutton p2.gif')
img13 = PhotoImage(file = 'singlebutton br2.gif')

colours = {
    1: 'red',
    2: 'blue',
    3: 'yellow',
    4: 'green',
        5: 'white',
        6: 'purple',
        7: 'brown',
    'red': 'red',
    'blue': 'blue',
    'yellow': 'yellow',
    'green': 'green',
        'white': 'white',
        'purple': 'purple',
        'brown': 'brown'
}

originalcoloursdict = {
    'red': 'darkred',
    'blue': 'darkblue',
    'yellow': 'goldenrod',
    'green': 'darkgreen',
        'white': 'grey',
        'purple': 'violet',
        'brown': 'tan'
}

buttons = {
	'red': button_r1,
	'blue': button_b1,
	'yellow': button_o1,
	'green': button_gr1,
        'white': button_g1,
        'purple': button_p1,
        'brown': button_br1
}


#Hits image variables
img14 = PhotoImage(file = 'Perfect.gif')
img15 = PhotoImage(file = 'Good.gif')
img16 = PhotoImage(file = 'Bad.gif')
img17 = PhotoImage(file = 'Miss.gif')
                   
#Level image variables
Level_1 = PhotoImage(file = 'LEVEL1.gif')
Level_2 = PhotoImage(file = 'LEVEL2.gif')
Level_3 = PhotoImage(file = 'LEVEL3.gif')
Level_4 = PhotoImage(file = 'LEVEL4.gif')

#Level bar image variables
StatMin = PhotoImage(file = 'StatMin.gif')
Stat1 = PhotoImage(file = 'Stat1.gif')
Stat2 = PhotoImage(file = 'Stat2.gif')
Stat3 = PhotoImage(file = 'Stat3.gif') 
Stat4 = PhotoImage(file = 'Stat4.gif') 
Stat5 = PhotoImage(file = 'Stat5.gif') 
Stat6 = PhotoImage(file = 'Stat6.gif') 
Stat7 = PhotoImage(file = 'Stat7.gif') 
Stat8 = PhotoImage(file = 'Stat8.gif')
Stat9 = PhotoImage(file = 'Stat9.gif') 
Stat10 = PhotoImage(file = 'Stat10.gif') 
Stat11 = PhotoImage(file = 'Stat11.gif') 
Stat12 = PhotoImage(file = 'Stat12.gif') 
Stat13 = PhotoImage(file = 'Stat13.gif') 
Stat14 = PhotoImage(file = 'Stat14.gif') 
Stat15 = PhotoImage(file = 'Stat15.gif') 
Stat16 = PhotoImage(file = 'Stat16.gif') 
Stat17 = PhotoImage(file = 'Stat17.gif') 
Stat18 = PhotoImage(file = 'Stat18.gif') 
Stat19 = PhotoImage(file = 'Stat19.gif') 
Stat20 = PhotoImage(file = 'Stat20.gif') 
Stat21 = PhotoImage(file = 'Stat21.gif') 
Stat22 = PhotoImage(file = 'Stat22.gif') 
Stat23 = PhotoImage(file = 'Stat23.gif') 
Stat24 = PhotoImage(file = 'Stat24.gif') 
Stat25 = PhotoImage(file = 'Stat25.gif') 
Stat26 = PhotoImage(file = 'Stat26.gif') 
Stat27 = PhotoImage(file = 'Stat27.gif') 
Stat28 = PhotoImage(file = 'Stat28.gif') 
Stat29 = PhotoImage(file = 'Stat29.gif') 
Stat30 = PhotoImage(file = 'Stat30.gif') 
Stat31 = PhotoImage(file = 'Stat31.gif') 
Stat32 = PhotoImage(file = 'Stat32.gif') 
Stat33 = PhotoImage(file = 'Stat33.gif')
Stat34 = PhotoImage(file = 'Stat34.gif') 
Stat35 = PhotoImage(file = 'Stat35.gif') 
Stat36 = PhotoImage(file = 'Stat36.gif') 
Stat37 = PhotoImage(file = 'Stat37.gif') 
Stat38 = PhotoImage(file = 'Stat38.gif') 
Stat39 = PhotoImage(file = 'Stat39.gif') 
Stat40 = PhotoImage(file = 'Stat40.gif') 
Stat41 = PhotoImage(file = 'Stat41.gif') 
Stat42 = PhotoImage(file = 'Stat42.gif') 
Stat43 = PhotoImage(file = 'Stat43.gif') 
Stat44 = PhotoImage(file = 'Stat44.gif') 
Stat45 = PhotoImage(file = 'Stat45.gif') 
Stat46 = PhotoImage(file = 'Stat46.gif') 
Stat47 = PhotoImage(file = 'Stat47.gif') 
Stat48 = PhotoImage(file = 'Stat48.gif') 
Stat49 = PhotoImage(file = 'Stat49.gif') 
Stat50 = PhotoImage(file = 'Stat50.gif') 
Stat51 = PhotoImage(file = 'Stat51.gif') 
Stat52 = PhotoImage(file = 'Stat52.gif') 
Stat53 = PhotoImage(file = 'Stat53.gif') 
Stat54 = PhotoImage(file = 'Stat54.gif') 
Stat55 = PhotoImage(file = 'Stat55.gif') 
StatMax = PhotoImage(file = 'StatMax.gif') 
StatMaxFlash = PhotoImage(file = 'StatMaxFlash.gif') 

status = [StatMin, Stat1, Stat2, Stat3, Stat4\
          , Stat5, Stat6, Stat7, Stat8, Stat9\
          , Stat10, Stat11, Stat12, Stat13, Stat14\
          , Stat15, Stat16, Stat17, Stat18, Stat19\
          , Stat20, Stat21, Stat22, Stat23, Stat24\
          , Stat25, Stat26, Stat27, Stat28, Stat29\
          , Stat30, Stat31, Stat32, Stat33, Stat34\
          , Stat35, Stat36, Stat37, Stat38, Stat39\
          , Stat40, Stat41, Stat42, Stat43, Stat44\
          , Stat45, Stat46, Stat47, Stat48, Stat49\
          , Stat50, Stat51, Stat52, Stat53, Stat54\
          , Stat55, StatMax, StatMaxFlash]

def Play():
    game = GUI(master)
    game.createFrames()
    game.StaticLabels()
    game.ChangingLabels()
    game.generateColour()
    game.flashButtons()
    game.showColours()
    game.mainloop()
    

#main program
#This function will call the class and initialize the GUI
#Can be tied to a start screen and start button
Play()

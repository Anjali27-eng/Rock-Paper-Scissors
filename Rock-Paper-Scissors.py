                         # Rock Paper Scissors
"""In this rock paper scissors game,  a player who chooses rock will win by another
 player who chooses scissors but loose by the player who chooses paper; a player with paper 
 will loose by the player with the scissors. If both choose the same then the game will tie."""

#import library
from tkinter import *
import random

#initialize window
"""Tk() use to initialized Tkinter to create window
geometry() sets the window width and height
resizable(0,0) by this command we can fix the size of the window
title() used to set the title of the window
bg = ‘’ use to set the color of the background"""
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('DataFlair-Rock,Paper,Scissors')
root.config(bg ='seashell3')


#heading
"""Label() widget used when we want to display text that users can’t modify.
root is the name of our window
text which displays on the label as the title of that label
font in which form the text is written
pack used to the organized widget in form of block"""
Label(root, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', bg = 'seashell2').pack()


##user choice
'''user_take is a string type variable that stores the choice that the user enters.
Entry() widget used when we want to create an input text field.textvariable used to retrieve the text to entry widget
place() – place widgets at specific position'''
user_take = StringVar()
Label(root, text = 'choose any one: rock, paper ,scissors' , font='arial 15 bold', bg = 'seashell2').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'antiquewhite2').place(x=90 , y = 130)



#computer choice
#random.randint() function will randomly take any number from the given number.
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
    



##function to play
"""Here we give the if-else() condition to play rock paper scissors

If the computer choose 1 then the rock will set to comp_pick variable
If the computer choose 2 then the paper will set to comp_pick variable
If the computer choose 3 then scissors will set to comp_pick variable"""
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')
    
        
    
##fun to reset
def Reset():
    Result.set("") 
    user_take.set("")

##fun to exit
'''root.destroy() will quit the rock paper scissors program by stopping the mainloop().'''
def Exit():
    root.destroy()


###### button
"""Button() widget used when we want to display a button.
command called the specific function when the button will be clicked.
root.mainloop() method executes when we run our program"""
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)

root.mainloop()
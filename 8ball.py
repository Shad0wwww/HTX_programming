from tkinter import *
import random

root = Tk()
root.geometry("300x300")
root.title(" 8Ball ")

#getting the input
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    clearToTextInput()
    Output.insert(END, get_random_letter(inputs, weights))

#
#clear input
def clearToTextInput():
   Output.delete("1.0","end") 

#randomize the message 

inputs = ['yes', 'no', 'idc', 'good for you']
weights = [10, 30, 50, 10]

def get_random_letter(inputs, weights):
    r = random.uniform(0, sum(weights))
    current_cutoff = 0
    for index in range(len(weights)):
        current_cutoff = current_cutoff + weights[index]
        if r < current_cutoff:
            return inputs[index]

#the gui

l = Label(text = "Type a message")

inputtxt = Text(root, height = 10,
    width = 25,
    bg = "light yellow")
 
Output = Text(root, height = 5,
    width = 25,
    bg = "light cyan")
 
Display = Button(root, height = 2,
    width = 20,
    text ="Show",
    command = lambda:Take_input())
 
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
 
mainloop()
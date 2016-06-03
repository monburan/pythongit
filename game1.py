#coding:UTF-8
from Tkinter import *
import tkMessageBox
from random import randint
def getrandintNum():
	randint_num = randint(1,100)
	return getrandintNum
def compare2num(randint_num=getrandintNum):
	bingo = 1
    	while bingo == 1: 
    		input_num = num.get()
       		if (int(randint_num)== int(input_num)):
			tkMessage1Box.showinfo("congratulation!","this is %d"%(int(input_num)))
			print "1"
			bingo = 1       
		elif (int(randint_num) < int(input_num)):
			prompt.set("warning !too big")
			print "2"
			bingo = 0
		else:
			prompt.set("warning !too small")
			print "3"
			bingo = 0
class game():       
	def __init__(self,master):
		input_frame = Frame(master)
		input_frame.pack(side=TOP)
		input_lable = Label(input_frame,text="please input a number(0-100)").pack()
		input_button = Button(input_frame,text="GetNumber",command=getrandintNum).pack()
		input_entry = Entry(input_frame,textvariable = num).pack()
		input_button = Button(input_frame,text="Compare",command=compare2num).pack()
		output_frame = Frame(master)
		output_frame.pack(side=BOTTOM)
		Soutput_entry = Entry(output_frame,textvariable = prompt,width=200).pack()

win = Tk()
win.title("This is a game")

global input_num
global randint_num
global num
num = StringVar()
global prompt
prompt = StringVar()

app = game(win)
win.mainloop()
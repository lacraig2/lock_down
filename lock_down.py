#!/usr/bin/python3

'''
Luke Craig
01/06/2019
Lock Down app for use at Warehouse.
'''

from sys import version_info

# I do not actually want to support python 2, but will do the minimum for support.
if version_info[0] == 2:
	from Tkinter import *
else:
	from tkinter import *

debug = False

# strings
lock_down_text = "Push for Lock Down"
all_clear_text = "Push for All Clear"
exit_program_text = "Exit"

# fonts
exit_program_font = ('helvetica', 30, 'underline bold')
lock_button_font = ('helvetica', 40, 'bold')

# just nicely handles full screen toggle
class Fullscreen_Window:
	def __init__(self,tp):
		self.tk = tp
		self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
		self.frame = Frame(self.tk)
		self.frame.pack()
		self.state = False
		self.tk.bind("<F11>", self.toggle_fullscreen)
		self.tk.bind("<Escape>", self.end_fullscreen)

	def toggle_fullscreen(self, event=None):
		self.state = not self.state  # Just toggling the boolean
		self.tk.attributes("-fullscreen", self.state)
		return "break"

	def end_fullscreen(self, event=None):
		self.state = False
		self.tk.attributes("-fullscreen", False)
		return "break"

# this code gets run when the lock down button is pressed
def lock_down_now():
	print("do lock down")
	# insert lock down code here
	lock_button.configure(text = all_clear_text, command = all_clear, bg="green")

# this code gets run when the all clear button is pressed
def all_clear():
	print("all clear")
	# instert all clear code here
	lock_button.configure(text = lock_down_text, command = lock_down_now, bg="red")


top = Tk()

# we base the button on screen size
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()

# here we make the two buttons and place them
lock_button = Button(top, text = lock_down_text, command = lock_down_now, height=screen_width-50, width=screen_width-50, bg="red", font=lock_button_font)
Button(top, text=exit_program_text, height=2, width=screen_width-50, command=top.destroy, font=exit_program_font).pack()
lock_button.pack()

# make it a full screen available app
app = Fullscreen_Window(top)

# run
top.mainloop()

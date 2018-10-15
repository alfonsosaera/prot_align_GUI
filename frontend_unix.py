#!/usr/bin/env python3

# Alfonso Saera Vila
#
# V 1.0
# 10/10/2018
# Graphic user interface that aligns two protein sequences with the selected
# substitution matrix using a simplified version of the needleman-wunsch
# algorithm.
# It is based on my prot_align script https://github.com/alfonsosaera/prot_align
#
# fronted_unix.py is created with tr -d '\r' <frontend.py >frontend_unix.py
# to allow direct execution of the script from the terminal with the shebang
# in linux terminal see https://stackoverflow.com/a/30128006/7902133

from tkinter import *
import backend # import functions from backend.py

#################
# GUI Functions #
#################

# define clear_command() function for b0_5 button (CLEAR ALL)
def clear_command():
    e0_1.delete(0,END)
    e1_5.delete(0,END)
    text2_0.delete(1.0, END)

# define blosum45_command() function for b1_1 button (BLOSUM45)
def blosum45_command():
    text2_0.delete(1.0, END) # clear the text box before doing anything
    text2_0.insert(END, backend.nw_protein(file_text.get(), \
    substitution_matrix = "blosum45"))

# define blosum62_command() function for b1_2 button (BLOSUM62)
def blosum62_command():
    text2_0.delete(1.0, END) # clear the text box before doing anything
    text2_0.insert(END, backend.nw_protein(file_text.get(), \
    substitution_matrix = "blosum62"))

# define blosum80_command() function for b1_3 button (BLOSUM80)
def blosum80_command():
    text2_0.delete(1.0, END) # clear the text box before doing anything
    text2_0.insert(END, backend.nw_protein(file_text.get(), \
    substitution_matrix = "blosum80"))

# define custom_command() function for b1_4 button (Custom:)
def custom_command():
    text2_0.delete(1.0, END) # clear the text box before doing anything
    text2_0.insert(END, backend.nw_protein(file_text.get(), \
    substitution_matrix = matrix_text.get()))

#################
# Configure GUI #
#################

# Create & Configure root
root=Tk()
root.wm_title("PROTEIN ALIGNMENT by Alfonso Saera Vila")

# Create & Configure paned window
app=PanedWindow(root, width=650, height=500, orient=VERTICAL)
app.pack(fill=BOTH, expand=1)

# Create & Configure frame
frame=Frame(app)
frame.grid(row=0, column=0, sticky=N+S+E+W)
app.add(frame)

# Create the grid of elements inside frame
for row_index in range(2):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(6):
        Grid.columnconfigure(frame, col_index, weight=1)

# first row
l0_0=Label(frame, text="File")
l0_0.grid(row=0, column=0, sticky=N+E+W)

file_text=StringVar() # the text variable must be created before the entry with StringVar
e0_1=Entry(frame, textvariable=file_text)
e0_1.grid(row=0, column=1, columnspan=4, sticky=N+E+W)

b0_5=Button(frame, text="CLEAR ALL", command=clear_command)
#clear_command is a function but without() so is only executed with button is pressed
b0_5.grid(row=0, column=5, sticky=N+E+W)

# second row
l1_0=Label(frame, text="Matrix")
l1_0.grid(row=1, column=0, sticky=N+E+W)

b1_1=Button(frame, text="BLOSUM45", command=blosum45_command)
b1_1.grid(row=1, column=1, sticky=N+E+W)

b1_2=Button(frame, text="BLOSUM62", command=blosum62_command)
b1_2.grid(row=1, column=2, sticky=N+E+W)

b1_3=Button(frame, text="BLOSUM80", command=blosum80_command)
b1_3.grid(row=1, column=3, sticky=N+E+W)

b1_4=Button(frame, text="Custom:", command=custom_command)
b1_4.grid(row=1, column=4, sticky=N+E+W)

matrix_text=StringVar() # the text variable must be created before the entry with StringVar
e1_5=Entry(frame, textvariable=matrix_text)
e1_5.grid(row=1, column=5, sticky=N+E+W)

# Create & Configure text box
text2_0=Text(app)
app.add(text2_0)
# Create & Configure scrollbar
sb1=Scrollbar(text2_0)
sb1.pack(fill=Y, side=RIGHT)
# link scrollbar with the list box
text2_0.configure(yscrollcommand=sb1.set)
sb1.configure(command=text2_0.yview)


root.mainloop()

# Calculator using TKinter

# Importing the Libraries
from tkinter import Tk
from tkinter import Entry
from tkinter import Frame
from tkinter import Button
from tkinter import Label
from tkinter import StringVar


#-------------------------------------------------Programming Logic-------------------------------------------------

def click(event):
    try:
        text = event.widget.cget('text')  # return the value of widget clicked
        if text == '=':
            if scvalue.get().isdigit():
                value = int(scvalue.get())
            else:
                value = eval(scvalue.get())
            scvalue.set(value)
        elif text == 'CLR':
            scvalue.set('')
        elif text == 'CLS':
            root.destroy()
        else:
            scvalue.set(scvalue.get() + text)
    except:
        scvalue.set('ERROR')

#-------------------------------------------------Programming Logic-------------------------------------------------


#-------------------------------------------------GUI Logic-------------------------------------------------

# setting up the GUI Window
# opening the GUI window
root = Tk()                                                                 # creating the root object of Tk class
root.geometry('388x528')                                                    # setting the default window size of GUI
root.minsize(388, 528)                                                      # setting the minimum window size of GUI
root.maxsize(388, 528)                                                      # setting the maximum window size of GUI
root.title('Calculator by Yashasvi Bhatt')                                  # giving the title of GUI Window
root.wm_iconbitmap('images/calculator_icon.ico')                                       # setting the icon of GUI Window


# setting the input field for calculator
scvalue = StringVar()
scvalue.set('')
input_field = Entry(textvariable = scvalue, font = 'lucida 30 bold', borderwidth = 10).pack(padx = 5)


# creating buttons for calculator
button = [['9', '8', '7', '+'], ['6', '5', '4', '-'], ['3', '2', '1', '*'], ['.', '0', '=', '/'], ['%', 'CLR', '00', 'CLS']]
Label(text = '', bg = 'grey', width = 388).pack()
for line in range(5):
    # creating frame for n line
    f = Frame(bg='grey')

    # creating buttons for 9, 8, 7, +
    for value in button[line]:
        b = Button(f, text = value, font = 'lucida 20 bold', width = 3, borderwidth = 10)
        b.pack(side='left', padx = 10, pady = 10)
        b.bind('<Button-1>', click)                                         # binding the button with event

    f.pack()


# holding the GUI window open
root.mainloop()

#-------------------------------------------------GUI Logic-------------------------------------------------
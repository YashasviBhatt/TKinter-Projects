# Notepad using TKinter

# Importing the Libraries
from tkinter import Tk
from tkinter import Text
from tkinter import Menu
from tkinter import Scrollbar
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
import os


#-------------------------------------------------Programming Logic-------------------------------------------------

# function to create a new file
def newFile():
    root.title('Untitled - Notepad by Yashasvi Bhatt')
    file = None
    TextArea.delete(1.0, 'end')

# funtion to open an existing file
def openFile():
    global file
    file = askopenfilename(defaultextension = '.txt', filetypes = [('All Files', '*.*'), ('Text Documents', '*.*')])
    if file == '':
        file = None
    else:
        # changing the title of GUI Window
        root.title(os.path.basename(file) + ' - Notepad by Yashasvi Bhatt')
        TextArea.delete(1.0, 'end')
        # replacing the content of text area with content of file
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()

# funtion to save the current file
def saveFile():
    global file
    if file == None:
        # opening save file dialog and setting pre-requisites
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = '.txt', filetypes = [('All Files', '*.*'), ('Text Documents', '*.*')])
        if file == '':
            file = None
        else:
            # saving the content of text area to a file
            f = open(file, 'w')
            f.write(TextArea.get(1.0, 'end'))
            f.close()
            # changing the title of GUI Window
            root.title(os.path.basename(file) + ' - Notepad by Yashasvi Bhatt')
    else:
        # directly saving the content
        f = open(file, 'w')
        f.write(TextArea.get(1.0, 'end'))
        f.close()

# function to exit the appliaction
def quitApp():
    root.destroy()

# function to cut the content
def cut():
    TextArea.event_generate('<<Cut>>')

# function to copy the content
def copy():
    TextArea.event_generate('<<Copy>>')

# function to paste the content
def paste():
    TextArea.event_generate('<<Paste>>')

# function to show info About the Notepad
def about():
    showinfo('About Notepad', 'Notepad made by Yashasvi Bhatt')

# function for help
def hlp():
    showinfo('Help', 'Mail me at : yashasvibhatt9@gmail.com')

#-------------------------------------------------Programming Logic-------------------------------------------------


#-------------------------------------------------GUI Logic-------------------------------------------------

# setting up the GUI Window
# opening the GUI window
root = Tk()                                                                 # creating the root object of Tk class
root.geometry('500x500')                                                    # setting the default window size of GUI
root.title('Untitled - Notepad by Yashasvi Bhatt')                          # giving the title of GUI Window
root.wm_iconbitmap('images/notepad_icon.ico')                               # setting the icon of GUI Window


# setting up the main layout of notepad

# creating a text area to insert user input data
TextArea = Text(font = 'lucida 11')
file = None
TextArea.pack(expand = True, fill = 'both')

# adding scrollbar to text area
Scroll = Scrollbar(TextArea)
Scroll.pack(side = 'right', fill = 'y')
Scroll.config(command = TextArea.yview)
TextArea.config(yscrollcommand = Scroll.set)

# creating a menu bar
MenuBar = Menu()

# creating file menu
FileMenu = Menu(MenuBar, tearoff = 0)
FileMenu.add_command(label = 'New', command = newFile)                      # submenu to create new file
FileMenu.add_command(label = 'Open', command = openFile)                    # submenu to open an existing file
FileMenu.add_command(label = 'Save', command = saveFile)                    # submenu to save the current file
FileMenu.add_separator()                                                    # adding separator
FileMenu.add_command(label = 'Exit', command = quitApp)                     # submenu to exit the application
MenuBar.add_cascade(label = 'File', menu = FileMenu)                        # adding the File Menu to MenuBar

# creating edit menu
EditMenu = Menu(MenuBar, tearoff = 0)
EditMenu.add_command(label = 'Cut', command = cut)                          # submenu to cut the content
EditMenu.add_command(label = 'Copy', command = copy)                        # submenu to copy the content
EditMenu.add_command(label = 'Paste', command = paste)                      # submenu to paste the content
MenuBar.add_cascade(label = 'Edit', menu = EditMenu)                        # adding the Edit Menu to MenuBar

# creating help menu
HelpMenu = Menu(MenuBar, tearoff = 0)
HelpMenu.add_command(label = 'About Notepad', command = about)              # submenu to show info about Notepad
HelpMenu.add_separator()                                                    # adding separator
HelpMenu.add_command(label = 'Help', command = hlp)                         # submenu for help
MenuBar.add_cascade(label = 'Help', menu = HelpMenu)                        # adding the Help Menu to MenuBar

root.config(menu = MenuBar)


# holding the GUI window open
root.mainloop()

#-------------------------------------------------GUI Logic-------------------------------------------------
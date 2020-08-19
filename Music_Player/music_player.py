# Music Player using TKinter

# Importing the libraries and classes
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Listbox
from tkinter.filedialog import askopenfilename
import os
from tkinter.messagebox import showerror
from pygame import mixer


#-------------------------------------------------Programming Logic-------------------------------------------------

music_list = list()
mixer.init()                                            # initializing the pygame mixer

# creating function to add music to list
def addMusic():
    global music_file
    music_file = askopenfilename(defaultextension = '.mp3', filetypes=[("Music Files", "*.mp3")])
    if music_file != '':
        if music_file in music_list:
            showerror('Error Adding Song', 'Song Already Exists')
        else:
            songs_list.insert('end', os.path.basename(music_file))
            music_list.append(music_file)

# creating function to remove music from list
def removeMusic():
    current_selected_file = songs_list.curselection()
    if current_selected_file:
        songs_list.delete(current_selected_file)
        music_list.pop(current_selected_file[0])
    else:
        songs_list.delete('end')
        music_list.pop()

# creating function to play music from list
def playMusic():
    current_seleted_file = songs_list.curselection()
    if current_seleted_file:
        mixer.music.load(music_list[current_seleted_file[0]])                           # loading the file
        mixer.music.play()                                                              # playing the file
    else:
        for music_index in range(len(music_list)):
            mixer.music.load(music_list[music_index])
            mixer.music.play(1)
            while mixer.music.get_busy():
                print('You Window might be showing not responding, \ndon\'t worry, \nit will respond as soon as your playlist completely plays all songs')
                continue


#-------------------------------------------------Programming Logic-------------------------------------------------


#-------------------------------------------------GUI Logic-------------------------------------------------

# setting up the GUI Window
# opening the GUI Window
root = Tk()
root.geometry('488x345')                                                    # setting the default window size of GUI
root.minsize(488, 345)                                                      # setting the minsize of GUI Window
root.maxsize(488, 345)                                                      # setting the maxsize of GUI Window
root.title('Music Player by Yashasvi Bhatt')                                # setting the title to GUI Window
root.wm_iconbitmap('images/music_icon.ico')                                 # setting the icon of GUI Window

# setting the main content of GUI

Label(text = 'Your Music Player', bg = '#392eb8', fg = '#ffffff', font = 'lucida 20 bold', width = 30, height = 2).place(x = 0, y = 0)

# creating button to add music to list
Button(text = 'Add Music', command = addMusic, font = 'lucida 15 bold', borderwidth = 5, width = 12).place(x = 30, y = 110)
# creating button to remove music from list
Button(text = 'Remove Music', command = removeMusic, font = 'lucida 15 bold', borderwidth = 5, width = 12).place(x = 30, y = 175)
# creating button to play the music from list
Button(text = 'Play Music', command = playMusic, font = 'lucida 15 bold', borderwidth = 5, width = 12).place(x = 30, y = 240)

# creating list box which contains list of names of song
songs_list = Listbox(width = 40, height = 12)
songs_list.place(x = 210, y = 101)

# holding the window open
root.mainloop()

#-------------------------------------------------GUI Logic-------------------------------------------------
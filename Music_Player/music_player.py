# Music Player using TKinter

# Importing the libraries and classes
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Listbox
from tkinter.filedialog import askopenfilename
import os
from tkinter.messagebox import showerror
import pygame as pg
from playsound import  playsound


#-------------------------------------------------Programming Logic-------------------------------------------------

music_list = list()

# creating function to add music to list
def addMusic():
    global music_file
    global music_list
    music_file = askopenfilename(defaultextension = '.mp3', filetypes=[("Music Files", "*.mp3")])
    if music_file != '':
        if music_file in music_list:
            showerror('Error Adding Song', 'Song Already Exists')
        else:
            songs_list.insert('end', os.path.basename(music_file))
            music_list.append(music_file)
    root.update()

# creating function to remove music from list
def removeMusic():
    current_selected_file = songs_list.curselection()
    if len(music_list) != 0:
        if current_selected_file:
            songs_list.delete(current_selected_file)
            music_list.pop(current_selected_file[0])
        else:
            songs_list.delete('end')
            music_list.pop()
    else:
        showerror('Error Deleting Song', 'Nothing to Delete')
    root.update()

# creating function to play music from list
def playMusic():
    current_seleted_file = songs_list.curselection()
    if current_seleted_file:
        pg.mixer.music.load(music_list[current_seleted_file[0]])                           # loading the file
        pg.mixer.music.play()                                                              # playing the file
    else:
        showerror('Can\'t Play', 'Select a Song First')


# creating function to play all music from playlist
def playAll():
    # setting up pygame window
    pg.init()                                                       # initializing the pygame
    screen = pg.display.set_mode((600, 400))                        # setting up the window size
    pg.display.set_caption('Playlist Player')                       # setting the title of pygame window
    background_image = pg.image.load("images/pygame.jpg").convert()

    song_finished = pg.USEREVENT                                    # creating a custom event type
    pg.mixer.music.set_endevent(song_finished)                      # when the music ends pygame will add the song_finished event to event queue
    pg.mixer.music.load(music_list[0])                              # loading a playing the first music
    pg.mixer.music.play()
    music_index = 0                                                 # index of first song
    done = False
    pause = True

    while not done:
        screen.blit(background_image, (0, 0))                       # putting the text object on screen
        for event in pg.event.get():
            if event.type == pg.QUIT:                               # if user close the window
                done = True
            elif event.type == pg.KEYDOWN:                          # if user give key input using keyboaard
                if event.key == pg.K_RIGHT:                         # if user press RIGHT KEY then next song will play
                    if music_index < len(music_list) - 1:
                        music_index += 1
                        pg.mixer.music.load(music_list[music_index])
                        pg.mixer.music.play()
                elif event.key == pg.K_LEFT:                        # if user press LEFT KEY then previous song will play
                    if music_index > 0:
                        music_index -= 1
                        pg.mixer.music.load(music_list[music_index])
                        pg.mixer.music.play()
                elif event.key == pg.K_SPACE:                       # if user press SPACE KEY then song will pause/resume
                    if pause:
                        pg.mixer.music.unpause()
                        pause = False
                    else:
                        pg.mixer.music.pause()
                        pause = True
            # if no key command is given then
            elif event.type == song_finished:
                if music_index < len(music_list) - 1:
                    pg.mixer.music.load(music_list[music_index + 1])
                    pg.mixer.music.play()
                else:                                               # if all songs played completely then stop
                    pg.mixer.music.stop()
                    print('You Playlist Complete')
            pg.display.update()
    pg.quit()

#-------------------------------------------------Programming Logic-------------------------------------------------


#-------------------------------------------------GUI Logic-------------------------------------------------

# setting up the GUI Window
# opening the GUI Window
root = Tk()
root.geometry('488x380')                                                    # setting the default window size of GUI
root.minsize(488, 380)                                                      # setting the minsize of GUI Window
root.maxsize(488, 380)                                                      # setting the maxsize of GUI Window
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
# creating button to play all the music from list
Button(text = 'Play All', command = playAll, font = 'lucida 15 bold', borderwidth = 5, width = 12).place(x = 30, y = 305)

# creating list box which contains list of names of song
songs_list = Listbox(width = 40, height = 15)
songs_list.place(x = 210, y = 109)

# holding the window open
root.mainloop()

#-------------------------------------------------GUI Logic-------------------------------------------------
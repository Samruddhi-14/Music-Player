
from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer

col1 = "#ffffff"     #white
col2 = "#e1c9bf"     #light pink
col3 = "#333333"     #black
col4 = "#ff3564"     #dark pink

window = Tk()
window.title("Music Player")
window.geometry("352x255")
window.configure(background=col1)
window.resizable(width=FALSE, height=FALSE)

#events
def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def continue_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index+1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0,END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

def previous_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index-1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0,END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

#frames
left_frame = Frame(window, width = 150, height = 150, bg = col1)
left_frame.grid(row=0,column=0, padx=1 ,pady=1 )

right_frame = Frame(window, width = 250, height = 150, bg=col3)
right_frame.grid(row = 0, column = 1, padx = 0)

down_frame = Frame(window, width = 400, height = 100, bg=col2)
down_frame.grid(row = 1, column = 0, columnspan = 3, padx=0, pady=1)

#right frame
listbox = Listbox(right_frame,selectmode = SINGLE, font=("Arial 9 bold"), width = 22, bg=col3, fg = col1)
listbox.grid(row=0,column=0)

w=Scrollbar(right_frame)
w.grid(row=0,column=1)

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)

#Images
img_1 = Image.open('logo.png')
img_1 = img_1.resize((120,120))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, width = 140,height = 170, image = img_1, padx=0, bg = col1)
app_image.place(x=0,y=0)

img_2 = Image.open('rewind.png')
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)
prev_button = Button(down_frame, width = 30,height = 30, font = "Ivy 10",image = img_2, padx=0, bg = col1,command=previous_music)
prev_button.place(x=30+28,y=45)

img_3 = Image.open('play.png')
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)
play_button = Button(down_frame, width = 30,height = 30, font = "Ivy 10",image = img_3, padx=0, bg = col1,command=play_music)
play_button.place(x=70+28,y=45)

img_4 = Image.open('fast-forward.png')
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)
next_button = Button(down_frame, width = 30,height = 30, font = "Ivy 10",image = img_4, padx=0, bg = col1,command=next_music)
next_button.place(x=110+28,y=45)

img_5 = Image.open('pause.png')
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)
pause_button = Button(down_frame, width = 30,height = 30, font = "Ivy 10",image = img_5, padx=0, bg = col1,command=pause_music)
pause_button.place(x=150+28,y=45)

img_6 = Image.open('continue.png')
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6)
continue_button = Button(down_frame, width = 30,height = 30, font = "Ivy 10",image = img_6, padx=0, bg = col1,command=continue_music)
continue_button.place(x=190+28,y=45)

img_7= Image.open('stop.png')
img_7 = img_7.resize((30,30))
img_7 = ImageTk.PhotoImage(img_7)
stop_button = Button(down_frame, width = 30,height = 30, font = "Ivy 10",image = img_7, padx=0, bg = col1,command=stop_music)
stop_button.place(x=230+28,y=45)


line = Label(left_frame, height = 1,width = 200, padx=10, bg = col3)
line.place(x=0,y=1)

line = Label(left_frame, width=200,height = 1,padx = 10, bg = col1)
line.place(x=0,y=3)

running_song = Label(down_frame, text = "Choose a song", font=("Ivy 10"), width = 44, height = 1, padx = 10,bg = col1, fg = col3, anchor=NW)
running_song.place(x=0,y=1)


os.chdir(r'C:\Users\SAMRUDDHI GUJAR\music player\songs')
songs = os.listdir()

def show():
    for i in songs:
        listbox.insert(END,i)

show()

mixer.init()
music_state = StringVar()
music_state.set("Choose one!")

window.mainloop()
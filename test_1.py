from logging import root
from tkinter import ttk
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
from numpy.ma import var
from tkinter import filedialog
import pygame
import sys
import os
from tkinter import messagebox
import time

music_player = tkr.Tk()
music_player.title("TGNR player")
music_player.geometry("320x500")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='white', selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def close():
    pygame.mixer.music.stop()
    music_player.destroy()
    music_player.quit()


def on_enter(e):
    e.widget['background'] = 'green'


def on_leave(e):
    e.widget['background'] = 'black'


def enter(e):
    e.widget['background'] = 'yellow'


def leave(e):
    e.widget['background'] = 'black'


def next_song(next_one=None):
    next_one = play_list.curselection()
    next_one = next_one[0] + 1
    song = play_list.get(next_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    play_list.selection_clear(0)
    play_list.activate(next_one)
    play_list.selection_set(next_one, last=None)


def previuos_song():
    next_one = play_list.curselection()
    next_one = next_one[0] - 1
    song = play_list.get(next_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    play_list.selection_clear(0)
    play_list.activate(next_one)
    play_list.selection_set(next_one, last=None)


Button1 = tkr.Button(music_player, width=4, height=1, font="Helvetica 12 bold", text="PLAY", command=play, bg="black",
                     fg="white")
Button1.bind("<Enter>", on_enter)
Button1.bind("<Leave>", on_leave)
Button2 = tkr.Button(music_player, width=4, height=1, font="Helvetica 12 bold", text="STOP", command=stop, bg="black",
                     fg="white")
Button2.bind("<Enter>", on_enter)
Button2.bind("<Leave>", on_leave)
Button3 = tkr.Button(music_player, width=3, height=1, font="Helvetica 12 bold", text="PAUSE", command=pause,
                     bg="black", fg="white")
Button3.bind("<Enter>", on_enter)
Button3.bind("<Leave>", on_leave)
Button4 = tkr.Button(music_player, width=3, height=1, font="Helvetica 12 bold", text="UNPAUSE", command=unpause,
                     bg="black", fg="white")
Button4.bind("<Enter>", on_enter)
Button4.bind("<Leave>", on_leave)
Button5 = tkr.Button(music_player, width=2, height=2, text="Close the Window", font="Helvetica 12 bold",
                     command=close,
                     bg="red", fg="white")
Button6 = tkr.Button(music_player, width=7, height=1, font="Helvetica 12 bold", text="NEXT", command=next_song,
                     bg="black", fg="white")
Button6.bind("<Enter>", enter)
Button6.bind("<Leave>", leave)
Button7 = tkr.Button(music_player, width=7, height=1, font="Helvetica 12 bold", text="previuos", command=previuos_song,
                     bg="black", fg="white")
Button7.bind("<Enter>", enter)
Button7.bind("<Leave>", leave)
var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button6.pack(fill="y")
Button7.pack(fill="y")
Button5.pack(fill="x")
play_list.pack(fill=tkr.BOTH, expand=True)
music_player.mainloop()

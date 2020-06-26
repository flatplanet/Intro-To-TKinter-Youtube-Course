from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('Codemy.com MP3 Player')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x300")

# Initialze Pygame Mixer
pygame.mixer.init()



#Add Song Function
def add_song():
	song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
	
	#strip out the directory info and .mp3 extension from the song name
	song = song.replace("C:/gui/audio/", "")
	song = song.replace(".mp3", "")

	# Add song to listbox
	song_box.insert(END, song)

# Play selected song
def play():
	song = song_box.get(ACTIVE)
	song = f'C:/gui/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

# Stop playing current song
def stop():
	pygame.mixer.music.stop()
	song_box.selection_clear(ACTIVE)

# Create Playlist Box
song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_box.pack(pady=20)

# Define Player Control Button Images
back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img =  PhotoImage(file='images/forward50.png')
play_btn_img =  PhotoImage(file='images/play50.png')
pause_btn_img =  PhotoImage(file='images/pause50.png')
stop_btn_img =  PhotoImage(file='images/stop50.png')

# Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0)
stop_button =  Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Add Song Menu 
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)

root.mainloop()
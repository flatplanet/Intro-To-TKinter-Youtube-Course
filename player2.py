from tkinter import *
import pygame
from tkinter import filedialog
from mutagen.mp3 import MP3
# pip install mutagen
import tkinter.ttk as ttk


root = Tk()
root.title('Codemy.com MP3 Player')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x400")

my_menu = Menu(root)
root.config(menu=my_menu)

pygame.mixer.init()

global current_song 

back_btn = PhotoImage(file='images/back50.png')
forward_btn = PhotoImage(file='images/forward50.png')
play_btn = PhotoImage(file='images/play50.png')
pause_btn = PhotoImage(file='images/pause50.png')
stop_btn = PhotoImage(file='images/stop50.png')

song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="green", selectforeground="black")
song_box.pack(pady=20)


def next_song():
	next_one = song_box.curselection()
	
	next_one = next_one[0]+1
	song = song_box.get(next_one)
	song = f"C:/gui/audio/{song}.mp3"

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
	
	song_box.selection_clear(0, END)

	song_box.activate(next_one)
	song_box.selection_set(next_one, last=None)
	
def previous_song():
	previous = song_box.curselection()
	previous = previous[0]-1
	song = song_box.get(previous)
	song = f"C:/gui/audio/{song}.mp3"

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
	song_box.selection_clear(0, END)

	song_box.activate(previous)
	song_box.selection_set(previous, last=None)
	#song_box.selection_anchor(previous)

	

def delete_song():
	song_box.delete(ANCHOR)
	pygame.mixer.music.stop()

def delete_all_songs():
	song_box.delete(0, END)
	pygame.mixer.music.stop()

def add_song():
	song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 files", "*.mp3"), ))
	song = song.replace("C:/gui/audio/", "")
	song = song.replace(".mp3", "")
	song_box.insert(END, song)

def add_many_songs():
	songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 files", "*.mp3"), ))
	
	for song in songs:
		song = song.replace("C:/gui/audio/", "")
		song = song.replace(".mp3", "")
		song_box.insert(END, song)


def open_file():
	global current_song
	current_song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 files", "*.mp3"), ))

def play():

	song = song_box.get(ACTIVE)
	song = f"C:/gui/audio/{song}.mp3"
	
	song_box.activate(ACTIVE)
	song_box.selection_set(ACTIVE, last=None)

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
	
	songMUT = MP3(song)
	songLength = songMUT.info.length
	global seconds
	seconds = songLength
	songLength = songLength / 60
	songLength = round(songLength, 2)
	song_length.config(text=f'Song Length: {songLength} - Seconds: {int(seconds)}')
	
	global my_slider
	my_slider.config(to=seconds, value=0)
	#my_slider = ttk.Scale(root, from_=0, to=seconds, orient=HORIZONTAL, value=2)
	#my_slider.pack(pady=10, padx=10)

	play_time()

	

def stop():
	pygame.mixer.music.stop()
	song_box.selection_clear(ACTIVE) 



global paused 
paused = False

def pause_song(is_paused):
	global paused
	paused = is_paused

	if paused:
		pygame.mixer.music.unpause()
		paused = False
	else:
		pygame.mixer.music.pause()
		paused = True

def slide(test):
	song = song_box.get(ACTIVE)
	song = f"C:/gui/audio/{song}.mp3"

	current_song_pos = int(pygame.mixer.music.get_pos() / 1000)
	current_slider_pos = int(my_slider.get())

	if current_song_pos == current_slider_pos:
		slide_label.config(text="TRUE")
	else:
		pygame.mixer.music.load(song)
		pygame.mixer.music.play(loops=0, start=current_slider_pos)
		my_slider.config(variable=current_slider_pos)
		#slide_label.config(text=f'song: {current_song_pos} || slider: {current_slider_pos}')

controls = Frame(root)
controls.pack()

previous_song_button = Button(controls, image=back_btn, borderwidth=0, command=previous_song)
previous_song_button.grid(row=0, column=0, padx=10)

my_button = Button(controls, image=play_btn, borderwidth=0, font=("Helvetica", 32), command=play)
my_button.grid(row=0, column=1, padx=10)

pause_song_button = Button(controls, image=pause_btn, borderwidth=0, command=lambda: pause_song(paused))
pause_song_button.grid(row=0, column=2, padx=10)

stop_button = Button(controls, image=stop_btn, borderwidth=0, command=stop)
stop_button.grid(row=0, column=3, padx=10)

next_song_button = Button(controls, image=forward_btn, borderwidth=0, command=next_song)
next_song_button.grid(row=0, column=4, padx=10)

my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.pack(pady=10, padx=10)



#open_song_button = Button(root, text="Open Song", command=open_file)
#open_song_button.pack(pady=30)

#options_frame = Frame(root)
#options_frame.pack(pady=20)

#add_song_button = Button(options_frame, text="Add Song To Playlist", command=add_song)
#add_song_button.grid(row=0, column=0, padx=20)

#delete_song_button = Button(options_frame, text="Delete Song From Playlist", command=delete_song)
#delete_song_button.grid(row=0, column=1, padx=20)



add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

remove_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)

def play_time():
	#my_slider.config(value=current_slider_pos)
	#stuff = pygame.mixer.music.get_pos() / 1000
	stuff = my_slider.get()
	pos_lbl.config(text=f'Current: {int(stuff)}')
	if int(stuff) == int(seconds):
		pass
	else:
		my_slider.config(value=stuff+1)
	#my_slider.set(int(stuff))
	pos_lbl.after(1000, play_time)



pos_btn = Button(root, text="Time Playing", command=play_time).pack()
pos_lbl = Label(root, text="")
pos_lbl.pack()

song_length = Label(root, text='')
song_length.pack()

slide_label_btn = Button(root, text="Slider", command=slide)
slide_label_btn.pack()

slide_label = Label(root, text='')
slide_label.pack(pady=10)

root.mainloop()
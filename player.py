from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title('Codemy.com MP3 Player')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x400")

# Initialze Pygame Mixer
pygame.mixer.init()


# Grab Song Length Time Info
def play_time():
	# Check for double timing
	if stopped:
		return 
	# Grab Current Song Elapsed Time
	current_time = pygame.mixer.music.get_pos() / 1000

	# throw up temp label to get data
	#slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}')
	# convert to time format
	converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

	# Get Currently Playing Song
	#current_song = song_box.curselection()
	#Grab song title from playlist
	song = song_box.get(ACTIVE)
	# add directory structure and mp3 to song title
	song = f'C:/gui/audio/{song}.mp3'
	# Load Song with Mutagen
	song_mut = MP3(song)
	# Get song Length
	global song_length
	song_length = song_mut.info.length
	# Convert to Time Format
	converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

	# Increase current time by 1 second
	current_time +=1
	
	if int(my_slider.get()) == int(song_length):
		status_bar.config(text=f'Time Elapsed: {converted_song_length}  of  {converted_song_length}  ')
	elif paused:
		pass
	elif int(my_slider.get()) == int(current_time):
		# Update Slider To position
		slider_position = int(song_length)
		my_slider.config(to=slider_position, value=int(current_time))

	else:
		# Update Slider To position
		slider_position = int(song_length)
		my_slider.config(to=slider_position, value=int(my_slider.get()))
		
		# convert to time format
		converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))

		# Output time to status bar
		status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')

		# Move this thing along by one second
		next_time = int(my_slider.get()) + 1
		my_slider.config(value=next_time)






	# Output time to status bar
	#status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')

	# Update slider position value to current song position...
	#my_slider.config(value=int(current_time))
	
	
	# update time
	status_bar.after(1000, play_time)


#Add Song Function
def add_song():
	song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
	
	#strip out the directory info and .mp3 extension from the song name
	song = song.replace("C:/gui/audio/", "")
	song = song.replace(".mp3", "")

	# Add song to listbox
	song_box.insert(END, song)

# Add many songs to playlist
def add_many_songs():
	songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))	

	# Loop thru song list and replace directory info and mp3
	for song in songs:
		song = song.replace("C:/gui/audio/", "")
		song = song.replace(".mp3", "")
		# Insert into playlist
		song_box.insert(END, song)

# Play selected song
def play():
	# Set Stopped Variable To False So Song Can Play
	global stopped
	stopped = False
	song = song_box.get(ACTIVE)
	song = f'C:/gui/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	# Call the play_time function to get song length
	play_time()

	# Update Slider To position
	#slider_position = int(song_length)
	#my_slider.config(to=slider_position, value=0)
	
	# Get current volume
	#current_volume = pygame.mixer.music.get_volume()
	#slider_label.config(text=current_volume * 100)

	# Get current Volume
	current_volume = pygame.mixer.music.get_volume()
	# Times by 100 to make it easier to work with
	current_volume = current_volume * 100
	#slider_label.config(text=current_volume * 100)

	# Change Volume Meter Picture
	if int(current_volume) < 1:
		volume_meter.config(image=vol0)
	elif int(current_volume) > 0 and int(current_volume) <= 25:
		volume_meter.config(image=vol1)
	elif int(current_volume) >= 25 and int(current_volume) <= 50:
		volume_meter.config(image=vol2)
	elif int(current_volume) >= 50 and int(current_volume) <= 75:
		volume_meter.config(image=vol3)
	elif int(current_volume) >= 75 and int(current_volume) <= 100:
		volume_meter.config(image=vol4)


# Stop playing current song
global stopped
stopped = False
def stop():
	# Reset Slider and Status Bar
	status_bar.config(text='')
	my_slider.config(value=0)
	# Stop Song From Playing
	pygame.mixer.music.stop()
	song_box.selection_clear(ACTIVE)

	# Clear The Status Bar
	status_bar.config(text='')

	# Set Stop Variable To True
	global stopped
	stopped = True 

	# Get current Volume
	current_volume = pygame.mixer.music.get_volume()
	# Times by 100 to make it easier to work with
	current_volume = current_volume * 100
	#slider_label.config(text=current_volume * 100)

	# Change Volume Meter Picture
	if int(current_volume) < 1:
		volume_meter.config(image=vol0)
	elif int(current_volume) > 0 and int(current_volume) <= 25:
		volume_meter.config(image=vol1)
	elif int(current_volume) >= 25 and int(current_volume) <= 50:
		volume_meter.config(image=vol2)
	elif int(current_volume) >= 50 and int(current_volume) <= 75:
		volume_meter.config(image=vol3)
	elif int(current_volume) >= 75 and int(current_volume) <= 100:
		volume_meter.config(image=vol4)

# Play The Next Song in the playlist
def next_song():
	# Reset Slider and Status Bar
	status_bar.config(text='')
	my_slider.config(value=0)

	# Get the current song tuple number
	next_one = song_box.curselection() 
	# Add one to the current song number
	next_one = next_one[0]+1
	#Grab song title from playlist
	song = song_box.get(next_one)
	# add directory structure and mp3 to song title
	song = f'C:/gui/audio/{song}.mp3'
	# Load and play song
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	# Clear active bar in playlist listbox
	song_box.selection_clear(0, END)

	# Activate new song bar
	song_box.activate(next_one)

	# Set Active Bar to Next Song
	song_box.selection_set(next_one, last=None)

# Play Previous Song In Playlist
def previous_song():
	# Reset Slider and Status Bar
	status_bar.config(text='')
	my_slider.config(value=0)
	# Get the current song tuple number
	next_one = song_box.curselection() 
	# Add one to the current song number
	next_one = next_one[0]-1
	#Grab song title from playlist
	song = song_box.get(next_one)
	# add directory structure and mp3 to song title
	song = f'C:/gui/audio/{song}.mp3'
	# Load and play song
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	# Clear active bar in playlist listbox
	song_box.selection_clear(0, END)

	# Activate new song bar
	song_box.activate(next_one)

	# Set Active Bar to Next Song
	song_box.selection_set(next_one, last=None)

# Delete A Song
def delete_song():
	stop()
	# Delete Currently Selected Song
	song_box.delete(ANCHOR)
	# Stop Music if it's playing
	pygame.mixer.music.stop()

# Delete All Songs from Playlist
def delete_all_songs():
	stop()
	# Delete All Songs
	song_box.delete(0, END)
	# Stop Music if it's playing
	pygame.mixer.music.stop()

# Create Global Pause Variable
global paused
paused = False

# Pause and Unpause The Current Song
def pause(is_paused):
	global paused
	paused = is_paused

	if paused:
		# Unpause
		pygame.mixer.music.unpause()
		paused = False
	else:
		# Pause
		pygame.mixer.music.pause()
		paused = True
	
# Create slider function
def slide(x):
	#slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
	song = song_box.get(ACTIVE)
	song = f'C:/gui/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

# Create Volume Function
def volume(x):
	pygame.mixer.music.set_volume(volume_slider.get())
	
	# Get current Volume
	current_volume = pygame.mixer.music.get_volume()
	# Times by 100 to make it easier to work with
	current_volume = current_volume * 100
	#slider_label.config(text=current_volume * 100)

	# Change Volume Meter Picture
	if int(current_volume) < 1:
		volume_meter.config(image=vol0)
	elif int(current_volume) > 0 and int(current_volume) <= 25:
		volume_meter.config(image=vol1)
	elif int(current_volume) >= 25 and int(current_volume) <= 50:
		volume_meter.config(image=vol2)
	elif int(current_volume) >= 50 and int(current_volume) <= 75:
		volume_meter.config(image=vol3)
	elif int(current_volume) >= 75 and int(current_volume) <= 100:
		volume_meter.config(image=vol4)	

# Create Master Frame
master_frame = Frame(root)
master_frame.pack(pady=20)

# Create Playlist Box
song_box = Listbox(master_frame, bg="black", fg="green", width=60, selectbackground="green", selectforeground="black")
song_box.grid(row=0, column=0)

# Define Player Control Button Images
back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img =  PhotoImage(file='images/forward50.png')
play_btn_img =  PhotoImage(file='images/play50.png')
pause_btn_img =  PhotoImage(file='images/pause50.png')
stop_btn_img =  PhotoImage(file='images/stop50.png')

# Define Volume Control Images
global vol0
global vol1
global vol2
global vol3
global vol4
vol0 = PhotoImage(file='images/volume0.png')
vol1 = PhotoImage(file='images/volume1.png')
vol2 = PhotoImage(file='images/volume2.png')
vol3 = PhotoImage(file='images/volume3.png')
vol4 = PhotoImage(file='images/volume4.png')

# Create Player Control Frame
controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)

# Create Volume Meter
volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=1, column=1, padx=10)

# Create Volume Label Frame
volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=30)

# Create Player Control Buttons
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button =  Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Add Song Menu 
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
# Add Many Songs to playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

# Create Delete Song Menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)

# Create Status Bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create Music Position Slider
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid(row=2, column=0, pady=10)

# Create Volume Slider
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.pack(pady=10)


# Create Temporary Slider Label
#slider_label = Label(root, text="0")
#slider_label.pack(pady=10)

root.mainloop()
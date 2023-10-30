import pygame
import os

# Initialize pygame
pygame.init()

# Set up the music directory
music_dir = 'path_to_your_music_directory'
os.chdir(music_dir)
music_files = [file for file in os.listdir() if file.endswith('.mp3')]

# Initialize the music player
pygame.mixer.init()

# Create a function to play music
def play_music(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

# Create a function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Main music player loop
while True:
    print("\nAvailable songs:")
    for i, song in enumerate(music_files):
        print(f"{i + 1}. {song}")

    choice = input("\nEnter the song number to play (q to quit): ")

    if choice.lower() == 'q':
        break

    try:
        song_number = int(choice) - 1
        if 0 <= song_number < len(music_files):
            selected_song = os.path.join(music_dir, music_files[song_number])
            play_music(selected_song)
        else:
            print("Invalid song number. Try again.")
    except ValueError:
        print("Invalid input. Try again.")

# Clean up and exit
pygame.mixer.quit()
pygame.quit()

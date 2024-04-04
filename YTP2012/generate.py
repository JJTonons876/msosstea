import os
from moviepy.editor import *
import random
import tkinter as tk
from tkinter import filedialog

# Function to generate YTP-style video
def generate_ytp_video(video_path, audio_path, music_path, photo_path, gif_path, mlg_path):
    # Load video
    video_clip = VideoFileClip(video_path)

    # Load audio
    audio_clip = AudioFileClip(audio_path)

    # Load music
    music_clip = AudioFileClip(music_path)

    # Load photo
    photo_clip = ImageClip(photo_path)

    # Load GIF
    gif_clip = ImageClip(gif_path)

    # Load MLG
    mlg_clip = VideoFileClip(mlg_path)

    # Applying YTP effects
    # You can implement various effects here using MoviePy functions

    # Example: Ear Rape
    audio_clip = audio_clip.fx.audio_normalize()

    # Example: Stutter Loop
    video_clip = video_clip.fx.speedx(factor=2)

    # Example: Sentence Mixing
    # You'd need some NLP tools for this part to manipulate subtitles

    # Example: Spadinner
    # This involves fast-paced, chaotic editing

    # Example: Special Effects
    # Add various effects using MoviePy functions

    # Concatenate clips
    final_clip = concatenate_videoclips([video_clip, music_clip.set_duration(video_clip.duration)])

    # Set audio
    final_clip = final_clip.set_audio(audio_clip)

    # Add overlays
    final_clip = CompositeVideoClip([final_clip, photo_clip.set_duration(final_clip.duration).set_position(("center", "bottom")),
                                     gif_clip.resize(width=200).set_duration(final_clip.duration).set_position(("right", "top")),
                                     mlg_clip.resize(final_clip.size).set_duration(final_clip.duration).set_position(("left", "top"))])

    # Write to file
    final_clip.write_videofile("output_ytp.mp4", codec='libx264', audio_codec='aac')

# Function to browse and select files
def browse_files(file_type):
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                           filetypes=(("Video files", "*.mp4"),
                                                      ("Audio files", "*.mp3"),
                                                      ("All files", "*.*")))
    if filename:
        if file_type == "video":
            video_entry.delete(0, tk.END)
            video_entry.insert(0, filename)
        elif file_type == "audio":
            audio_entry.delete(0, tk.END)
            audio_entry.insert(0, filename)
        # Similarly for other file types...

# GUI setup
root = tk.Tk()
root.title("YTP Style Video Generator")

video_label = tk.Label(root, text="Video:")
video_label.grid(row=0, column=0, sticky="e")
video_entry = tk.Entry(root, width=50)
video_entry.grid(row=0, column=1, columnspan=2)
video_button = tk.Button(root, text="Browse", command=lambda: browse_files("video"))
video_button.grid(row=0, column=3)

# Similarly setup for other file types...

generate_button = tk.Button(root, text="Generate YTP Video",
                            command=lambda: generate_ytp_video(video_entry.get(), audio_entry.get(),
                                                               music_entry.get(), photo_entry.get(),
                                                               gif_entry.get(), mlg_entry.get()))
generate_button.grid(row=6, column=0, columnspan=4)

root.mainloop()

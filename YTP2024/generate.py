import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp
import random

class YTPGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("YTP Generator")

        self.video_button = tk.Button(master, text="Browse Video", command=self.browse_video)
        self.video_button.pack()

        self.audio_button = tk.Button(master, text="Browse Audio", command=self.browse_audio)
        self.audio_button.pack()

        # Add buttons for other sources (music, photo, GIF, MLG)

        self.generate_button = tk.Button(master, text="Generate YTP", command=self.generate_ytp)
        self.generate_button.pack()

    def browse_video(self):
        self.video_path = filedialog.askopenfilename()

    def browse_audio(self):
        self.audio_path = filedialog.askopenfilename()

    # Define functions for other sources

    def generate_ytp(self):
        # Load video
        video_clip = mp.VideoFileClip(self.video_path)

        # Load audio
        audio_clip = mp.AudioFileClip(self.audio_path)

        # Add stutter loop
        video_clip = video_clip.fx(mp.vfx.speedx, factor=random.uniform(0.5, 2))

        # Add ear rape
        audio_clip = audio_clip.volumex(random.uniform(2, 10))

        # Apply special effects
        # Example: add spadinner text
        video_clip = video_clip.subclip(0, 5).fx(mp.vfx.text.fx(0.01, "Spadinner!"))

        # Combine video and audio
        video_clip = video_clip.set_audio(audio_clip)

        # Export the final YTP
        output_path = "output_ytp.mp4"
        video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

        # Display success message or open the output file

root = tk.Tk()
app = YTPGeneratorApp(root)
root.mainloop()

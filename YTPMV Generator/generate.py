import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, concatenate_videoclips
from pydub import AudioSegment

class YTPMVGenerator:
    def __init__(self, master):
        self.master = master
        master.title("YTPMV Generator")

        self.video_button = tk.Button(master, text="Select Video", command=self.select_video)
        self.video_button.pack()

        self.sound_button = tk.Button(master, text="Select Sound", command=self.select_sound)
        self.sound_button.pack()

        self.music_button = tk.Button(master, text="Select Music", command=self.select_music)
        self.music_button.pack()

        self.pitch_scale = tk.Scale(master, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, label="Pitch")
        self.pitch_scale.pack()

        self.generate_button = tk.Button(master, text="Generate YTPMV", command=self.generate_ytpmv)
        self.generate_button.pack()

    def select_video(self):
        self.video_path = filedialog.askopenfilename()

    def select_sound(self):
        self.sound_path = filedialog.askopenfilename()

    def select_music(self):
        self.music_path = filedialog.askopenfilename()

    def generate_ytpmv(self):
        video_clip = VideoFileClip(self.video_path)
        sound_clip = AudioSegment.from_file(self.sound_path)
        music_clip = AudioSegment.from_file(self.music_path)

        # Adjust pitch
        pitch_factor = self.pitch_scale.get()
        sound_clip = sound_clip._spawn(sound_clip.raw_data, overrides={'frame_rate': int(sound_clip.frame_rate * pitch_factor)})
        
        # Combine sound and music
        final_audio = sound_clip.overlay(music_clip)

        # Combine video and audio
        final_video = video_clip.set_audio(final_audio)

        # Export YTPMV
        final_video.write_videofile("output_ytpmv.mp4", codec="libx264", audio_codec="aac")

root = tk.Tk()
app = YTPMVGenerator(root)
root.mainloop()

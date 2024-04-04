import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

class VideoEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("YTP Kids Video Editor")
        
        # Create buttons
        self.browse_video_btn = tk.Button(master, text="Browse Video", command=self.browse_video)
        self.browse_audio_btn = tk.Button(master, text="Browse Audio", command=self.browse_audio)
        self.browse_music_btn = tk.Button(master, text="Browse Music", command=self.browse_music)
        self.browse_photo_btn = tk.Button(master, text="Browse Photo", command=self.browse_photo)
        self.browse_gif_btn = tk.Button(master, text="Browse GIF", command=self.browse_gif)
        self.combine_btn = tk.Button(master, text="Combine", command=self.combine)

        # Layout
        self.browse_video_btn.pack()
        self.browse_audio_btn.pack()
        self.browse_music_btn.pack()
        self.browse_photo_btn.pack()
        self.browse_gif_btn.pack()
        self.combine_btn.pack()

    def browse_video(self):
        self.video_path = filedialog.askopenfilename(title="Select Video File")

    def browse_audio(self):
        self.audio_path = filedialog.askopenfilename(title="Select Audio File")

    def browse_music(self):
        self.music_path = filedialog.askopenfilename(title="Select Music File")

    def browse_photo(self):
        self.photo_path = filedialog.askopenfilename(title="Select Photo File")

    def browse_gif(self):
        self.gif_path = filedialog.askopenfilename(title="Select GIF File")

    def combine(self):
        video_clip = VideoFileClip(self.video_path)
        
        if hasattr(self, 'audio_path'):
            audio_clip = AudioFileClip(self.audio_path)
            video_clip = video_clip.set_audio(audio_clip)

        if hasattr(self, 'music_path'):
            music_clip = AudioFileClip(self.music_path)
            video_clip = video_clip.set_audio(music_clip)

        if hasattr(self, 'photo_path'):
            photo_clip = ImageClip(self.photo_path)
            photo_clip = photo_clip.set_duration(video_clip.duration)
            video_clip = CompositeVideoClip([video_clip, photo_clip])

        if hasattr(self, 'gif_path'):
            gif_clip = VideoFileClip(self.gif_path)
            gif_clip = gif_clip.set_duration(video_clip.duration)
            video_clip = CompositeVideoClip([video_clip, gif_clip])
        
        output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        video_clip.write_videofile(output_path, codec='libx264', fps=24)

def main():
    root = tk.Tk()
    app = VideoEditorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

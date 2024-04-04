import moviepy.editor as mp
from moviepy.video.fx import all as vfx
from tkinter import filedialog, Tk, Button, Label, messagebox
from PIL import Image, ImageTk

class YTPMVGenerator:
    def __init__(self, master):
        self.master = master
        master.title("YTPMV Generator")

        self.video_path = None
        self.audio_path = None

        self.label = Label(master, text="Welcome to YTPMV Generator!")
        self.label.pack()

        self.browse_video_button = Button(master, text="Browse Video", command=self.browse_video)
        self.browse_video_button.pack()

        self.browse_audio_button = Button(master, text="Browse Audio", command=self.browse_audio)
        self.browse_audio_button.pack()

        self.generate_button = Button(master, text="Generate YTPMV", command=self.generate_ytpmv)
        self.generate_button.pack()

    def browse_video(self):
        self.video_path = filedialog.askopenfilename(title="Select Video File")
        if self.video_path:
            messagebox.showinfo("Video Selected", f"Video selected: {self.video_path}")

    def browse_audio(self):
        self.audio_path = filedialog.askopenfilename(title="Select Audio File")
        if self.audio_path:
            messagebox.showinfo("Audio Selected", f"Audio selected: {self.audio_path}")

    def generate_ytpmv(self):
        if self.video_path and self.audio_path:
            video_clip = mp.VideoFileClip(self.video_path)
            audio_clip = mp.AudioFileClip(self.audio_path)

            # Apply some example visual effects
            video_clip = video_clip.fx(vfx.rotate, lambda t: 45*t)
            video_clip = video_clip.fx(vfx.speedx, 2)
            video_clip = video_clip.set_audio(audio_clip)

            # Output the YTPMV
            output_path = "output_ytpmv.mp4"
            video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
            messagebox.showinfo("YTPMV Generated", f"YTPMV generated and saved as: {output_path}")
        else:
            messagebox.showerror("Error", "Please select both video and audio files.")

root = Tk()
app = YTPMVGenerator(root)
root.mainloop()

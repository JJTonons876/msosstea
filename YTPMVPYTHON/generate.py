import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from tkinter import Tk, Label, Button, Entry, filedialog

class YTPMVGenerator:
    def __init__(self, master):
        self.master = master
        master.title("YTPMV Generator")

        self.label = Label(master, text="YTPMV Generator")
        self.label.pack()

        self.select_video_button = Button(master, text="Select Video", command=self.select_video)
        self.select_video_button.pack()

        self.select_audio_button = Button(master, text="Select Audio", command=self.select_audio)
        self.select_audio_button.pack()

        self.output_entry = Entry(master)
        self.output_entry.pack()

        self.generate_button = Button(master, text="Generate YTPMV", command=self.generate_ytpmv)
        self.generate_button.pack()

    def select_video(self):
        self.video_path = filedialog.askopenfilename()
        print("Selected Video:", self.video_path)

    def select_audio(self):
        self.audio_path = filedialog.askopenfilename()
        print("Selected Audio:", self.audio_path)

    def generate_ytpmv(self):
        if not hasattr(self, 'video_path') or not hasattr(self, 'audio_path'):
            print("Please select both video and audio files.")
            return

        output_path = self.output_entry.get()
        if not output_path:
            print("Please enter the output file path.")
            return

        video_clip = VideoFileClip(self.video_path)
        audio_clip = AudioFileClip(self.audio_path)
        
        # Make the video shorter if necessary to match audio duration
        if video_clip.duration > audio_clip.duration:
            video_clip = video_clip.subclip(0, audio_clip.duration)
        
        # Set audio of the video to the selected audio
        video_clip = video_clip.set_audio(audio_clip)

        # Write the video with the new audio
        video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        print("YTPMV Generated successfully!")

root = Tk()
ytpmv_generator = YTPMVGenerator(root)
root.mainloop()

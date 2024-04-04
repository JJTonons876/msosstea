import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, concatenate_videoclips

class VideoMashupApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Mashup App")

        self.clips = []

        self.select_button = tk.Button(master, text="Select Video Clips", command=self.select_video_clips)
        self.select_button.pack()

        self.create_button = tk.Button(master, text="Create Mashup", command=self.create_mashup)
        self.create_button.pack()

    def select_video_clips(self):
        file_paths = filedialog.askopenfilenames(title="Select Video Clips", filetypes=[("Video files", "*.mp4")])
        for file_path in file_paths:
            self.clips.append(VideoFileClip(file_path))

    def create_mashup(self):
        if len(self.clips) < 2:
            print("Please select at least 2 video clips.")
            return
        
        final_clip = concatenate_videoclips(self.clips)
        final_clip.write_videofile("mashup.mp4")

        print("Mashup video created successfully!")

def main():
    root = tk.Tk()
    app = VideoMashupApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

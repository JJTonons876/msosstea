import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, concatenate_videoclips

class VideoMashupGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Karameesh Video Mashup Remix Generator")

        self.video_files = []

        self.label = tk.Label(master, text="Karameesh Video Mashup Remix Generator")
        self.label.pack()

        self.add_button = tk.Button(master, text="Add Video", command=self.add_video)
        self.add_button.pack()

        self.generate_button = tk.Button(master, text="Generate Remix", command=self.generate_remix)
        self.generate_button.pack()

    def add_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
        if file_path:
            self.video_files.append(file_path)

    def generate_remix(self):
        if not self.video_files:
            return

        video_clips = [VideoFileClip(file) for file in self.video_files]
        final_clip = concatenate_videoclips(video_clips)
        final_clip.write_videofile("output.mp4")

def main():
    root = tk.Tk()
    app = VideoMashupGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

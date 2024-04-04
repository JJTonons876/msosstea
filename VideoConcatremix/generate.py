import os
from tkinter import *
from tkinter import filedialog
from moviepy.editor import *

class VideoRemixerApp:
    def __init__(self, master):
        self.master = master
        master.title("Video Remix Culture")

        self.label = Label(master, text="Video Remix Culture")
        self.label.pack()

        self.select_button = Button(master, text="Select Video", command=self.select_video)
        self.select_button.pack()

        self.remix_button = Button(master, text="Remix Video", command=self.remix_video)
        self.remix_button.pack()

    def select_video(self):
        self.video_path = filedialog.askopenfilename(initialdir="/", title="Select Video File",
                                                      filetypes=(("Video Files", "*.mp4 *.avi"), ("All Files", "*.*")))
        print("Selected video:", self.video_path)

    def remix_video(self):
        if hasattr(self, 'video_path'):
            video_clip = VideoFileClip(self.video_path)
            # Your remixing logic here
            # For example, you can apply some effects, concatenate clips, etc.
            # For demonstration, let's just overlay text
            text_clip = TextClip("Remixed by Video Remix Culture", fontsize=50, color='white').set_duration(5)
            final_clip = CompositeVideoClip([video_clip, text_clip.set_position(('center', 'bottom'))])
            output_path = os.path.splitext(self.video_path)[0] + "_remixed.mp4"
            final_clip.write_videofile(output_path, codec='libx264')
            final_clip.close()
            print("Remixed video saved at:", output_path)
        else:
            print("Please select a video first")

def main():
    root = Tk()
    app = VideoRemixerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

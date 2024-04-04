import tkinter as tk
from tkinter import ttk
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips

class FakeVideoGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fake Video Generator")
        self.root.geometry("400x300")

        self.commercial_btn = ttk.Button(self.root, text="Generate Commercial Fake", command=self.generate_commercial_fake)
        self.commercial_btn.pack(pady=10)

        self.advert_btn = ttk.Button(self.root, text="Generate Advert Fake", command=self.generate_advert_fake)
        self.advert_btn.pack(pady=10)

    def generate_commercial_fake(self):
        clip_duration = 10  # Duration of the generated clip in seconds
        output_file = "commercial_fake.mp4"

        # Placeholder commercial content
        text_clip = TextClip("Commercial Content", fontsize=70, color='white', bg_color='black').set_duration(clip_duration)

        # Generate video clip
        text_clip.write_videofile(output_file, fps=24)

        # Show success message
        tk.messagebox.showinfo("Success", "Commercial Fake Video generated successfully!")

    def generate_advert_fake(self):
        clip_duration = 10  # Duration of the generated clip in seconds
        output_file = "advert_fake.mp4"

        # Placeholder advert content
        text_clip = TextClip("Advert Content", fontsize=70, color='white', bg_color='black').set_duration(clip_duration)

        # Generate video clip
        text_clip.write_videofile(output_file, fps=24)

        # Show success message
        tk.messagebox.showinfo("Success", "Advert Fake Video generated successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FakeVideoGenerator(root)
    root.mainloop()

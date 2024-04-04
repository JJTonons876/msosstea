import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, AudioFileClip

class YTPMVGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("YTPMV Generator")

        self.input_video_label = tk.Label(master, text="Input Video:")
        self.input_video_label.grid(row=0, column=0, padx=10, pady=10)

        self.input_video_entry = tk.Entry(master, width=50)
        self.input_video_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_video)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        self.output_audio_label = tk.Label(master, text="Output Audio:")
        self.output_audio_label.grid(row=1, column=0, padx=10, pady=10)

        self.output_audio_entry = tk.Entry(master, width=50)
        self.output_audio_entry.grid(row=1, column=1, padx=10, pady=10)

        self.generate_button = tk.Button(master, text="Generate YTPMV", command=self.generate_ytpmv)
        self.generate_button.grid(row=2, column=1, padx=10, pady=10)

    def browse_video(self):
        filename = filedialog.askopenfilename(filetypes=(("Video files", "*.mp4;*.avi;*.mov"), ("All files", "*.*")))
        self.input_video_entry.delete(0, tk.END)
        self.input_video_entry.insert(0, filename)

    def generate_ytpmv(self):
        input_video_path = self.input_video_entry.get()
        output_audio_path = self.output_audio_entry.get()

        if not input_video_path:
            tk.messagebox.showerror("Error", "Please select an input video.")
            return

        if not output_audio_path:
            tk.messagebox.showerror("Error", "Please specify an output audio path.")
            return

        try:
            video_clip = VideoFileClip(input_video_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(output_audio_path)
            tk.messagebox.showinfo("Success", "YTPMV generated successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error occurred: {str(e)}")

def main():
    root = tk.Tk()
    ytpmv_generator = YTPMVGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

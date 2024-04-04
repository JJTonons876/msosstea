import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, concatenate_videoclips
from PIL import Image, ImageTk

class KidsVideoRemixerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kids Video Remix and Parody")
        
        self.selected_video_paths = []
        self.selected_audio_path = None
        self.selected_image_paths = []
        self.selected_gif_paths = []
        
        # Create browse buttons
        self.browse_video_button = tk.Button(self.master, text="Browse Videos", command=self.browse_videos)
        self.browse_video_button.pack()
        
        self.browse_audio_button = tk.Button(self.master, text="Browse Audio", command=self.browse_audio)
        self.browse_audio_button.pack()
        
        self.browse_image_button = tk.Button(self.master, text="Browse Images", command=self.browse_images)
        self.browse_image_button.pack()
        
        self.browse_gif_button = tk.Button(self.master, text="Browse GIFs", command=self.browse_gifs)
        self.browse_gif_button.pack()
        
        # Create remix button
        self.remix_button = tk.Button(self.master, text="Remix", command=self.remix_videos)
        self.remix_button.pack()
        
    def browse_videos(self):
        video_paths = filedialog.askopenfilenames(title="Select Videos", filetypes=(("Video files", "*.mp4;*.avi"), ("All files", "*.*")))
        self.selected_video_paths = list(video_paths)
        
    def browse_audio(self):
        audio_path = filedialog.askopenfilename(title="Select Audio", filetypes=(("Audio files", "*.mp3;*.wav"), ("All files", "*.*")))
        self.selected_audio_path = audio_path
        
    def browse_images(self):
        image_paths = filedialog.askopenfilenames(title="Select Images", filetypes=(("Image files", "*.jpg;*.png"), ("All files", "*.*")))
        self.selected_image_paths = list(image_paths)
        
    def browse_gifs(self):
        gif_paths = filedialog.askopenfilenames(title="Select GIFs", filetypes=(("GIF files", "*.gif"), ("All files", "*.*")))
        self.selected_gif_paths = list(gif_paths)
        
    def remix_videos(self):
        # Load videos
        video_clips = [VideoFileClip(video_path) for video_path in self.selected_video_paths]
        
        # Load audio
        audio_clip = VideoFileClip(self.selected_audio_path).audio
        
        # Combine videos
        final_clip = concatenate_videoclips(video_clips)
        
        # Add images and gifs
        for image_path in self.selected_image_paths:
            image = Image.open(image_path)
            final_clip = final_clip.set_duration(final_clip.duration + 2) # Extend duration to accommodate image display time
            final_clip = final_clip.set_pos(('center', 'center')).set_position(('center', 'center')).set_opacity(0.5).set_duration(2).blit(im=image, xy=(0, 0))
        
        for gif_path in self.selected_gif_paths:
            gif = Image.open(gif_path)
            gif = gif.resize((final_clip.size[0], final_clip.size[1]))
            gif = gif.convert('RGBA')
            final_clip = final_clip.set_duration(final_clip.duration + 2) # Extend duration to accommodate gif display time
            final_clip = final_clip.set_pos(('center', 'center')).set_position(('center', 'center')).set_duration(2).blit(im=gif, xy=(0, 0))
        
        # Set audio
        final_clip = final_clip.set_audio(audio_clip)
        
        # Save final remix
        final_clip.write_videofile("kids_remix.mp4", codec='libx264', audio_codec='aac')
        
        # Close video clips
        for clip in video_clips:
            clip.close()
        
        # Notify user
        tk.messagebox.showinfo("Remix Complete", "Remixing complete. Check 'kids_remix.mp4'.")
        

def main():
    root = tk.Tk()
    app = KidsVideoRemixerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

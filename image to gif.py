from moviepy import VideoFileClip

clip = VideoFileClip(r"C:\Users\Dell\OneDrive\Documents\Image Website\WhatsApp Video 2026-01-26 at 4.58.22 PM.mp4")
clip.write_gif("gif_2.gif")
clip.close()

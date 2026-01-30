from moviepy import VideoFileClip

#add your video patha to convert into GIF 
clip = VideoFileClip(r"C:\Users\Dell\OneDrive\Documents\Image Website\WhatsApp Video 2026-01-26 at 4.58.22 PM.mp4")
#give the name of the GIF file with Extention ".gif"
clip.write_gif("gif_2.gif")
clip.close()


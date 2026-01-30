# -MP4-video-file-into-a-GIF-using-Python-
This project converts an MP4 video file into a GIF using Python and the moviepy library. It works in an isolated virtual environment to avoid dependency issues.
Step 1: Create Virtual Environment

Open PowerShell in the project folder and run:

python -m venv .venv

🔹 Step 2: Activate Virtual Environment
PowerShell
.venv\Scripts\activate


After activation, you will see:

(.venv)

🔹 Step 3: Install Required Module

Install moviepy inside the virtual environment:

pip install moviepy

🔹 Step 4: Python Script Code

Use this code in image to gif.py:

from moviepy import VideoFileClip

clip = VideoFileClip("Status.mp4")
clip.write_gif("gif_1.gif", fps=10)
clip.close()


Make sure the video file name and path are correct.

▶️ Step 5: Run the Script
python "image to gif.py"


After successful execution, a GIF file will be generated in the same folder.

⚠️ Important Instructions

Always activate the virtual environment before running the script

Install modules inside the virtual environment only

Video file name must be exactly correct (case-sensitive)

If video is in another folder, use full file path

WhatsApp videos may show warnings — they are safe to ignore

🚫 Common Mistakes

Running script without activating .venv

Installing packages globally instead of inside .venv

Wrong video file name or path

Using old import style (moviepy.editor)

✅ Correct Import (MoviePy 2.x)
from moviepy import VideoFileClip

📌 Notes

Warnings related to last frames are normal

GIF creation will still complete successfully

FPS can be adjusted to control size and quality

🧹 Deactivate Virtual Environment

After work is done:

deactivate

✅ Done!

Your video-to-GIF converter is now ready to use 🎉

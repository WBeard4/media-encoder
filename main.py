import ffmpeg
import tkinter
from tkinter import filedialog
import os
# Check file path for any ProRes videos in folder
# Create a new Proxies folder if it doesnt already exist
# Create a new video in h.264 mp4 format for each video in the source folder
# Keep running and checking until folder is closed

def get_folder_path():
    root = tkinter.Tk()
    root.withdraw()    
    folder_path = filedialog.askdirectory()
    if folder_path is not None:
        return folder_path
    
def convert_to_proxy():
    pass

def main():
    folder_path = get_folder_path()
    if folder_path:
        for video in os.listdir(folder_path):
            video_path = os.path.join(folder_path, video)

            if video.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):
                print(f"Processing video: {video_path}")
                convert_to_proxy()

if __name__ == "__main__":
    main()
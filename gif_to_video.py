import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def select_file():
    """
    Opens a file dialog for selecting a GIF file.
    Returns the selected file path.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select a GIF File",
        filetypes=[("GIF files", "*.gif")]
    )
    return file_path

def convert_gif_to_video(input_gif, output_video, frame_rate=24):
    """
    Converts a GIF to a video file.
    
    Parameters:
        input_gif (str): Path to the input GIF file.
        output_video (str): Path for the output video file (e.g., output.mp4).
        frame_rate (int): Frame rate for the output video. Default is 24.
    """
    try:
        # Load the GIF
        clip = VideoFileClip(input_gif)
        
        # Set the frame rate and write the video file
        clip.write_videofile(output_video, fps=frame_rate, codec="libx264", audio=False)
        print(f"Conversion successful! Video saved to {output_video}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Select the GIF file
    input_gif = select_file()
    if not input_gif:
        print("No file selected. Exiting.")
        exit()
    
    # Specify the output video file
    output_video = input_gif.rsplit(".", 1)[0] + ".mp4"
    
    # Convert the GIF to video
    convert_gif_to_video(input_gif, output_video)

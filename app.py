import os
import sys
from moviepy.editor import VideoFileClip

def convert_video_to_audio(input_file, output_file):
    try:
        video = VideoFileClip(input_file)
        audio = video.audio
        audio.write_audiofile(output_file)
        video.close()
        print(f"Conversion successful! Audio saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python video_to_audio_converter.py input_video_file output_audio_file")
    else:
        input_video = sys.argv[1]
        output_audio = sys.argv[2]
        convert_video_to_audio(input_video, output_audio)

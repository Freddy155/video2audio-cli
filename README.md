# CLI Video to Audio Converter

This is a command-line tool to convert video files to audio files using Python. It utilizes the `moviepy` library to extract audio from video files and save it as audio files.

## Installation

Before using the Video to Audio Converter, you need to install the necessary libraries. You can do this using `pip`.

```bash
pip install moviepy
```

Usage
-----

To convert a video to an audio file, use the following command-line syntax:

```bash
python video_to_audio_converter.py input_video output_audio
```

-   `input_video`: The path to the input video file that you want to convert.
-   `output_audio`: The path to the output audio file you wish to create.

Example:

```bash
python video_to_audio_converter.py input_video.mp4 output_audio.mp3
```

Replace `input_video.mp4` with the path to your video file and `output_audio.mp3` with the desired name for the output audio file.

Errors
------

If any errors occur during the conversion process, the application will display an error message indicating the issue.
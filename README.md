# 

## 🖥 Introduction <a name="introduction"></a>
Record your clip and this app will take care of the rest. The objective of this project is to edit and auto schedule your favorite clips on your social media (YouTube, Facebook and Twitter).

I created this project mainly to play around with the different APIs Google, Twitter and Meta offer and try at the same time to create a fun and useful tool.

## Screenshots 
<p align="center">
<img src="https://user-images.githubusercontent.com/60163267/185815338-5fce8701-0cb6-4a7c-ac9a-f0f4060e6dee.PNG">
</p>

## Table of Contents
1. [Introduction](#introduction)
2. [Acknowledgements](#acknowledgements)
3. [Useful documentation and libraries used](#lib)
4. [Getting Started](#install)
5. [Notes](#notes)


## 🎖 Acknowledgements <a name="acknowledgements"></a>
The stylesheets "dark_teal" theme for the Qt widgets was maded by GCPDS, Copyright (c) 2020, GCPDS, All rights reserved.

https://github.com/UN-GCPDS/qt-material

## 📚 Useful documentation and libraries used <a name="lib"></a>
- YouTube API (https://developers.google.com/youtube/v3/guides/uploading_a_video)
- MoviePy - for video editing (https://zulko.github.io/moviepy/)
- qt-materials (https://github.com/UN-GCPDS/qt-material)

## 🏃‍♂️ Getting Started <a name="install"></a>

Create a virtual environment via the command:

    python3 -m venv venv

This creates the folder `venv/` in your current directory. It will contain the necessary libraries for running the examples.

To activate the virtual environment, use the following command:

```
# On Windows:
call venv\Scripts\activate.bat
# On Mac / Linux:
source venv/bin/activate
```

Now execute the following to install the necessary dependencies:

    pip install -r requirements.txt


You can the program with the command:

    python main.py

Please note that the virtual environment must still be active for this to work.

## Notes <a name="notes"></a>
The video editor section found in [`/editor/video.py`](https://github.com/alexismurari/videoedit/blob/main/editor/video.py) is not connected to the GUI yet.

## Todo <a name="todo"></a>

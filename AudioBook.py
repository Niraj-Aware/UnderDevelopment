#!/usr/bin/env python

import streamlit as st
from pydub import AudioSegment
from pydub.playback import play

# Define the file path for the audiobook
file_path = "C:\\Users\\niraj\\Downloads\\The_Red_Notebook.mp3"

def play_audio(audio_file):
    # Load the audio file using Pydub
    audio = AudioSegment.from_file(audio_file, format="mp3")

    # Play the audio file using Pydub
    play(audio)

def main():
    # Create a dropdown menu to select the audiobook to play
    audio_choice = st.sidebar.selectbox(
        "Select Audiobook",
        list(audio_files.keys())
    )

    # Get the file path for the selected audiobook
    audio_file = audio_files[audio_choice]

    # Add buttons to play, pause, skip forward, and skip backward
    if st.button("Play"):
        play_audio(audio_file)

    if st.button("Pause"):
        play_audio(audio_file).stop()

    if st.button("Skip Forward 15 Seconds"):
        audio = AudioSegment.from_file(audio_file, format="mp3")
        audio += 15 * 1000  # Add 15 seconds to the audio segment
        play(audio)

    if st.button("Skip Backward 15 Seconds"):
        audio = AudioSegment.from_file(audio_file, format="mp3")
        audio -= 15 * 1000  # Subtract 15 seconds from the audio segment
        play(audio)

if __name__ == "__main__":
    # Define the available audiobooks
    audio_files = {
        "The Red Notebook": file_path,
        # Add more audiobook files here
    }

    # Run the app
    main()

#!/usr/bin/env python

import streamlit as st
from pydub import AudioSegment
import os

# Function to play audio
def play_audio(audio_file):
    audio = AudioSegment.from_file(audio_file)
    audio.export("audio.wav", format="wav")
    os.system("afplay audio.wav") # Replace with appropriate command for your OS

# Main function
def main():
    st.title("Audiobook Player")

    # Upload audio file
    audio_file = st.file_uploader("Upload an audio file in MP3 format", type=["mp3"])

    # Check if audio file is uploaded
    if audio_file is not None:
        # Play audio
        play_audio(audio_file)

if __name__ == "__main__":
    main()

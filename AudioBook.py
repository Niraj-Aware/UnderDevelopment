import streamlit as st
import time
from pydub import AudioSegment
from pydub.playback import play


# Define the audio files and their names
audio_files = {'Book 1': 'book1.mp3',
               'Book 2': 'book2.mp3',
               'Book 3': 'book3.mp3'}

# Define the audio player function
def play_audio(file_path):
    audio = AudioSegment.from_file(file_path, format="mp3")
    play(audio)


# Define the Streamlit app
def main():
    st.title("Audiobook Player")

    # Create a dropdown menu to select the audiobook to play
    selected_audio = st.selectbox("Select an audiobook to play", list(audio_files.keys()))

    # Load the selected audiobook
    file_path = audio_files[selected_audio]

    # Create play/pause, skip forward/backward buttons
    if st.button('Play'):
        play_audio(file_path)
    elif st.button('Pause'):
        play_audio(file_path).stop()
    elif st.button('Skip Forward'):
        play_audio(file_path + ' -ss 15')
    elif st.button('Skip Backward'):
        play_audio(file_path + ' -ss -15')


if __name__ == "__main__":
    main()

import streamlit as st
import PyPDF2
from io import StringIO
from gtts import gTTS
from IPython.display import Audio

# function to extract text from PDF file
def extract_text(pdf_file):
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page in range(pdf_reader.getNumPages()):
        page_obj = pdf_reader.getPage(page)
        text += page_obj.extractText()
    return text

# function to convert text to audio file
def text_to_audio(text):
    audio_file = StringIO()
    tts = gTTS(text=text, lang='en')
    tts.write_to_fp(audio_file)
    return audio_file.getvalue()

# main function
def main():
    st.title("PDF to Audiobook Converter")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # display the text content of the PDF file
        with st.spinner('Extracting text from PDF...'):
            text = extract_text(uploaded_file)
        st.subheader("PDF Content:")
        st.write(text)

        # option to listen to the audio version of the text
        if st.button("Listen to Audiobook"):
            with st.spinner('Converting text to audio...'):
                audio_content = text_to_audio(text)
            st.audio(audio_content)

if __name__ == "__main__":
    main()

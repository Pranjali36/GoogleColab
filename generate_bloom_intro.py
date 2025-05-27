import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="Bloom Intro Generator", page_icon="🌸")

st.title("🎙️ Generate Bloom's Intro Voice")

# Define path safely
output_dir = "assets/music"
output_path = os.path.join(output_dir, "bloom_intro.mp3")

# Create directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

if st.button("Generate Bloom Intro MP3"):
    bloom_text = (
        "Hi, my name is Bloom. Nice to meet you. "
        "I'm your friend and guide in this beautiful virtual world. "
        "How are you feeling today?"
    )
    tts = gTTS(text=bloom_text, lang='en')
    tts.save(output_path)

    st.success("✅ Bloom intro has been generated!")
    st.audio(output_path)  # Optional: lets you play it right away!

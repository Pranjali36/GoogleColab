import streamlit as st
import time
from PIL import Image
import os
import random
import base64
from gtts import gTTS
from textblob import TextBlob
from streamlit.components.v1 import html
import pygame

# Initialize
st.set_page_config(page_title="Bloom - The Sakura Tree", layout="centered")
st.title("🌸 Bloom: Your Virtual Cherry Blossom Tree")

# Paths
tree_folder = "assets/tree"
music_path = "assets/music/calming_music.mp3"
intro_voice_path = "assets/music/bloom_intro.mp3"

# Load tree stages
tree_images = sorted(
    [img for img in os.listdir(tree_folder) if img.endswith((".jpg", ".png"))]
)

# Load calming music
def play_music(file_path):
    audio_file = open(file_path, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

# Tree animation function
def animate_tree_growth():
    st.subheader("Watch me grow... 🌱🌳🌸")
    for i, img_name in enumerate(tree_images):
        img_path = os.path.join(tree_folder, img_name)
        img = Image.open(img_path)
        st.image(img, caption=f"Stage {i+1}", use_column_width=True)
        time.sleep(6)  # 5 stages x 6 = ~30s
    time.sleep(3)

# Play Bloom's voice intro
def play_bloom_intro():
    st.subheader("🌸 Meet Bloom!")
    audio_file = open(intro_voice_path, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")

# Emotion Menu
def emotion_selector():
    st.subheader("💬 How are you feeling today?")
    emotion = st.radio(
        "Select an emotion:",
        ("Anxious", "Reflective", "Sad", "Excited"),
        index=0,
    )
    if st.button("Submit"):
        st.success(f"Thanks! Transitioning to the {emotion} environment...")
        # You can add environment logic here based on emotion
        show_environment_info(emotion)

def show_environment_info(emotion):
    if emotion == "Anxious":
        st.info("In the beach environment, Bloom helps you relax with waves and breeze.")
    elif emotion == "Reflective":
        st.info("In the forest environment, Bloom offers wisdom and insight.")
    elif emotion == "Sad":
        st.info("In the sky temple, Bloom lifts your spirits with gentle winds.")
    elif emotion == "Excited":
        st.info("In the meadow, Bloom celebrates with you among butterflies.")
    st.balloons()

# Main
if st.button("Start Bloom's Journey"):
    play_music(music_path)
    animate_tree_growth()
    play_bloom_intro()
    emotion_selector()

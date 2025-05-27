import streamlit as st
import time
from PIL import Image
import os

# Set page configuration
st.set_page_config(page_title="Bloom's Tree", layout="centered")

# Paths
tree_folder = "assets/tree"
music_path = "assets/music/calming_music.mp3"
intro_voice_path = "assets/music/bloom_intro.mp3"

# Load tree images
tree_images = sorted(
    [img for img in os.listdir(tree_folder) if img.endswith((".jpg", ".png"))]
)

# Function to play audio
def play_audio(file_path):
    audio_file = open(file_path, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")

# Function to animate tree growth
def animate_tree_growth():
    st.subheader("🌱 Watch the Tree Grow")
    for i, img_name in enumerate(tree_images):
        img_path = os.path.join(tree_folder, img_name)
        img = Image.open(img_path)
        st.image(img, caption=f"Stage {i+1}", use_container_width=True)
        time.sleep(6)
        st.empty()  # Clear the image before showing the next one
    time.sleep(3)

# Function to play Bloom's introduction
def play_bloom_intro():
    st.subheader("🌸 Meet Bloom")
    play_audio(intro_voice_path)

# Function for emotion selection
def emotion_selector():
    st.subheader("💬 How are you feeling today?")
    emotion = st.radio(
        "Select an emotion:",
        ("Anxious", "Reflective", "Sad", "Excited"),
        index=0,
    )
    if st.button("Submit"):
        st.success(f"Thanks! Transitioning to the {emotion} environment...")
        # Add environment logic here based on emotion
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

# Main application
st.title("🌸 Bloom: Your Virtual Cherry Blossom Tree")

if st.button("Start Bloom's Journey"):
    play_audio(music_path)
    animate_tree_growth()
    play_bloom_intro()
    emotion_selector()

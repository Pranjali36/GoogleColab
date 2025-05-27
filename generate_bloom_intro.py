from gtts import gTTS

# Text Bloom will speak
bloom_text = """
Hi there! My name is Bloom. I'm your friend and guide in this magical journey.
I blossomed just for you! 
How are you feeling today?
Please choose one of the following emotions: anxious, reflective, sad or excited.
"""

# Convert to speech
tts = gTTS(text=bloom_text, lang='en')
tts.save("assets/music/bloom_intro.mp3")

print("✅ bloom_intro.mp3 has been created and saved in assets/music/")

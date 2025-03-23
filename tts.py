from gtts import gTTS
import os

def text_to_speech(text, output_file="output.mp3", lang="en"):
    # Convert the text to speech using gTTS
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    print(f"Audio file saved as {output_file}")
    try:
        from playsound import playsound
        playsound(output_file)
    except Exception as e:
        print("Failed to play the audio. Please open output.mp3 manually.", e)

if __name__ == "__main__":
    sample_text = "Hello, this is a text to speech test."
    text_to_speech(sample_text)

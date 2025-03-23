import whisper

def transcribe_audio(audio_path):
    # Load the Whisper model using the "medium" configuration for better accuracy
    model = whisper.load_model("medium")
    # Transcribe the audio file to text
    result = model.transcribe(audio_path)
    return result["text"]

if __name__ == "__main__":
    audio_file = "sample.mp3"  # Please ensure your audio file is named sample.mp3 and is located in this folder
    transcription = transcribe_audio(audio_file)
    print("Transcription result:")
    print(transcription)
    # Save the transcription result to a file
    with open("transcription.txt", "w", encoding="utf-8") as f:
        f.write(transcription)

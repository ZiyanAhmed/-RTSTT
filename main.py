from src.recorder import Recorder
from src.transcriber import Transcriber
import time
import os

def cleanup_data_folder():
    """Remove old audio files to save space."""
    print("Cleaning up old audio files...")
    for file in os.listdir("data"):
        os.remove(os.path.join("data", file))

def main():
    # Initialize Recorder and Transcriber
    recorder = Recorder()
    transcriber = Transcriber()

    # Display available audio input devices
    print("Available Audio Input Devices:")
    recorder.list_input_devices()

    # Set the input device index (adjust based on the list displayed)
    input_device_index = 1  # Example: MacBook Pro Microphone

    print("Starting Real-Time Speech-to-Text. Press Ctrl+C to stop...")

    while True:
        try:
            # Generate unique file name based on timestamp
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            audio_file = f"data/audio_{timestamp}.wav"

            # Record a 5-second audio clip
            recorder.record(duration=11, output_file=audio_file, input_device_index=input_device_index)

            # Transcribe the audio file
            transcription = transcriber.transcribe(audio_file)

            # Log the transcription
            with open("logs/transcriptions.log", "a") as log_file:
                log_file.write(f"[{timestamp}] {transcription}\n")

            print(f"Transcription [{timestamp}]: {transcription}")
        except KeyboardInterrupt:
            print("Stopping Real-Time Speech-to-Text...")
            break

if __name__ == "__main__":
    cleanup_data_folder()
    main()

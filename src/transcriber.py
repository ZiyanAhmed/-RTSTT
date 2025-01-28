import whisper
import os
import logging

# Configure logging for transcription
logging.basicConfig(
    filename="logs/transcriber.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

class Transcriber:
    def __init__(self, model_size="base"):
        """
        Initialize the Whisper model for transcription.
        :param model_size: The size of the Whisper model (e.g., tiny, base, small, medium, large).
        """
        logging.info(f"Loading Whisper model: {model_size}...")
        self.model = whisper.load_model(model_size)
        logging.info("Whisper model loaded successfully.")

    def transcribe(self, audio_file):
        """
        Transcribes the given audio file using Whisper.
        :param audio_file: Path to the audio file to transcribe.
        :return: Transcription text.
        """
        logging.info(f"Starting transcription for {audio_file}...")
        try:
            result = self.model.transcribe(audio_file)
            logging.info(f"Transcription result: {result['text']}")
            return result["text"]
        except Exception as e:
            logging.error(f"Error during transcription: {e}")
            raise

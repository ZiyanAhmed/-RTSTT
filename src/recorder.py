import pyaudio
import wave
import logging

# Configure logging for recording
logging.basicConfig(
    filename="logs/recorder.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

class Recorder:
    def __init__(self, rate=16000, chunk=1024, channels=1, format=pyaudio.paInt16):
        self.rate = rate
        self.chunk = chunk
        self.channels = channels
        self.format = format
        self.audio = pyaudio.PyAudio()
        logging.info("Recorder initialized with default parameters.")

    def list_input_devices(self):
        """Lists all available input devices."""
        for i in range(self.audio.get_device_count()):
            info = self.audio.get_device_info_by_index(i)
            print(f"Device {i}: {info['name']}")

    def record(self, duration=5, output_file="output.wav", input_device_index=None):
        """
        Records audio from the microphone and saves it as a WAV file.
        :param duration: Duration of the recording in seconds.
        :param output_file: Name of the output WAV file.
        :param input_device_index: Index of the input device to use.
        """
        logging.info(f"Starting recording for {duration} seconds...")
        stream = self.audio.open(format=self.format,
                                 channels=self.channels,
                                 rate=self.rate,
                                 input=True,
                                 input_device_index=input_device_index,
                                 frames_per_buffer=self.chunk)
        frames = []

        for _ in range(0, int(self.rate / self.chunk * duration)):
            data = stream.read(self.chunk)
            frames.append(data)

        logging.info("Recording finished. Saving audio to file.")
        stream.stop_stream()
        stream.close()

        # Save the recorded audio to a file
        with wave.open(output_file, "wb") as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.audio.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(frames))
        logging.info(f"Audio saved to {output_file}.")

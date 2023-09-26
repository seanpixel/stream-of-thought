import sounddevice as sd
import numpy as np
import wavio
import threading

# Global variables
RATE = 44100
CHANNELS = 1
DTYPE = np.int16
FILENAME = "audios/audio.wav"
audio_data = np.array([], dtype=DTYPE)
stop_recording_flag = threading.Event()
stream = None

# Callback function to collect data
def callback(indata, frames, time, status):
    global audio_data
    audio_data = np.append(audio_data, indata)

# Start recording function
def start_recording():
    global audio_data, stream, stop_recording_flag
    audio_data = np.array([], dtype=DTYPE)
    stop_recording_flag.clear()

    stream = sd.InputStream(callback=callback, channels=CHANNELS, samplerate=RATE)
    stream.start()
    print("Recording started...")

# Stop recording function
def stop_recording():
    global stream, stop_recording_flag
    if stream is not None:
        stream.stop()
        stream.close()
    stop_recording_flag.set()
    wavio.write(FILENAME, audio_data.reshape(-1, CHANNELS), RATE, sampwidth=2)
    print(f"Recording complete. Audio saved as {FILENAME}")

# Example usage
if __name__ == '__main__':
    print("Press Enter to start recording...")
    input()
    start_recording()

    print("Press Enter to stop recording...")
    input()
    stop_recording()

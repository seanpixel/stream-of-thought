from audio_to_text import get_transcription
from audio_recorder import start_recording, stop_recording
from stream_of_thought import generate_stream_of_thought
from voice_manipulation import clone_voice, stream_audio
from concurrent.futures import ThreadPoolExecutor

audio_dir = "audios/"

print("Welcome to the Stream of Thought Generator!\n\nEnter your name: ")
username = input()

print("Press Enter to start/stop recording your Stream of Thought...")

# Start Recording 
input()
start_recording()

# Stop Recording
input()
stop_recording()

print("Cloning voice...")
clone_voice(username, audio_dir + "audio.wav")
print("Voice Cloned!")

print("Transcribing Audio...")
stream_of_thought = get_transcription(audio_dir + "audio.wav")
print(stream_of_thought)

print("Generating Stream of Thought...")
stream_of_thought = generate_stream_of_thought(stream_of_thought)
print(stream_of_thought)

# Continuously generate stream of thought while streaming audio
while True:
    with ThreadPoolExecutor(max_workers=2) as executor:
        future2 = executor.submit(stream_audio, username, stream_of_thought)
        future1 = executor.submit(generate_stream_of_thought, stream_of_thought)
        stream_of_thought = future1.result()
        
        

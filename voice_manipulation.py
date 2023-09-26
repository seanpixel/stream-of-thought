from elevenlabs import clone, generate, play, stream
import elevenlabs
import os

elevenlabs.set_api_key(os.getenv("ELEVENLABS_API_KEY"))


# generates a voice that can be used to generate audio using an audio file
def clone_voice(username, file_name):
    voice = clone(
        name=username,
        files=[file_name],
    )

    return voice

def stream_audio(voice, text):
    audio = generate(text, voice=voice, stream=True, latency=2)

    stream(audio)
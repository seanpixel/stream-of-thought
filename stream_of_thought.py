from prompts import stream_of_thought_prompt
from generator import generate

# This is the function that will be called to generate the stream of thought
# Only ONE continued stream is generated.
def generate_stream_of_thought(stream_of_thought):
    stream_of_thought = generate(stream_of_thought_prompt.format(stream_of_thought=stream_of_thought))
    return stream_of_thought

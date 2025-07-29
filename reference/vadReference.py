# Voice Activity Detection (VAD) - Automatic
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

config = {
    "response_modalities": ["TEXT"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}

client = genai.Client()
model = "gemini-2.5-flash-live-preview"

config = {"response_modalities": ["TEXT"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

# Disable automatic VAD
# config = {
#     "response_modalities": ["TEXT"],
#     "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
# }

# async with client.aio.live.connect(model=model, config=config) as session:
#     # ...
#     await session.send_realtime_input(activity_start=types.ActivityStart())
#     await session.send_realtime_input(
#         audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
#     )
#     await session.send_realtime_input(activity_end=types.ActivityEnd())
#     # ...

if __name__ == "__main__":
    asyncio.run(main())
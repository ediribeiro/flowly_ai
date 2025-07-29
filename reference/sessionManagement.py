# Context window compression

import asyncio
from google import genai
from google.genai import types


config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)

# Session resumption

client = genai.Client()
model = "gemini-2.5-flash-live-preview"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

# Receiving a message before the session disconnects

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        async for response in session.receive():
            if response.go_away is not None:
                # The connection will soon be terminated
                print(response.go_away.time_left)


# Receiving a message when the generation is complete

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        async for response in session.receive():
            if response.server_content.generation_complete is True:
                # The generation is complete
                break

if __name__ == "__main__":
    asyncio.run(main())
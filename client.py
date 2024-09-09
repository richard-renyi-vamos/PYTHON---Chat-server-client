import asyncio
import websockets

async def chat_client():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        # Start a task to send messages
        async def send_message():
            while True:
                message = input("You: ")
                await websocket.send(message)

        # Start a task to receive messages
        async def receive_message():
            while True:
                message = await websocket.recv()
                print(f"Friend: {message}")

        await asyncio.gather(send_message(), receive_message())

asyncio.get_event_loop().run_until_complete(chat_client())

import asyncio
import websockets

connected_clients = set()

async def chat_server(websocket, path):
    # Add new client to the connected_clients set
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            # Broadcast the message to all connected clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.ConnectionClosed as e:
        print(f"Connection closed: {e}")
    finally:
        # Remove the client from the set when the connection is closed
        connected_clients.remove(websocket)

start_server = websockets.serve(chat_server, "localhost", 6789)

print("Server started on ws://localhost:6789")
# Start the server and run forever
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

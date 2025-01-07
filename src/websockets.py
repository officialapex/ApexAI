import asyncio
import websockets

clients = set()

async def handler(websocket, path):
    """Handles WebSocket connections."""
    clients.add(websocket)
    try:
        async for message in websocket:
            # Echo the message to all clients
            for client in clients:
                await client.send(message)
    finally:
        clients.remove(websocket)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(handler, "localhost", 6789)
    )
    asyncio.get_event_loop().run_forever()

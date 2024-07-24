import asyncio
import websockets
import json

async def game_client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        async def receive_messages():
            async for message in websocket:
                data = json.loads(message)
                if data['action'] == "init":
                    print(f"Your starting position: {data['position']}")
                elif data['action'] == "update":
                    print(f"Opponent's position: {data['position']}")
                elif data['action'] == "win":
                    print(f"Player {data['player']} wins!")
                    return

        async def send_moves():
            while True:
                move = input("Enter move (up, down, left, right): ")
                if move in ["up", "down", "left", "right"]:
                    await websocket.send(json.dumps({"move": move}))

        await asyncio.gather(receive_messages(), send_moves())

if __name__ == "__main__":
    asyncio.run(game_client())
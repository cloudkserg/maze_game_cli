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
                elif data['action'] == "saved":
                    print("Game state saved successfully.")
                elif data['action'] == "restored":
                    print(f"Game state restored. Your position: {data['positions'][0]}, Opponent's position: {data['positions'][1]}")
                elif data['action'] == "no_save":
                    print("No saved game state found.")

        async def send_commands():
            while True:
                command = input("Enter command (move, save, restore): ")
                if command == "save":
                    await websocket.send(json.dumps({"action": "save"}))
                elif command == "restore":
                    await websocket.send(json.dumps({"action": "restore"}))
                elif command in ["up", "down", "left", "right"]:
                    await websocket.send(json.dumps({"action": "move", "move": command}))

        await asyncio.gather(receive_messages(), send_commands())

if __name__ == "__main__":
    asyncio.run(game_client())
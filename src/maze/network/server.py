import asyncio
import websockets
import json

# Game state
GRID_SIZE = 6
positions = [(0, 0), (0, 0)]  # Starting positions of player 1 and player 2
players = []  # List of connected players


async def handler(websocket):
    global players
    players.append(websocket)
    index = len(players) - 1  # Player index (0 or 1)

    try:
        # Send initial state to the new player
        await websocket.send(json.dumps({"action": "init", "position": positions[index]}))
        for other_player in players:
            if other_player != websocket:
                await other_player.send(json.dumps({"action": "update", "position": positions[index]}))

        async for message in websocket:
            data = json.loads(message)
            move = data.get("move")

            # Update game state based on the move
            if move and index < 2:
                x, y = positions[index]
                if move == "up" and y > 0:
                    positions[index] = (x, y - 1)
                elif move == "down" and y < GRID_SIZE - 1:
                    positions[index] = (x, y + 1)
                elif move == "left" and x > 0:
                    positions[index] = (x - 1, y)
                elif move == "right" and x < GRID_SIZE - 1:
                    positions[index] = (x + 1, y)

                # Check win condition
                if positions[index] == (GRID_SIZE - 1, GRID_SIZE - 1):
                    for player in players:
                        await player.send(json.dumps({"action": "win", "player": index}))
                    break

                # Send updated positions to both players
                for player in players:
                    await player.send(json.dumps({"action": "update", "position": positions[index]}))

    finally:
        players.remove(websocket)


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())
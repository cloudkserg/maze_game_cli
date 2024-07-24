import asyncio
import json
import threading
import websockets

# Game state
GRID_SIZE = 6
positions = [(0, 0), (0, 0)]  # Starting positions of player 1 and player 2
players = []  # List of connected players
positions_lock = threading.Lock()  # To prevent race conditions on positions

async def handler(websocket, index):
    global players
    players.append(websocket)

    try:
        # Send initial state to the new player
        await websocket.send(json.dumps({"action": "init", "position": positions[index]}))
        for other_index, other_player in enumerate(players):
            if other_index != index:
                await other_player.send(json.dumps({"action": "update", "position": positions[index]}))

        async for message in websocket:
            data = json.loads(message)
            move = data.get("move")

            if move and index < 2:
                x, y = positions[index]
                new_x, new_y = x, y

                if move == "up" and y > 0:
                    new_y -= 1
                elif move == "down" and y < GRID_SIZE - 1:
                    new_y += 1
                elif move == "left" and x > 0:
                    new_x -= 1
                elif move == "right" and x < GRID_SIZE - 1:
                    new_x += 1

                with positions_lock:
                    # Ensure the new position is valid and not occupied by the other player
                    if (new_x, new_y) != positions[1 - index]:
                        positions[index] = (new_x, new_y)

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
    server = websockets.serve(lambda ws: handler(ws, len(players)), "localhost", 8765)
    async with server:
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
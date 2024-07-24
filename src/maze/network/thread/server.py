import asyncio
import json
import threading
import websockets
from models import Session, GameState, GRID_SIZE

positions = [(0, 0), (0, 0)]  # Starting positions of player 1 and player 2
players = []  # List of connected players
positions_lock = threading.Lock()  # To prevent race conditions on positions


async def handle_message(websocket, index, message):
    data = json.loads(message)
    action = data.get("action")

    if action == "save":
        with positions_lock:
            session = Session()
            game_state = GameState(
                player1_x=positions[0][0], player1_y=positions[0][1],
                player2_x=positions[1][0], player2_y=positions[1][1]
            )
            session.add(game_state)
            session.commit()
            session.close()
            await websocket.send(json.dumps({"action": "saved"}))

    elif action == "restore":
        session = Session()
        game_state = session.query(GameState).order_by(GameState.id.desc()).first()
        if game_state:
            positions[0] = (game_state.player1_x, game_state.player1_y)
            positions[1] = (game_state.player2_x, game_state.player2_y)
            await websocket.send(json.dumps({"action": "restored", "positions": positions}))
        else:
            await websocket.send(json.dumps({"action": "no_save"}))
        session.close()

    elif action == "move":
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
                if (new_x, new_y) != positions[1 - index]:
                    positions[index] = (new_x, new_y)

                    if positions[index] == (GRID_SIZE - 1, GRID_SIZE - 1):
                        for player in players:
                            await player.send(json.dumps({"action": "win", "player": index}))
                        return

                    for player in players:
                        await player.send(json.dumps({"action": "update", "position": positions[index]}))


async def handler(websocket):
    global players
    index = len(players)
    players.append(websocket)

    try:
        await websocket.send(json.dumps({"action": "init", "position": positions[index]}))
        for other_index, other_player in enumerate(players):
            if other_index != index:
                await other_player.send(json.dumps({"action": "update", "position": positions[index]}))

        async for message in websocket:
            await handle_message(websocket, index, message)

    finally:
        players.remove(websocket)


async def main():
    server = websockets.serve(handler, "localhost", 8765)
    async with server:
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())
import random
import websockets
import asyncio
import logging

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def first_clicked():
    return random.randint(0,1)


b1 = board[0:0]
...
b9 = board[2:2]


def button_click(self):
    pass


def win():
    pass

def swap_first_clicked():
    pass


#websoket logic


async def handler(websocket, path):
    data = await websocket.recv()
    reply = f"Data recieved as:  {data}!"
    await websocket.send(reply)


start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()


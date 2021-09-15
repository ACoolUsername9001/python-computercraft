from dataclasses import dataclass, field
from typing import TypeVar
import websocket
from io import IOBase
import json

WebSocket = TypeVar('WebSocket')


class ComputerCraftException(Exception):
    pass


@dataclass
class CCWebsocketWriter(IOBase):
    url: str
    c_id: str
    c_pass: str
    websocket: WebSocket = field(default_factory=lambda: websocket.WebSocket())

    def connect(self):
        self.websocket.connect(self.url)
        self.websocket.send(self.c_id)
        self.websocket.send(self.c_pass)

    def write(self, data, write=True):
        if write:
            self.websocket.send(data)
            res = self.websocket.recv()

            try:
                res = json.loads(res)
            except json.decoder.JSONDecodeError:
                raise ComputerCraftException(res)

            return res
        else:
            return data

    def disconnect(self):
        self.websocket.close()

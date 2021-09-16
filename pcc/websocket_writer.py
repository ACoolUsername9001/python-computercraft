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
                res = ReturnValue(self, json.loads(res))
            except json.decoder.JSONDecodeError:
                raise ComputerCraftException(res)

            return res
        else:
            return data

    def disconnect(self):
        self.websocket.close()


class ReturnValue(list):
    def __init__(self, writer, *args, **kwargs):
        super(ReturnValue, self).__init__(*args, **kwargs)
        self.writer = writer


    def __getattr__(self, item):
        return self.writer.write(f'returned[1].{item}')
    
    def __call__(self, *args):
        return self.writer.write(f'returned[1]({",".join((str(x) for x in args))})')

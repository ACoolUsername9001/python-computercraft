from pcc.websocket_writer import CCWebsocketWriter
from pcc.cc_objects import Turtle


def dig_move(turtle, direction):
    if direction == 'down':
        if not turtle.down()[0]:
            turtle.digDown()
            turtle.down()
    elif direction == 'up':
        if not turtle.up()[0]:
            turtle.digUp()
            turtle.up()
    elif direction == 'forward':
        if not turtle.forward()[0]:
            turtle.dig()
            turtle.forward()


def dig_sipral(turtle, steps):
    for _ in range(steps):
        turtle.turnLeft()
        dig_move(turtle, 'forward')
        turtle.digUp()
        dig_move(turtle, 'down')

if __name__ == '__main__':
    writer = CCWebsocketWriter('ws://acooldomain.co:50806/admin/ws', '12', 'ACoolPassword1')
    writer.connect()
    turtle = Turtle(writer)
    dig_sipral(turtle, 30)
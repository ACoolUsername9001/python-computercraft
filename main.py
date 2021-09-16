from pcc.websocket_writer import CCWebsocketWriter
from pcc.cc_objects import Turtle
class AdvancedTurtle(Turtle):
    
    def dig_move(self, direction, ammount=1):
        for i in range(ammount):
            if direction == 'down':
                if not self.down()[0]:
                    self.digDown()
                    self.down()
            elif direction == 'up':
                if not self.up()[0]:
                    self.digUp()
                    self.up()
            elif direction == 'forward':
                if not self.forward()[0]:
                    self.dig()
                    self.forward()
        if direction == 'left':
            self.turnLeft()
            self.dig_move('forward', ammount)
            self.turnRight()
        elif direction == 'right':
            self.turnRight()
            self.dig_move('forward', ammount)
            self.turnLeft()

    def get_inventory(self):
        return [self.getItemDetails(i)[0] for i in range(1, 17)]

    def has_item_in_inventory(item_name) -> int:
        return any(map(lambda x: x[]))

    def dig_sipral(self, steps):
        for _ in range(steps):
            self.turnLeft()
            self.dig_move('forward')
            self.digUp()
            self.dig_move('down')
            if not self.detectDown():
                pass
                

    def dig_wall(self, hight, length, init_horiz='left', vertical='up', return_to_start=True):
        anti_horiz = 'right' if init_horiz == 'left' else 'left'
        anti_vertical = 'down' if vertical == 'up' else 'up'

        for i in range(hight):
            self.dig_move(init_horiz, length)
            self.dig_move(vertical, 1)
            init_horiz, anti_horiz = anti_horiz, init_horiz

        if return_to_start:
            self.dig_move(init_horiz, length)
            self.dig_move(anti_vertical, hight)

    def dig_room(self, hight, length, depth, init_horiz='left', init_vertical='up', return_to_start=True):
        for i in range(depth):
            self.dig_wall(hight, length, init_horiz, init_vertical, False)
            self.dig_move('forward')
            init_horiz = 'right' if init_horiz == 'left' else 'left'
            init_vertical = 'down' if init_vertical == 'up' else 'up'

        if return_to_start:
            self.dig_move(init_vertical, hight)
            self.dig_move(init_horiz, length)
            self.dig_move('back', depth)

if __name__ == '__main__':
    writer = CCWebsocketWriter('ws://acooldomain.co:50806/admin/ws', '12', 'ACoolPassword1')
    writer.connect()
    turtle = AdvancedTurtle(writer)
    # turtle.dig_sipral(30)
    # turtle.dig_room(5, 5, 5)
    # [dig_move(self, 'up') for _ in range(2)]
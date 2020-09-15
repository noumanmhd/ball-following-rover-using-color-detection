
class Rover(object):
    def __init__(self):
        pass

    def stop(self):
        print("stop")

    def forward(self):
        print("forward")

    def backward(self):
        print("back")

    def left(self):
        print("left")

    def right(self):
        print("right")

    def control(self, cmd):
        try:
            if cmd == 'forward':
                self.forward()
            elif cmd == 'back':
                self.backward()
            elif cmd == 'right':
                self.right()
            elif cmd == 'left':
                self.left()
            else:
                self.stop()
        except:
            print('Error')

    def close(self):
        pass

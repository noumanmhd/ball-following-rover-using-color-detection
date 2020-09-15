import serial

class Rover(object):
    def __init__(self,port='/dev/ttyUSB0'):
        self.ser = serial.Serial(port)
        print(self.ser.name)

    def stop(self):
        self.ser.write(b'stop\n')
        print("stop")
        
    def forward(self):
        self.ser.write(b'forward\n')
        print("forward")
        
    def backward(self):
        self.ser.write(b'back\n')
        print("back")
        
    def left(self):
        self.ser.write(b'left\n')
        print("left")

    def right(self):
        self.ser.write(b'right\n')
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
            print('Serial Port ERROR!!!')

    def close(self):
        self.ser.close()


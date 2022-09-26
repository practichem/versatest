import serial
class versatest():

    def __init__(self, port, speed) -> None:
         self.port = port
         self.speed = speed
         self.connection = self.open_channel(port, speed)

    def open_channel(self, port, speed):
        return serial.Serial(port, speed, timeout = 0.5, write_timeout = 0.5)

    def send_bytes(self, command):
        self.connection.write(command)
    
    def receive_bytes(self, number_of_bytes):
        return self.connection.read(1)

    def make_packet(self, command, parameter):
        packet = bytearray()
        packet.append(command)
        packet.append(parameter)
        return packet

    def percent_to_8bit(self, percent):
        '''Converts a percentage (0.0 to 100.0%) to an 8 bit bytearray.'''
        if (percent > 0.0) & (percent <= 100.0): 
            eightBitPercent = round(percent * 2.55)
            return eightBitPercent        
        else:
            return 0

    def set_speed(self, dir, speed):  # Sets the speed. Dir is up or down. 0xFF = 100%
        command = 0
        parameter = self.percent_to_8bit(speed)
        if dir == 'up':
            command = 0x1
        elif dir == 'down':
            command = 0x2
        return self.make_packet(command, parameter)

    def set_mode(self, mode):
        command = 0
        if mode == 'manual':
            command = 0x80
        elif mode == 'single_cycle':
            command = 0x81
        elif mode == 'cont_cycle':
            command = 0x82
        return command.to_bytes(1,'big')

    def set_go(self, mode):          # Simulates the up/down switch: neutral, up, down
        command = 0
        if mode == 'off':
            command = 0x90
        elif mode == 'up':
            command = 0x91
        elif mode == 'down':
            command = 0x92
        message = command.to_bytes(1,'big')
        self.send_bytes(message)

    def set_limit(self, mode):       # Simulates the travel limit switch set: open, up_limit, down_limit
        command = 0
        if mode == 'open':
            command = 0xa0
        elif mode == 'up_limit':
            command = 0xa1
        elif mode == 'down_limit':
            command = 0xa2
        return command.to_bytes(1,'big')

    def set_control(self, mode):        # Sets the control mode: remote, local. In 'local', all commands are ignored except 'remote'
        command = 0
        if mode == 'remote':
            command = 0xf2
        elif mode == 'local':
            command = 0xf3
        return command.to_bytes(1,'big')
        
    def get_switches_status(self):
        # Returns simulated switch status.
            command = 0xe0
            # Send command to port.
            # Interpret response from port.
            # Create object containing interpreted responses.
            return command

    def get_up_speed_setpoint(self):            # Returns set speed for up.
            command = 0xE1
            return command

    def get_down_speed_setpoint(self):          # Returns set speed for down.
            command = 0xE2
            return command

    def get_run_state(self):
            command = 0xE8
            return command        

    def get_run_speed(self):
            command = 0xE9
            self.send_bytes(command)
            response = self.receive_bytes(1)
            print(len(response))

    def get_version(self):
            command = 0xEF
            self.send_bytes(command)
            response = self.receive_bytes(1)
            print(len(response))

    # https://stackoverflow.com/questions/17553543/pyserial-non-blocking-read-loop/38758773

my_versatest = versatest("COM5", 9600)
result = my_versatest.get_run_speed()
print(result)
#my_versatest.set_go("off")


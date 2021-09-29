import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

print(ser.name)         # check which port was really used
ser.write(b'0xf2')     # write a string
ser.close()             # close port

def percent_to_8bit(percent):
    '''Converts a percentage (0.0 to 100.0%) to an 8 bit bytearray.'''
    if (percent > 0.0) & (percent <= 100.0): 
        eightBitPercent = round(percent * 2.55)
        return eightBitPercent        
    else:
        return 0

def makePacket(command, parameter):
    packet = bytearray()
    packet.append(command)
    packet.append(parameter)
    return packet

def set_speed(dir, speed):  # Sets the speed. Dir is up or down. 0xFF = 100%
    command = 0
    parameter = percent_to_8bit(speed)
    if dir == 'up':
        command = 0x1
    elif dir == 'down':
        command = 0x2
    return makePacket(command, parameter)

def set_mode(mode):
    command = 0
    if mode == 'manual':
        command = 0x80
    elif mode == 'single_cycle':
        command = 0x81
    elif mode == 'cont_cycle':
        command = 0x82
    return command.to_bytes(1,'big')

def set_go(mode):          # Simulates the up/down switch: neutral, up, down
    command = 0
    if mode == 'neutral':
        command = 0x90
    elif mode == 'up':
        command = 0x91
    elif mode == 'down':
        command = 0x92
    return command.to_bytes(1,'big')

def set_limit(mode):       # Simulates the travel limit switch set: open, up_limit, down_limit
    command = 0
    if mode == 'open':
        command = 0xa0
    elif mode == 'up_limit':
        command = 0xa1
    elif mode == 'down_limit':
        command = 0xa2
    return command.to_bytes(1,'big')

def set_control(mode):        # Sets the control mode: remote, local. In 'local', all commands are ignored except 'remote'
    command = 0
    if mode == 'remote':
        command = 0xf2
    elif mode == 'local':
        command = 0xf3
    return command.to_bytes(1,'big')
    
def get_switches_status():
    # Returns simulated switch status.
        command = 0xe0
        # Send command to port.
        # Interpret response from port.
        # Create object containing interpreted responses.
        return command

def get_up_speed_setpoint():            # Returns set speed for up.
        command = 0xe1
        return command

def get_down_speed_setpoint():          # Returns set speed for down.
        command = 0xe2
        return command

def get_run_state():
        command = 0xe8
        return command        

def get_run_speed():
        command = 0xe9
        return command

def get_version():
        command = 0xEF
        return command


# https://stackoverflow.com/questions/17553543/pyserial-non-blocking-read-loop/38758773




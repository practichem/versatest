import serial
import time


ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

print('Port:', ser.name)  # Print the name of the port
# ser.close()             # close port

def percent_to_8bit(percent):
    '''Converts a percentage (0.0 to 100.0%) to an 8 bit bytearray.'''
    if (percent > 0.0) & (percent <= 100.0): 
        eightBitPercent = round(percent * 2.55)
        return eightBitPercent        
    else:
        return 0

def byte_to_percent(value):
    return round(int.from_bytes(value,'big') / 2.55)

def byte_to_int(value):
    return int.from_bytes(value, 'big')

def send_command(command):
    ser.write(command.to_bytes(1,'big'))
    # print("wrote command", ser.write(command.to_bytes(1, 'big')), "bytes")
    time.sleep(0.01)

def send_parameter(parameter):
    ser.write(parameter.to_bytes(1, 'big'))
    #print("wrote parameter", ser.write(parameter.to_bytes(1, 'big')), "bytes")
    time.sleep(0.01)

def read_response(bytes):
    response = ser.read(bytes)
    return response

def makePacket(command, parameter):
    packet = bytearray()
    packet.append(command)
    packet.append(parameter)
    return packet

def set_speed(dir, speed):  # Sets the speed. Dir is up or down. 0xFF = 100%
    command = {
        'up': 0x1,
        'down': 0x2
    }
    parameter = percent_to_8bit(speed)
    send_command(command[dir])
    send_parameter(parameter)

def set_mode(mode):
    command = {
        'manual': 0x80,
        'single': 0x81,
        'continuous': 0x82
    }
    send_command(command[mode])

def set_go(mode):          # Simulates the up/down switch: neutral, up, down
    command = {
        'neutral': 0x90,
        'up': 0x91,
        'down': 0x92
    }
    send_command(command[mode])

def set_limit(mode):       # Simulates the travel limit switch set: open, up_limit, down_limit
    command = {
        'open': 0xa0,
        'up_limit': 0xa1,
        'down_limit': 0xa2
    }
    send_command(command[mode])

def set_control(mode):        # Sets the control mode: remote, local. In 'local', all commands are ignored except 'remote'
    command = {
        'remote': 0xf2,
        'local': 0xf3
    }
    send_command(command[mode])

def reset():
    send_command(0xff)
    
def get_switches_status():
    # Returns simulated switch status.
        command = 0xe0
        # Send command to port.
        # Interpret response from port.
        # Create object containing interpreted responses.
        send_command(command)
        response = read_response(1)

def get_up_speed_setpoint():            # Returns set speed for up.
        command = 0xe1
        send_command(command)
        response = read_response(1)
        return byte_to_percent(response)

def get_down_speed_setpoint():          # Returns set speed for down.
        command = 0xe2
        send_command(command)
        response = read_response(1)
        return byte_to_percent(response)

def get_run_state():
    '''Returns run state as tuple'''
    command = 0xe8
    runState = {
        0: 'idle',
        1: 'running up',
        2: 'running down'
    }
    send_command(command)
    response = byte_to_int(read_response(1))
    return (response, runState[response])
    
def get_run_speed():
    '''Returns the current running speed in percent as int.'''
    command = 0xe9
    send_command(command)
    response = read_response(1)
    return byte_to_percent(response)

def get_version():
    '''Returns the firmware version as int.'''
    command = 0xEF
    send_command(command)
    response = read_response(1)
    return byte_to_int(response)


# https://stackoverflow.com/questions/17553543/pyserial-non-blocking-read-loop/38758773


#reset()
#time.sleep(0.5)
set_control("remote")
set_speed("down", 10)
set_speed("up", 25)
# set_mode("continuous_cycle")
# set_mode("single_cycle")
set_mode("manual")
set_go("up")
get_up_speed_setpoint()
get_down_speed_setpoint()
print("Version:", get_version())
print('Run speed:', get_run_speed())
print('Run state:', get_run_state())
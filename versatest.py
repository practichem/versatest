def percent_to_8bit(percent):
    '''Converts a percentage (0.0 to 100.0%) to an 8-bit bytearray.'''
    if 0.0 <= percent <= 100.0:
        eight_bit_percent = round(percent * 2.55)
        return eight_bit_percent
    return 0

def make_packet(command, parameter):
    return bytearray([command, parameter])

def set_speed(direction, speed):
    # Sets the speed. Direction is 'up' or 'down'. 0xFF = 100%
    command = 0
    parameter = percent_to_8bit(speed)
    
    if direction == 'up':
        command = 0x1
    elif direction == 'down':
        command = 0x2
    
    return make_packet(command, parameter)

def set_mode(mode):
    command = 0
    
    mode_mapping = {
        'manual': 0x80,
        'single_cycle': 0x81,
        'cont_cycle': 0x82
    }
    
    return mode_mapping.get(mode, 0).to_bytes(1, 'big')

def set_go(mode):
    command = 0
    
    mode_mapping = {
        'neutral': 0x90,
        'up': 0x91,
        'down': 0x92
    }
    
    return mode_mapping.get(mode, 0).to_bytes(1, 'big')

def set_limit(mode):
    command = 0
    
    mode_mapping = {
        'open': 0xa0,
        'up_limit': 0xa1,
        'down_limit': 0xa2
    }
    
    return mode_mapping.get(mode, 0).to_bytes(1, 'big')

def set_control(mode):
    command = 0
    
    mode_mapping = {
        'remote': 0xf2,
        'local': 0xf3
    }
    
    return mode_mapping.get(mode, 0).to_bytes(1, 'big')

def get_switches_status():
    # Returns simulated switch status.
    return 0xe0.to_bytes(1, 'big')

def get_up_speed_setpoint():
    # Returns set speed for up.
    return 0xe1.to_bytes(1, 'big')

def get_down_speed_setpoint():
    # Returns set speed for down.
    return 0xe2.to_bytes(1, 'big')

def get_run_state():
    return 0xe8.to_bytes(1, 'big')

def get_run_speed():
    return 0xe9.to_bytes(1, 'big')

def get_version():
    return 0xEF.to_bytes(1, 'big')

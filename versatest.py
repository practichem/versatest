class VersaTest:
    def __init__(self):
        self.command = 0
        self.parameter = 0

    def set_speed(self, direction, speed):
        # Sets the speed. Direction is 'up' or 'down'. 0xFF = 100%
        self.command = 0
        self.parameter = percent_to_8bit(speed)

        if direction == 'up':
            self.command = 0x1
        elif direction == 'down':
            self.command = 0x2

    def set_mode(self, mode):
        mode_mapping = {
            'manual': 0x80,
            'single_cycle': 0x81,
            'cont_cycle': 0x82
        }
        self.command = mode_mapping.get(mode, 0)

    def set_go(self, mode):
        mode_mapping = {
            'neutral': 0x90,
            'up': 0x91,
            'down': 0x92
        }
        self.command = mode_mapping.get(mode, 0)

    def set_limit(self, mode):
        mode_mapping = {
            'open': 0xa0,
            'up_limit': 0xa1,
            'down_limit': 0xa2
        }
        self.command = mode_mapping.get(mode, 0)

    def set_control(self, mode):
        mode_mapping = {
            'remote': 0xf2,
            'local': 0xf3
        }
        self.command = mode_mapping.get(mode, 0)

    def get_switches_status(self):
        return self.command.to_bytes(1, 'big')

    def get_up_speed_setpoint(self):
        return self.command.to_bytes(1, 'big')

    def get_down_speed_setpoint(self):
        return self.command.to_bytes(1, 'big')

    def get_run_state(self):
        return self.command.to_bytes(1, 'big')

    def get_run_speed(self):
        return self.command.to_bytes(1, 'big')

    def get_version(self):
        return self.command.to_bytes(1, 'big')

    def percent_to_8bit(self, percent):
        '''Converts a percentage (0.0 to 100.0%) to an 8-bit bytearray.'''
        if 0.0 <= percent <= 100.0:
            return round(percent * 2.55)
        return 0

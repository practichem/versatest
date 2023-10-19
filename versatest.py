class VersaTest:
    def __init__(self):
        self.command = 0
        self.parameter = 0

    def _percent_to_8bit(self, percent):
        '''Converts a percentage (0.0 to 100.0%) to an 8-bit bytearray.'''
        if 0.0 <= percent <= 100.0:
            return round(percent * 2.55)
        return 0
    
    @speed.setter
    def speed(self, new_speed):
        if new_speed < 0.0 or new_speed > 100.0:
            raise ValueError("Speed must be between 0.0 and 100.0")
        self._speed = new_speed
        self.command = 0

    @mode.setter
    def mode(self, new_mode):
        mode_mapping = {
            'manual': 0x80,
            'single_cycle': 0x81,
            'cont_cycle': 0x82
        }

        if new_mode not in mode_mapping:
            raise ValueError("Invalid mode")

        self._mode = new_mode
        self.command = mode_mapping[new_mode]

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



class VersaTest:
    def __init__(self):
        self._command = 0
        self._parameter = 0
        self._speed = 0.0  # Initialize speed
        self._mode = 'manual'  # Initialize mode with a default value

    @staticmethod
    def _percent_to_8bit(percent):
        '''Converts a percentage (0.0 to 100.0%) to an 8-bit value.'''
        return round(min(max(percent, 0.0), 100.0) * 2.55)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if not 0.0 <= new_speed <= 100.0:
            raise ValueError("Speed must be between 0.0 and 100.0")
        self._speed = new_speed

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new_mode):
        mode_mapping = {'manual': 0x80, 'single_cycle': 0x81, 'cont_cycle': 0x82}
        if new_mode not in mode_mapping:
            raise ValueError("Invalid mode")
        self._mode = new_mode
        self._command = mode_mapping[new_mode]

    def set_command(self, command_category, mode):
        mode_mapping = {
            'go': {'neutral': 0x90, 'up': 0x91, 'down': 0x92},
            'limit': {'open': 0xa0, 'up_limit': 0xa1, 'down_limit': 0xa2},
            'control': {'remote': 0xf2, 'local': 0xf3}
        }
        category_mapping = mode_mapping.get(command_category, {})
        self._command = category_mapping.get(mode, 0)

    def get_status_bytes(self, attribute_name):
        """Get byte representation of various statuses, based on the attribute's current value."""
        attribute_value = getattr(self, attribute_name, None)

        # Example of how you might handle different attribute types
        if attribute_name in ['_command', '_parameter']:
            # These are already integers, so we can directly convert them
            return attribute_value.to_bytes(1, 'big')
        elif attribute_name == '_speed':
            # Convert speed percentage to an 8-bit value
            return self._percent_to_8bit(attribute_value).to_bytes(1, 'big')
        elif attribute_name == '_mode':
            # Convert mode to its corresponding command byte value
            mode_mapping = {'manual': 0x80, 'single_cycle': 0x81, 'cont_cycle': 0x82}
            mode_value = mode_mapping.get(attribute_value, 0)
            return mode_value.to_bytes(1, 'big')
        else:
            # Default case or attribute not found
            return b'\x00'


# Example usage:
# versatest = VersaTest()
# versatest._speed = 50.0  # Setting some values for demonstration
# versatest._mode = 'single_cycle'
# versatest._command = 128  # An example command value

# print(versatest.get_status_bytes('_command'))  # Example command byte
# print(versatest.get_status_bytes('_speed'))    # Speed as a byte
# print(versatest.get_status_bytes('_mode'))     # Mode as a command byte





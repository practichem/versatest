# Mecmesin VersaTest force test stand commands
Note inter-byte delay implemented in code.


| Function  |  Command  |  Returned bytes  |  Description  |  Note  |
|--|--|--|--|--|
|set_speed_up|	    0x01h|	1|	Sets the up speed. | Ø..255 = 1%..1ØØ%	|
|set_speed_dn	    |0x02h|	1|	Sets the down speed.|	
|set_mode_manual	    |0x80h	|0	|Sets the stand in manual mode|	
|set_mode_cycle	|    0x81h	|0	|Sets the stand in cycle mode.	|
|set_mode_once	   | 0x82h	|0	|Sets the stand in once mode.	|
|set_go_off|	        0x90h|	0|	Maintains the up/down switch in the center position.	|
|set_go_up	|        0x91h	|0|	Maintains the up/down switch in the up position.	|Follow this command with a center command.|
|set_go_down|	        0x92h	|0	|Maintains the up/down switch in the down position.	|Follow this command with a center command.|
|set_ls_normal	    |0xA0h|	0|	Maintains the limit switch in the non-limited position.	|
|set_ls_up          |0xA1h|	0|	Maintains the limit switch in the up limited position.	|
|set_ls_dn	        |0xA2h|	0|	Maintains the limit switch in the down limited position.	|
|get_mdgols	        |0xE0h|	1|	Requests a byte comprising mimicked switch status 00MDGOLS|	
|get_up_speed|	        0xE1h|	1|	Requests the set up speed. |Returns a byte value percentage.	
|get_dn_speed	        |0xE2h|	1|	Requests the set down speed. |Returns a byte value percentage.|	
|get_motor_run	   | 0xE8h|	1|	Returns the current motor run status (TODO: ???)|	
|get_motor_speed	|    0xE9h	|1|	Returns the actual motor speed.| Returns a byte value percentage	|
|get_version 	   | 0xEFh|	1|	Returns the firmware version.|	
|set_mode_remote     |0xF2h|	0|	Sets remote mode, listens to serial port commands, and disables front panel.	
|set_mode_local|      0xF3h	|0|	Sets local mode, responds to front panel commands, disables serial commands except 'remote'	In local mode, settings will persist in memory, but the stand will not react until put in remote mode.
|reset|   	        0xFFh|	0|	Resets the controller|

# MDGOLS
	MD (mode)       00 = manual; 01 = cycle; 10 = once	
	GO (go)         00 = center; 01 = up; 10 = down	
	LS (limits)     00 = normal; 01 = up limit; 10 = down limit|	

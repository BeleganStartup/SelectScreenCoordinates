import win32api
from pynput.mouse import Button, Controller as Mouse_Controller


def select_area():
	global box_size
	count = 0
	mouse = Mouse_Controller()  # Mouse obj
	state_left = win32api.GetKeyState(0x01)
	while True:

		buttons_clicked = win32api.GetKeyState(0x01)
		if buttons_clicked != state_left:  # Button state changed
			state_left = buttons_clicked
			if buttons_clicked < 0:
				x1,y1 = mouse.position
			else:
				x2, y2 = mouse.position
				box_size = (x1,y1,x2,y2)
				print(box_size)
				break

select_area()
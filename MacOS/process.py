import bluetooth
import image

import time

size = 90
offset = 15

renderer = image.Renderer(size)

hc05 = bluetooth.MySerial("/dev/tty.HC-05-DevB")

hc05.setDebugLevel("error")
hc05.connect()

hc05.write("s")
time.sleep(1)

while True:
	data = hc05.read()
	if data == "":
		break
	else:
		print ('%s' % data)
		try:
			parsedData = [int(a) for a in data.split(",")]
			parsedData[0] -= (90 - (size/2))
			parsedData[1] -= (90 - (size/2))
			if parsedData[1] % 2:
				parsedData[0] += offset
			if parsedData[0] >= size or parsedData[1] >= size:
				continue
			renderer.setData(parsedData[0], parsedData[1], parsedData[2])
			renderer.render()
		except:
			continue

renderer.finalShow()

# TO DO LIST
# make the resolution a param that can be set from bt command
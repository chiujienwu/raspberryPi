from picamera import PiCamera
from time import sleep
from gpiozero import Button
from datetime import datetime

button = Button(7)
camera = PiCamera()

frame = 1
while True:
    try:
        button.wait_for_press()
        camera.start_preview()
        sleep(2)
        camera.annotate_text_size = 60 # (values 6 to 160, default is 32)
        camera.annotate_text = datetime.now().strftime('%A %d %b %Y %H:%M')
        camera.capture('/home/pi/Pictures/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break

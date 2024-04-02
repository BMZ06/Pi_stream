from time import sleep
from picamera import PiCamera

i = 0
while i<10
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()
# Camera warm-up time
sleep(10)
camera.stop_preview()
sleep(10)
i=i+1
end

import scrollphathd as sphd
import time

sphd.set_brightness(0.5)
sphd.rotate(degrees= 180)
    
sphd.write_string('Shiver me timbers!')

while True:
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.05)

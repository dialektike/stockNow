import scrollphathd as sphd
from scrollphathd.fonts import font5x7
import time

sphd.set_brightness(0.5)
sphd.rotate(degrees= 180)
    
sphd.write_string('Shiver me timbers!', font=font5x7)

while True:
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.1)

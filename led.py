from gpiozero import LED
import time

G = LED(18)
R= LED(12)
Y= LED(13)

G.on()
time.sleep(10)
G.off()
Y.on()
time.sleep(5)
Y.off
R.on()
time.sleep(10)
R.off()
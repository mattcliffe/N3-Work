from usbiss.spi import SPI
import time
import matplotlib.pyplot as plt
spi.close()
port ='COM60'
spi = SPI(port)
spi.mode = 1
hz =  300000
spi.max_speed_hz = hz

#spi.open()

senddata = [0x03]
y = []
try:
    while True:
        
        x = spi.xfer2(senddata)
        
        print(x)
        y.append(x)
        plt.scatter(len(y),x)
        time.sleep(1)
        plt.draw()
except KeyboardInterrupt:
    print('interrupted!')

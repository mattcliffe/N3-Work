from usbiss.spi import SPI
import time
import matplotlib.pyplot as plt
def OpenOPC():
    port ='COM6'
    spi = SPI(port)
    spi.mode = 1
    hz =  300000
    spi.max_speed_hz = hz
    
    senddata = [0x03]
    x = spi.xfer(senddata)
    print(x)

def CloseOPC():
    spi.close()
    
def SetFanSpeed(Speed):
    
    x = senddata=[0x42,0x42,0x42,0x00,speed]
    y = spi.xfer([0x13,0x13,0x13,0x13,0x13,0x13,0x13,0x13,0x13])
    return x,y



    
#OpenOPC()
loop = 1
try:
    while True:
        Speed = input("Input fan speed in HEX") 
        x,y=SetFanSpeed(Speed)
        print(x)
        print(y)
        print(Speed)
        time.sleep(2)
        
except KeyboardInterrupt:
    CloseOPC()
    pass

from esp8266_i2c_lcd import I2cLcd
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
#i2c.scan()
lcd = I2cLcd(i2c,63, 2, 16)
lcd.clear()
lcd.putstr("Ready!")
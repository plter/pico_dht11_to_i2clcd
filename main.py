from machine import Pin, ADC, I2C
import time
from DHT22 import DHT22
import utime
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
DHT11_PIN    = 15


if __name__ == "__main__":
    
    i2c = I2C(0)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    lcd.backlight_off()
    
    dht_data = Pin(DHT11_PIN,Pin.IN,Pin.PULL_UP)
    dht_sensor=DHT22(dht_data,dht11=True)
    while True:
        T,H = dht_sensor.read()
        if T is None:
            # print(" sensor error")
            pass
        else:
            lcd.clear()
            lcd.putstr("{:3.1f}'C  {:3.1f}%".format(T,H))
        #DHT22 not responsive if delay to short
        utime.sleep_ms(1000)
        

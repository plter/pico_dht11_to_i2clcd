from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from DHT22 import DHT22
import utime

DHT11_PIN = 22

OLED_WIDTH  = 128
OLED_HEIGHT = 32

sda=machine.Pin(4)
scl=machine.Pin(5)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)


from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)


if __name__ == "__main__":
    dht_data = Pin(DHT11_PIN,Pin.IN,Pin.PULL_UP)
    dht_sensor=DHT22(dht_data,dht11=True)
    while True:
        temperature,humidity = dht_sensor.read()
        if temperature is None or humidity is None:
            # skip errors
            pass
        else:
            oled.fill(0)
            oled.text(f"T: {temperature}'C",0,0)
            oled.text(f"H: {humidity}%",0,15)
            oled.show()
        
        utime.sleep(2)

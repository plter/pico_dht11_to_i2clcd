import machine
import time
from pico_i2c_lcd import I2cLcd

sensor_temp = machine.ADC(4)
conversion_factor = 3.3/(65536)


I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
DHT11_PIN    = 15

if __name__ == "__main__":
    i2c = machine.I2C(0)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

    while True:
        reading = sensor_temp.read_u16()*conversion_factor
        t = 27 - (reading - 0.706)/0.001721
        time.sleep(1)
        lcd.move_to(0,0)
        lcd.putstr("{:3.2f} 'C      ".format(t))
        print("temperature:", t)

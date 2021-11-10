import machine,uasyncio
import time
from pico_i2c_lcd import I2cLcd

sensor_temp = machine.ADC(4)
conversion_factor = 3.3/(65536)


I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
DHT11_PIN    = 15

def format_time(input):
    return f'{("" if input>=10 else "0")}{input}'

async def main():
    i2c = machine.I2C(0)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

    while True:
        reading = sensor_temp.read_u16()*conversion_factor
        t = 27 - (reading - 0.706)/0.001721
        lcd.move_to(0,0)
        lcd.putstr("{:3.2f} 'C      ".format(t))
        current_time = time.localtime()
        lcd.move_to(0,1)
        lcd.putstr(f"{format_time(current_time[3])}:{format_time(current_time[4])} {current_time[0]}-{format_time(current_time[1])}-{format_time(current_time[2])}")
        await uasyncio.sleep(1)

if __name__ == "__main__":
    uasyncio.run(main())

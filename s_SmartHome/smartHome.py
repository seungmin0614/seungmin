from machine import ADC, Pin, PWM, SoftI2C
from time import sleep
from servo import Servo

import dht
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

import ble_library
import bluetooth

import ssd1306
import framebuf

# 조도 센서 연결 핀
cds = ADC(Pin(36))
cds.atten(ADC.ATTN_11DB)

cds_flag = 0

# 서보 모터 연결 핀
motor = Servo(pin=13)

# 피에조 부저 연결
speaker = PWM(Pin(23))
speaker.duty_u16(0)

# 피에조 부저 멜로디
blindMelody = (523, 1046, 2093)
melody1 = (784, 784, 880, 880, 784, 784, 659)
melody2 = (523, 523, 784, 784, 880, 880, 784)

# LED 전등 연결 핀 
LEDR = Pin(25, Pin.OUT)
LEDG = Pin(26, Pin.OUT)
LEDB = Pin(27, Pin.OUT)

# 터치 센서 연결 핀
touch1 = Pin(17, Pin.IN)
touch2 = Pin(5, Pin.IN)
touch3 = Pin(18, Pin.IN)
touch4 = Pin(19, Pin.IN)

# 온습도 센서 연결 핀
d = dht.DHT11(Pin(4))

# TV(I2C LCD) 연결 핀
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.clear()

# LCD 아이콘 
temp_icon = bytearray([0x04, 0x0A, 0x0A, 0x0E, 0x0E, 0x1F, 0x1F, 0x0E])
humi_icon = bytearray([0x04, 0x04, 0x0A, 0x0A, 0x11, 0x1F, 0x1F, 0x0E])
lcd.custom_char(0, temp_icon)
lcd.custom_char(1, humi_icon)

# 블루투스 연결
ble = bluetooth.BLE()
p = ble_library.BLESimplePeripheral(ble, "ESP_mini")

#OLED
oled = SoftI2C(sda=Pin(21), scl=Pin(22))
display = ssd1306.SSD1306_I2C(128, 64, oled)

display.fill(0)
display.show()

def on_rx(v): 
    print(v)
    # '1' 일 때 TV에 현재 온습도 정보 출력
    '''if v == '1':
        lcd.clear()
        print("1")
        d.measure()  # 온습도 센서 측정
        temp = str(int(d.temperature()))
        humi = str(int(d.humidity()))
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putchar(chr(0))
        lcd.putstr("temp : ")
        lcd.putstr(temp)
        lcd.putstr("C")
        lcd.move_to(0, 1)
        lcd.putchar(chr(1))
        lcd.putstr("humi : ")
        lcd.putstr(humi)
        lcd.putstr("%")
        p.send("temp : " + temp + "\n")
        p.send("humi : " + humi + "\n")
        '''
    # '2'일 때 TV에 밝기 출력
    if v == '2':
        lcd.clear()
        cds_value = cds.read()
        lcd.move_to(0, 0)
        lcd.putstr(str(cds_value))
        
        if cds_value > 3000:   
            lcd.move_to(0, 1)
            lcd.putstr("It's dark")
        else:
            lcd.move_to(0, 1)
            lcd.putstr("It's bright")
        p.send(str(cds_value) + "\n")

    # '3'일 때 TV 켜기
    if v == '3':
        lcd.backlight_on()
        
    # '4' 일 때 TV 끄기
    if v == '4':
        lcd.backlight_off()
    
    # '5' 일 때 멜로디1 출력
    if v == '5':
        speaker.duty_u16(1000)
        for i in melody1:
            speaker.freq(i)
            sleep(0.5)
        speaker.duty_u16(0) 

    # '6' 일 때 멜로디2 출력
    if v == '6':
        speaker.duty_u16(1000)
        for i in melody2:
            speaker.freq(i)
            sleep(0.5)
        speaker.duty_u16(0) 
    
    # '7' 일 때 전등 켜기
    if v == '7':
        LEDR.on()
        LEDG.on()
        LEDB.on()
    
    # '8' 일 때 전등 끄기
    if v == '8':
        LEDR.off()
        LEDG.off()
        LEDB.off()
  
    # '9' 일 때 OLED 그림
    if v == '9':
        with open('image/snoppy.pbm', 'rb') as f:
            f.readline() # 파일 방식
            f.readline() # 이미지 사이즈(가로 세로)
            data = bytearray(f.read())
        fb = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
        display.invert(0)
        display.fill(0)
        display.blit(fb, 0, 0)
        display.show()

p.on_write(on_rx)


while True:
    # 조도센서(블라인드 제어)
    cds_value = cds.read()
    #print(cds_value)
    
    if cds_value > 4000 and cds_flag == 1:
        speaker.duty_u16(1000)
        for i in blindMelody:
            speaker.freq(i)
            sleep(0.3)
        speaker.duty_u16(0) 
        motor.move(180)
        cds_flag = 0        
        
    elif cds_value <= 4000 and cds_flag == 0:
        motor.move(90)
        cds_flag = 1
        
     #터치 센서(LED 제어)
    if touch1.value():
        print("Button 1 touched")
        LEDR.on()
        LEDG.off()
        LEDB.off()
        
    elif touch2.value():
        print("Button 2 touched")
        LEDR.off()
        LEDG.on()
        LEDB.off()
    
    elif touch3.value():
        print("Button 3 touched")
        LEDR.off()
        LEDG.off()
        LEDB.on()
        
    elif touch4.value():
        print("Button 4 touched")
        LEDR.off()
        LEDG.off()
        LEDB.off()

    sleep(0.5)




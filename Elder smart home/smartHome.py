from machine import Pin, PWM, SoftI2C
from time import sleep
from servo import Servo

from lcd_api import LcdApi
from i2c_lcd import I2cLcd

import ble_library
import bluetooth

import ssd1306
import framebuf

# 서보 모터 연결 핀 (D13)
motor = Servo(pin=13)

# 피에조 부저 연결 (D23)
speaker = PWM(Pin(23))
speaker.duty_u16(0)

# LED 전등 연결 핀 (D25, D26, D27)
LEDR = Pin(25, Pin.OUT)
LEDG = Pin(26, Pin.OUT)
LEDB = Pin(27, Pin.OUT)

# 터치 센서 연결 핀 (D17, D5, D18, D19)
touch1 = Pin(17, Pin.IN)
touch2 = Pin(5, Pin.IN)
touch3 = Pin(18, Pin.IN)
touch4 = Pin(19, Pin.IN)

# I2C 설정 (LCD & OLED 공유)
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# I2C LCD 연결 (0x27)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.clear()
lcd.putstr("Meds System Ready")

# OLED 연결 (0x3C)
display = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
display.fill(0)
display.show()

# 복약 상태 저장 변수 (초기값 X)
med_records = {"Morning": "(X)", "Lunch": "(X)", "Dinner": "(X)"}

# 부저 알림음 멜로디 재생 함수 (도 - 미 - 솔)
def play_buzzer():
    notes = [523, 659, 784]
    speaker.duty_u16(1000)
    for freq in notes:
        speaker.freq(freq)
        sleep(0.15)
    speaker.duty_u16(0)

# 비상 전용 사이렌 멜로디 재생 함수 (삐뽀삐뽀)
def play_emergency_buzzer():
    speaker.duty_u16(1000)
    for _ in range(4):
        speaker.freq(880)
        sleep(0.15)
        speaker.freq(587)
        sleep(0.15)
    speaker.duty_u16(0)

# OLED 하루 복약 기록 갱신 함수
def update_oled():
    display.fill(0)
    display.text("[ Today Meds ]", 0, 0)
    display.text("Morning : " + med_records["Morning"], 0, 20)
    display.text("Lunch   : " + med_records["Lunch"], 0, 35)
    display.text("Dinner  : " + med_records["Dinner"], 0, 50)
    display.show()

# 복약 피드백 공통 동작 (초록색 LED 3회 반짝임)
def trigger_feedback():
    for _ in range(3):
        LEDG.on()
        sleep(0.15)
        LEDG.off()
        sleep(0.15)

# 블루투스 연결 및 이벤트 처리
ble = bluetooth.BLE()
p = ble_library.BLESimplePeripheral(ble, "ESP_mini")

def on_rx(v):
    try:
        cmd = v.decode().strip()
    except:
        cmd = v.strip()
    
    print("Received command:", cmd)
    if cmd == '1':
        lcd.backlight_on()
    elif cmd == '2':
        lcd.backlight_off()
    elif cmd == '3':
        LEDR.on()
        LEDG.on()
        LEDB.on()
    elif cmd == '4':
        LEDR.off()
        LEDG.off()
        LEDB.off()
    elif cmd == '5':
        motor.move(90)   # 블라인드 열기 (90도)
    elif cmd == '6':
        motor.move(0)    # 블라인드 닫기 (0도)
    elif cmd == '9':     # 캐릭터 이미지 로딩 (보너스 기능 유지)
        try:
            with open('image/snoppy.pbm', 'rb') as f:
                f.readline() # PBM 포맷 헤더 스킵
                f.readline() # 해상도 정보 스킵
                data = bytearray(f.read())
            fb = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
            display.fill(0)
            display.blit(fb, 0, 0)
            display.show()
        except Exception as e:
            print("OLED Image error:", e)

p.on_write(on_rx)

# OLED 초기 화면 업데이트
update_oled()

# 메인 감지 루프
while True:
    if touch1.value():
        print("Morning medication touched")
        med_records["Morning"] = "(O)"
        
        # LCD 표시 업데이트
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Morning Med")
        lcd.move_to(0, 1)
        lcd.putstr("Completed (O)")
        
        # OLED 업데이트 & BLE 전송
        update_oled()
        p.send("MED:MORNING\n")
        
        # 하드웨어 피드백
        play_buzzer()
        trigger_feedback()
        
        sleep(1.0) # 디바운스 대기
        
    elif touch2.value():
        print("Lunch medication touched")
        med_records["Lunch"] = "(O)"
        
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Lunch Med")
        lcd.move_to(0, 1)
        lcd.putstr("Completed (O)")
        
        update_oled()
        p.send("MED:LUNCH\n")
        
        play_buzzer()
        trigger_feedback()
        
        sleep(1.0)
        
    elif touch3.value():
        print("Dinner medication touched")
        med_records["Dinner"] = "(O)"
        
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Dinner Med")
        lcd.move_to(0, 1)
        lcd.putstr("Completed (O)")
        
        update_oled()
        p.send("MED:DINNER\n")
        
        play_buzzer()
        trigger_feedback()
        
        sleep(1.0)
        
    elif touch4.value():
        print("Emergency call touched")
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("EMERGENCY CALL!")
        lcd.move_to(0, 1)
        lcd.putstr("ALARM ACTIVATED")
        
        p.send("MED:EMERGENCY\n")
        play_emergency_buzzer()
        
        sleep(1.0)
        
    sleep(0.1)

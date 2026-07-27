# 📋 스마트홈 웹 대시보드 표준 제품 요구사항 정의서 (PRD_s)

### ESP32 Bluetooth NUS Web Controller — 고령자 스마트 복약/스마트홈 템플릿

---

> [!IMPORTANT]
> **이 문서의 사용 방법**
>
> 이 PRD_s 파일을 **Antigravity(안티그래비티)**에 제공하면, AI가 이 문서를 읽고 여러분만의 스마트홈 웹 대시보드와 ESP32 펌웨어를 처음부터 자동으로 만들어 줍니다.
>
> **시작 전에 아래 항목들을 본인의 정보로 채워주세요:**
>
> - `[park]` → 제작자 이름
> - `[ESP_mini]` → ESP32 블루투스 기기 이름
> - `[image/snoppy.pbm]` → OLED에 출력할 캐릭터 비트맵 파일
>

---

## 📌 0. 프로젝트 기본 정보

| 항목                     | 내용                                         |
| :----------------------- | :------------------------------------------- |
| **프로젝트명**     | "고령자 스마트홈 및 복약 관리 시스템"        |
| **제작자**         | `park`                                       |
| **BLE 기기명**     | `ESP_mini`                                   |
| **OLED 이미지**    | `image/snoppy.pbm`                           |
| **메인 컬러 테마** | 흰색계열 (Clean Light Theme)                 |

---

## 🔩 1. 하드웨어 시스템 사양 (Hardware Specifications)

ESP32 DEVKIT V1(30핀) 마이크로컨트롤러를 기반으로 각 센서/액추에이터 및 입력장치를 연결합니다.

### 1.1. 핀 결선 맵 (Pin Mapping) 및 담당 기능

| 하드웨어                 | 모델                  | ESP32 GPIO 핀 | 입출력          | 상세 기능 정의 |
| :----------------------- | :-------------------- | :------------ | :-------------- | :--- |
| **터치 센서 1번**  | TTP223                | D17           | 디지털 입력     | **아침** 약 복용 완료 입력 |
| **터치 센서 2번**  | TTP223                | D5            | 디지털 입력     | **점심** 약 복용 완료 입력 |
| **터치 센서 3번**  | TTP223                | D18           | 디지털 입력     | **저녁** 약 복용 완료 입력 |
| **터치 센서 4번**  | TTP223                | D19           | 디지털 입력     | 예비 / 비상 버튼 |
| **RGB LED (빨강)** | 공통 캐소드 RGB       | D25           | 디지털 출력     | 조명 제어 (PWM) |
| **RGB LED (초록)** | 공통 캐소드 RGB       | D26           | 디지털 출력     | 조명 제어 & 복약 완료 피드백 점멸 |
| **RGB LED (파랑)** | 공통 캐소드 RGB       | D27           | 디지털 출력     | 조명 제어 (PWM) |
| **서보 모터**      | SG90                  | D13           | PWM 출력        | 창문 블라인드 제어 (0~90°) |
| **피에조 부저**    | 패시브 부저           | D23           | PWM 주파수 출력 | 복약 확인 멜로디/알림음 |
| **LCD (SDA)**      | HD44780 I2C (0x27)    | D21           | I2C             | 복약 상태 및 안내 표출 |
| **LCD (SCL)**      | HD44780 I2C (0x27)    | D22           | I2C             | LCD 통신 클럭 |
| **OLED (SDA)**     | SSD1306 128x64 (0x3C) | D21           | I2C             | 하루치 복약 기록 상시 표출 |
| **OLED (SCL)**     | SSD1306 128x64 (0x3C) | D22           | I2C             | OLED 통신 클럭 |

---

## 📡 2. 블루투스 BLE NUS 통신 규격 (BLE Specification)

웹 앱과 ESP32는 **Nordic UART Service (NUS)** 프로토콜로 양방향 통신합니다.

### 2.1. NUS UUID 규격

| 채널                  | UUID                                     | 방향        |
| :-------------------- | :--------------------------------------- | :---------- |
| **NUS 서비스**  | `6e400001-b5a3-f393-e0a9-e50e24dcca9e` | —          |
| **RX (Write)**  | `6e400002-b5a3-f393-e0a9-e50e24dcca9e` | 웹 → ESP32 |
| **TX (Notify)** | `6e400003-b5a3-f393-e0a9-e50e24dcca9e` | ESP32 → 웹 |

---

## 🎮 3. 제어 및 복약 이벤트 동작 규격 (Control & Event Spec)

### 3.1. 터치패드 복약 입력 시 동작 (하드웨어 피드백 & OLED 기록)

터치패드(D17, D5, D18)를 누르면 **부저 알림음**과 함께 **OLED 디스플레이에 하루 동안의 복약 여부**가 실시간으로 갱신되어 표출됩니다.

1. **하드웨어 피드백 (터치 즉시):**
   * **피에조 부저 (D23):** 복약 성공 확인 멜로디(삐-빅!) 재생
   * **RGB LED (D26 초록색):** 초록색 3회 반짝임 피드백
2. **디스플레이 표출:**
   * **OLED (0x3C):** 아침, 점심, 저녁 복약 상태를 `(O)` / `(X)` 형태로 상시 유지 및 갱신
   * **LCD (0x27):** 복약 완료 상태 표출 (예: `Morning (O)`)
3. **웹 앱 전송:**
   * BLE NUS TX 채널을 통해 복약 캘린더 기록용 패킷 송신

### 3.2. 복약 이벤트 대응 표

| 입력 이벤트 | 핀 번호 | 부저 피드백 | OLED 기록 표출 (오늘 하루치) | 웹 앱 송신 패킷 |
| :--- | :---: | :--- | :--- | :--- |
| **터치 1번 (아침)** | D17 | 알림 멜로디 | `Morning : (O)` | `MED:MORNING\n` |
| **터치 2번 (점심)** | D5 | 알림 멜로디 | `Lunch   : (O)` | `MED:LUNCH\n` |
| **터치 3번 (저녁)** | D18 | 알림 멜로디 | `Dinner  : (O)` | `MED:DINNER\n` |

> **OLED 출력 화면 레이아웃 (SSD1306 예시):**
> ```text
> [ Today Med Status ]
>  Morning : (O)
>  Lunch   : (X)
>  Dinner  : (X)
> ```

### 3.3. 웹 → ESP32 제어 명령어 (ASCII 1글자)

웹 대시보드에서는 지정된 **6가지 핵심 제어 명령어**만 다룹니다.

| 제어 문자 | 기능 | ESP32 동작 |
| :---: | :--- | :--- |
| `'1'` | LCD 백라이트 켜기 | `lcd.backlight_on()` |
| `'2'` | LCD 백라이트 끄기 | `lcd.backlight_off()` |
| `'3'` | 조명 전등 켜기 | RGB LED WHITE 점등 |
| `'4'` | 조명 전등 끄기 | RGB LED 전체 소등 |
| `'5'` | 블라인드 열기 | 서보모터 D13 90° |
| `'6'` | 블라인드 닫기 | 서보모터 D13 0° |

### 3.4. 외부 날씨 API 연동 및 블라인드 자동 제어 (OpenWeather API)

웹 대시보드는 외부 날씨 API(OpenWeather API)와 연동하여 실시간 기상 상태 및 미세먼지 수치를 수집하고, 조건 충족 시 하드웨어를 자동으로 제어합니다.

1. **비 오는 날 제어:**
   * OpenWeather API 기준 현재 기상 상태가 'Rain', 'Thunderstorm', 'Drizzle'인 경우, 웹 앱은 자동으로 ESP32에 블라인드 닫기 명령어(`'6'`)를 전송합니다.
2. **미세먼지 높은 날 제어:**
   * 대기 질 API(Air Pollution API) 기준 PM2.5/PM10 농도 또는 AQI(Air Quality Index) 수치가 나쁨 수준(AQI 3단계 이상 또는 한국 기준 PM2.5 35µg/m³ 초과)인 경우, 웹 앱은 자동으로 ESP32에 블라인드 닫기 명령어(`'6'`)를 전송해 창문을 보호합니다.
3. **사용자 직접 제어 우선:**
   * 기상/미세먼지에 따른 자동 제어 명령이 작동 중이더라도, 사용자가 대시보드에서 직접 블라인드를 조작할 경우 수동 명령이 즉시 우선 처리됩니다.
4. **자동 제어 설정 및 활성화/비활성화 (On/Off Switch & Real-time Settings):**
   * **기능 On/Off 토글:** 웹 대시보드 UI에 "날씨 연동 자동 제어 활성화" 토글 스위치를 제공하여 사용자가 실시간 자동 작동 기능을 언제든지 켜고 끌 수 있게 합니다.
   * **실시간 설정 변동:** 사용자가 대시보드 화면에서 **OpenWeather API Key**, **대상 지역(도시명)**, 그리고 **날씨 감시 주기(Polling Interval, 예: 5분/10분/30분 등)**를 실시간으로 직접 변동하여 재설정할 수 있는 UI를 제공합니다.
   * **로컬 저장 및 복원:** 모든 변동된 설정 값(On/Off 토글 상태, API Key, 도시명, 감시 주기)은 브라우저의 LocalStorage에 실시간 저장되어, 새로고침이나 재접속 시에도 그대로 유지 및 자동 실행됩니다.
   * **비활성화 상태:** 기능이 Off(비활성화)로 꺼지면 날씨 감시 루프가 정지되며 기상 조건에 따른 자동 제어 명령(`'6'`)을 전송하지 않습니다.

---

## 🎨 4. UI/UX 디자인 & 픽토그램 가이드라인

### 4.1. 한글 미해득자 배려
* 글자 대신 대형 직관적인 그림으로 상태 표시:
* **실내 기구 수동 제어 버튼:**
  * 백라이트 켜기/끄기 (`'1'`, `'2'`)
  * 전등 켜기/끄기 (`'3'`, `'4'`)
  * 블라인드 열기/닫기 (`'5'`, `'6'`)

### 4.2. 일별 복용 캘린더 (Calendar View) & 로컬 데이터 지속성
* 웹 앱 상에 달력 UI를 제공합니다.
* ESP32로부터 `MED:MORNING`, `MED:LUNCH`, `MED:DINNER` 패킷을 전달받으면 해당 날짜의 캘린더 칸에 **알약 픽토그램/초록 체크(✔️)** 도장을 기록합니다.
* **데이터 영구 보존 (Local Storage / IndexedDB):**
  * BLE 연결이 해제되거나 브라우저 새로고침, 재접속 시에도 이전 복약 기록이 유지되도록 브라우저의 **LocalStorage** 또는 **IndexedDB**에 복약 내역 데이터를 저장합니다.
  * 대시보드 로드 시 LocalStorage에서 기존 복약 이력을 불러와 화면 및 캘린더 뷰를 복원합니다.

---

## 🚀 5. ESP32 MicroPython 핵심 구현 예시 (`smartHome.py`)

```python
import machine
import time
import ssd1306

# 복약 상태 저장 변수 (초기값 X)
med_records = {"Morning": "(X)", "Lunch": "(X)", "Dinner": "(X)"}

# 부저 알림음 멜로디 재생 함수
def play_buzzer():
    buzzer = machine.PWM(machine.Pin(23))
    # '도 - 미 - 솔' 복약 알림 멜로디
    notes = [523, 659, 784]
    for freq in notes:
        buzzer.freq(freq)
        buzzer.duty(512)
        time.sleep_ms(100)
    buzzer.duty(0)
    buzzer.deinit()

# OLED 하루 복약 기록 갱신 함수
def update_oled():
    oled.fill(0)
    oled.text("[ Today Meds ]", 0, 0)
    oled.text("Morning : " + med_records["Morning"], 0, 20)
    oled.text("Lunch   : " + med_records["Lunch"], 0, 35)
    oled.text("Dinner  : " + med_records["Dinner"], 0, 50)
    oled.show()

# 웹 제어 명령어 수신 처리 (6가지 지원)
def on_rx(v):
    if v == '3': lcd.backlight_on()
    elif v == '4': lcd.backlight_off()
    elif v == '7': R.on(); G.on(); B.on()  # 전등 켜기
    elif v == '8': R.off(); G.off(); B.off() # 전등 끄기
    elif v == 'o': servo.write_angle(90)   # 블라인드 열기
    elif v == 'c': servo.write_angle(0)    # 블라인드 닫기

# 터치패드 센서 입력 감지 루프
def check_touch_inputs():
    if touch_morning.value():
        med_records["Morning"] = "(O)"
        update_oled()
        play_buzzer()
        p.send("MED:MORNING\n")
        time.sleep(1) # 디바운스
        
    elif touch_lunch.value():
        med_records["Lunch"] = "(O)"
        update_oled()
        play_buzzer()
        p.send("MED:LUNCH\n")
        time.sleep(1)
        
    elif touch_dinner.value():
        med_records["Dinner"] = "(O)"
        update_oled()
        play_buzzer()
        p.send("MED:DINNER\n")
        time.sleep(1)
import serial  # 시리얼 통신을 하기 위한 라이브러리를 불러옵니다.
import time    # 시간을 정지시키는 명령어를 불러옵니다.

def create_serial_connection(port):
    try:
        connection = serial.Serial(f"COM{port}", 115200)
        print("아두이노 연결 성공")
        return connection
    except serial.SerialException:
        print(f"COM{port}에 연결 실패")
        return None

def find_arduino_connection():
    for portnum in range(1, 101):
        connection = create_serial_connection(portnum)
        if connection is not None:
            return connection
    print("100개의 포트를 모두 확인했지만, 아두이노 연결을 찾을 수 없습니다.")
    return None

def encode_servo_values(values):
    return [f"{v:03}".encode('utf-8') for v in values]

def move_servos(arduino, sv, number, gap):
    sv[number - 8] = gap  # 8번 핀부터 시작하는 번호를 고려하여 인덱스 조정
    arduino.write(b's')   # 시작 신호를 전송
    for val in encode_servo_values(sv):
        arduino.write(val)  # 인코딩된 서보 값 전송

# 메인 프로그램 실행
if __name__ == "__main__":
    user_input = input("///아두이노의 포트 번호만 입력하세요///\n예)COM8 -> 8\n포트번호: ")
    arduino = create_serial_connection(user_input) if user_input else find_arduino_connection()

    if arduino:
        sv = [90, 90, 90, 90]  # 서보모터 초기 위치 설정
        # 예시로 서보모터를 조작하는 부분, 필요에 따라 함수 호출
        move_servos(arduino, sv, number=8, gap=45)

